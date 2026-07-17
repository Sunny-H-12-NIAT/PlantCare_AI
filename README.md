# 🌱 PlantCare AI - SmartSpray Node

**Team:** TECH TITANS
**Members:** Sai Charan Reddy, Dhruv Sagar, Sree Charan Reddy, Vignesh Arya, Rithvik, Sai Ram
**Author:** K. Sai Charan Reddy, AI/ML Scholar at NxtWave Institute of Advanced Technologies

![Main Project Setup](images/main_setup.png)
*(Place a clear, wide photograph of your entire working setup here)*

---

## 📖 The Big Picture: What is this project?

Imagine having a robot gardener that never sleeps. That is exactly what PlantCare AI is. 

In a normal garden, you have to walk around, look at your plants, and guess if they need water or if they are getting sick from a disease. We decided to automate this entire process using Artificial Intelligence (AI) and some simple electronics. 

Here is exactly how our system works, step-by-step:
1. **The Eyes:** We use a smartphone camera or a webcam pointing at the plants. This acts as the eyes of our system.
2. **The Brain:** We trained an Artificial Intelligence model (a very smart computer program) to look at the video feed and recognize three things: 
   * A completely healthy plant.
   * A dry plant that is dying of thirst.
   * A diseased plant that has an infection.
3. **The Nerves:** Once the AI makes a decision, our Python code talks to a tiny microcontroller board called an ESP32. This board is connected to your computer via a USB cable.
4. **The Muscles:** The ESP32 sends electrical signals to "Relays." A relay is just a digital light switch. When the ESP32 says "TURN ON!", the relay clicks closed and allows electricity from a battery pack to flow into a water pump.
5. **The Action:** If the plant is dry, the water pump turns on for 10 seconds. If the plant is diseased, a completely different pump turns on to spray pesticide for 10 seconds.

This project proves that we can use computer vision to protect our agriculture automatically!

---

## 🔌 Picture-Perfect Hardware Guide

When building hardware, you have to be extremely precise. One wrong wire can stop the whole machine. Here is every single piece you need.

![All Hardware Components](images/all_components.png)
*(Place a picture of all your parts laid out on a table here)*

**The Parts List:**
* **ESP32 Microcontroller:** This is the black circuit board with the silver square on it. It receives commands from your computer.
* **Two 5V Relay Modules:** These are the blue boxes on little green circuit boards. They act as the switches for your pumps. 
* **Two 5V Submersible Pumps:** These are the white plastic tubes that actually push the liquid.
* **One Breadboard:** The white plastic board with lots of holes. We use this to share power.
* **4xAA Battery Pack:** This provides the heavy electrical lifting to spin the pumps.
* **Jumper Wires:** The colorful wires used to connect everything together.

### The Exact Wiring Instructions

![Wiring Close Up](images/wiring_closeup.png)
*(Place a close-up picture of your wires plugged into the breadboard and ESP32 here)*

**Powering the Relays (The 5V Power Sharing):**
Your ESP32 only has one 5V power pin, but you have two relays that need 5V to click. 
* Connect the **V5** (or VIN) pin on the ESP32 to a row on your breadboard.
* Connect the **VCC** wire from Relay 1 into that exact same breadboard row.
* Connect the **VCC** wire from Relay 2 into that exact same breadboard row.
* Connect the **GND** (Ground) wire from both relays to any **GND** pin on the ESP32.

**Connecting the Brain to the Switches:**
* Connect a wire from **Pin 23** on the ESP32 to the **IN** pin on Relay 1 (Water Pump).
* Connect a wire from **Pin 22** on the ESP32 to the **IN** pin on Relay 2 (Pesticide Pump).

---

## 💻 Download Dependencies

Before you can run the code, you need to teach your computer how to understand the specific commands we wrote. We do this by downloading "Dependencies" or "Libraries". Think of these like adding new vocabulary words to your computer's dictionary.

Open your computer's terminal (the black coding screen) and type exactly what is written in the grey boxes below. Press ENTER after each one and wait for it to finish downloading.

### 1. download opencv
This allows your computer code to open your phone's camera and look at images.
```bash
pip install opencv-python

### 2. download numpy
**What is this and why do we need it?**
To a computer, a picture of a leaf is not a green object; it is just a massive grid of thousands of tiny numbers that represent colors. NumPy (which stands for Numerical Python) is a powerful mathematical tool that takes the video from your camera and instantly chops it up into these giant grids of numbers. Without NumPy, our AI would have no idea how to read the picture because it only understands numbers, not images. 
**The Installation Command:**
```bash
pip install numpy

3. download tensorflow

What is this and why do we need it?
This is the absolute core of our project. TensorFlow is a massive Artificial Intelligence engine created by Google. We are using a special, lightweight version of it called "TensorFlow Lite." When NumPy turns the camera picture into numbers, it hands those numbers over to TensorFlow. TensorFlow then uses its "brain" (the model we trained) to scan the numbers and make a final decision: "Is this plant Healthy, Dry, or Diseased?" It is the decision-maker of the entire operation.
The Installation Command:
(Note: This is a very large file, so your computer might take a few minutes to finish downloading it. Just let it load!)

```bash
pip install tensorflow

4. download pyserial
What is this and why do we need it?
Once TensorFlow decides a plant is Dry or Diseased, it needs a way to tell the water pumps to turn on. The problem is, the AI lives inside your computer, but the pumps are connected to the ESP32 board outside the computer. PySerial acts as a digital bridge. It takes the text commands from our Python code (like the letter 'S' for Spray) and pushes them through your USB cord directly into the ESP32 board.
The Installation Command:
(Warning: Make sure you type pyserial and NOT just serial, otherwise you will download the wrong package!)

Bash
pip install pyserial
5. download supabase
What is this and why do we need it?
We want our SmartSpray Node to be a modern Internet-of-Things (IoT) device. That means it needs to talk to the internet. Supabase is a cloud database service. Every single time our AI detects a problem and turns on a pump, this library takes that information, securely connects to the internet, and writes a log entry in our cloud database. This allows us to check on our plants from anywhere in the world just by looking at our Supabase dashboard!
The Installation Command:

Bash
pip install supabase
🚀 System Starting: The Boot-Up Sequence
Now that your computer has all the vocabulary it needs, it is time to bring the hardware and software together. You must follow these steps in this exact order, or the system will experience a "traffic jam" on the USB port!

Step 1: Uploading the Brain's Firmware
First, we have to teach the ESP32 board how to listen for our Python commands.

Open the file named sketch_jul15a.ino using the Arduino IDE software on your computer.

Plug your ESP32 board into your computer using a USB cable.

In the Arduino software, go to the top menu, click Tools -> Port, and select the COM port your board is plugged into (for example, COM7).

Click the Upload button (the arrow pointing to the right at the top left of the screen).

Wait for the green bar to load at the bottom. Once it says "Done uploading", the ESP32 is officially ready.

Step 2: The Most Important Failsafe
YOU MUST CLOSE THE ARDUINO SOFTWARE NOW.
If you leave the Arduino program or its Serial Monitor open, it will hold your USB port hostage. When Python tries to connect to the ESP32 to turn on the pumps, it will crash and say "Access is Denied." Close the Arduino window completely!

🤖 Running the AI: Let the Magic Happen
You are finally ready to turn on the robot gardener.

Step 1: Set Up the Camera Eyes
If you are using a smartphone as your camera:

Connect your phone and your computer to the exact same Wi-Fi network.

Open your IP Webcam app on your phone and click "Start Server".

The app will show a web address on your phone screen (like http://10.10.19.192:8080).

Make sure that exact address is typed into your main.py code where it says phone_camera_url.

Step 2: Start the Engine
Open your code editor (like VS Code).

Open the Terminal window at the very bottom.

Make sure you are inside your PlantCare_AI folder.

Type this final command and hit ENTER:

Bash
python main.py
Step 3: Watch It Work!
A new window will pop up on your computer screen showing exactly what your phone camera sees.

Point the camera at a healthy plant. The text will turn Green, and the pumps will stay silent.

Point the camera at a picture of a Dry Plant. The text will turn Yellow, the ESP32 will flash, the relay will CLICK, and the Water Pump will turn on for exactly 10 seconds!

Point the camera at a picture of a Diseased Plant. The text will turn Red, the ESP32 will route the signal, the second relay will CLICK, and the Pesticide Pump will trigger for exactly 10 seconds!
