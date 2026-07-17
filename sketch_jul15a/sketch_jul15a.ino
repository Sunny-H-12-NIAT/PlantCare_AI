#define WATER_RELAY_PIN 23
#define PEST_RELAY_PIN 22

void setup() {
  Serial.begin(115200);
  
  // Set both pins as INPUT to act like physically disconnected wires (OFF)
  pinMode(WATER_RELAY_PIN, INPUT); 
  pinMode(PEST_RELAY_PIN, INPUT);
  
  Serial.println("System Ready. Both pumps are completely OFF.");
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); 
    
    // WATER COMMAND
    if (command == 'S') {
      Serial.println("Action: Dry Plant detected. Spraying WATER for 10 seconds...");
      
      pinMode(WATER_RELAY_PIN, OUTPUT);
      digitalWrite(WATER_RELAY_PIN, LOW);   
      delay(10000); // 10 seconds
      pinMode(WATER_RELAY_PIN, INPUT);  
      
      Serial.println("Watering complete. Standing by.");
    }
    
    // PESTICIDE COMMAND
    if (command == 'P') {
      Serial.println("Action: Diseased Plant detected. Spraying PESTICIDE for 10 seconds...");
      
      pinMode(PEST_RELAY_PIN, OUTPUT);
      digitalWrite(PEST_RELAY_PIN, LOW);   
      delay(10000); // 10 seconds
      pinMode(PEST_RELAY_PIN, INPUT);  
      
      Serial.println("Pesticide treatment complete. Standing by.");
    }
  }
}