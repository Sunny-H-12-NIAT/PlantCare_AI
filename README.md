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