# Raspberry Pi Pico MicroPython Examples

This repository contains a collection of MicroPython code examples for the **Raspberry Pi Pico** (and Pico W). These examples are designed to serve as a comprehensive, "A to Z" guide for interfacing the Pico with various hardware components, communication protocols, and basic electronics.

Each folder contains its own detailed `README.md` explaining the code, hardware setup, and necessary pin connections.

## Repository Contents

### 1. Basic I/O & Analog
* **[ADC (Analog to Digital Converter)](ADC/)**: Read analog voltages (e.g., from a potentiometer) and convert them to digital values.
* **[Button (Digital Input)](Button/)**: Handle push button inputs, including state reading and turning on an LED when pressed.
* **[LED (Digital Output)](LED/)**: Basic digital output to blink an LED.
* **[PWM (Pulse Width Modulation)](PWM/)**: Generate PWM signals to control LED brightness, including an interactive example using an ADC input.

### 2. Communication Protocols
* **[I2C](I2C/)**: Examples of I²C communication, including interfacing with an OLED display (`SSD1306`) and basic master transmit/receive operations.
* **[SPI](SPI/)**: Examples of SPI communication, featuring transmit, receive, and a self-loopback testing script.
* **[UART](UART/)**: Universal Asynchronous Receiver-Transmitter examples, covering basic data transmission, receiving commands to control an LED, and loopback testing.

### 3. Motor Control
* **[Servo Motor](Servo%20motor/)**: Control standard hobby servo motors using PWM. Includes examples for moving to specific angles and sweeping smoothly using loops.

### 4. Networking (Pico W Only)
* **[WiFi Connect](wifi%20connect/)**: Connect the Raspberry Pi Pico W to a local Wi-Fi network and host a simple HTTP web server to toggle an LED over the internet.

## Getting Started

### Prerequisites
1. **Hardware**:
   - A Raspberry Pi Pico or Pico W.
   - A breadboard and assorted jumper wires.
   - Basic components: LEDs, resistors (e.g., 330Ω), push buttons, potentiometers.
   - Specific modules as needed by the examples (Servo motor, I2C OLED display).
2. **Software**:
   - [Thonny IDE](https://thonny.org/) (Recommended) or another MicroPython-compatible editor.
   - Appropriate MicroPython firmware flashed to your Pico.

### How to Use This Repository
1. Navigate to the folder of the component or protocol you want to learn about.
2. Read the local `README.md` file for specific wiring instructions.
3. Open the `.py` script in Thonny and save it to your Pico.
4. Run the script!

## Note on Libraries
Certain examples (like the OLED display and Servo motor) rely on external library files to function (e.g., `ssd1306.py`). Be sure to upload these library files directly to the root directory of your Raspberry Pi Pico before running the main scripts. All required libraries are mentioned in their respective component folders.
