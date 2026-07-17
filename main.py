import cv2
import numpy as np
import tensorflow as tf
import time
import serial
from supabase import create_client, Client

# -----------------------------
# 1. Supabase Cloud Setup
# -----------------------------
SUPABASE_URL = "https://hgukstnjqsqmcvhmpaxg.supabase.co"
SUPABASE_KEY = "sb_publishable_yi7y4eKRpUf7PtBsj2stGA_yZbT5uIH"

try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    print("☁️ Connected to Supabase Cloud!")
except Exception as e:
    print(f"⚠️ Warning: Could not connect to Supabase: {e}")
    supabase = None

def log_to_cloud(condition, action):
    """Pushes the AI detection event directly to the Supabase database."""
    if supabase:
        try:
            data = {"condition": condition, "action": action}
            supabase.table('plant_logs').insert(data).execute()
            print(f"✅ Cloud Log Saved: {condition} -> {action}")
        except Exception as e:
            print(f"❌ Failed to log to cloud: {e}")

# -----------------------------
# 2. ESP32 Serial Setup
# -----------------------------
try:
    # Connect to the ESP32 on COM7
    esp32 = serial.Serial('COM7', 115200, timeout=1)
    print("🔌 Connected to ESP32 on COM7")
except Exception as e:
    print(f"⚠️ Warning: Could not connect to ESP32: {e}")
    esp32 = None

# -----------------------------
# 3. Load TFLite Model & Labels
# -----------------------------
with open("converted_tflite_quantized/labels.txt", "r") as f:
    labels = [line.strip().split(" ", 1)[1] for line in f.readlines()]

interpreter = tf.lite.Interpreter(
    model_path="converted_tflite_quantized/model.tflite"
)

interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

height = input_details[0]["shape"][1]
width = input_details[0]["shape"][2]

print("🧠 Model Loaded Successfully")

# -----------------------------
# 4. Open Camera Stream
# -----------------------------
phone_camera_url = "http://10.10.19.192:8080/stream.mjpg"
cap = cv2.VideoCapture(phone_camera_url)

# Detect once every 30 seconds to prevent flooding
DETECTION_INTERVAL = 30
last_detection_time = 0

# Initial display values
label = "Initializing Scan..."
confidence = 0
color = (255, 255, 255)

# -----------------------------
# 5. Main Processing Loop
# -----------------------------
while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to access camera")
        break

    current_time = time.time()
    time_since_last_scan = current_time - last_detection_time

    # Run AI only when the cooldown timer finishes
    if time_since_last_scan >= DETECTION_INTERVAL:

        # Format image for TFLite
        image = cv2.resize(frame, (width, height))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = np.expand_dims(image, axis=0)
        image = image.astype(np.uint8)

        # Run Prediction
        interpreter.set_tensor(input_details[0]["index"], image)
        interpreter.invoke()
        prediction = interpreter.get_tensor(output_details[0]["index"])[0]
        
        index = np.argmax(prediction)
        confidence = prediction[index] / 255.0 * 100
        label = labels[index]

        # -----------------------------
        # 6. Action & Hardware Trigger
        # -----------------------------
        action_taken = "None"

        if label == "Healthy Plants":
            color = (0, 255, 0) # Green
            action_taken = "No action needed"

        elif label == "Dry Plants":
            color = (0, 255, 255) # Yellow
            if esp32:
                esp32.write(b'S')
                print(f"💧 Command 'S' sent! Watering {label}...")
            action_taken = "Water Pump activated for 10s"

        elif label == "Diseased Plants":
            color = (0, 0, 255)   # Red
            if esp32:
                esp32.write(b'P')
                print(f"🧪 Command 'P' sent! Applying pesticide to {label}...")
            action_taken = "Pesticide Pump activated for 10s"

        # Update detection time to reset the cooldown
        last_detection_time = current_time

        # Print to local terminal & send data to Supabase Dashboard
        print(f"Detected: {label} ({confidence:.1f}%)")
        log_to_cloud(label, action_taken)

    # -----------------------------
    # 7. Display Results & Telemetry
    # -----------------------------
    # Primary Label
    text = f"Status: {label} ({confidence:.1f}%)"
    cv2.putText(frame, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    
    # Dynamic Cooldown Timer (Calculates seconds remaining)
    remaining_time = max(0, int(DETECTION_INTERVAL - (current_time - last_detection_time)))
    if remaining_time > 0:
        timer_text = f"Next Scan In: {remaining_time}s"
        cv2.putText(frame, timer_text, (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 2)
    else:
        cv2.putText(frame, "Scanning...", (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("PlantCare AI - SmartSpray Node", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Clean up hardware and windows
cap.release()
cv2.destroyAllWindows()
if esp32:
    esp32.close()