# ADC (Analog to Digital Converter)

This simple example demonstrates how to read analog values using the Raspberry Pi Pico's built-in ADC. 

## Files
- `ADC_check.py`: Reads the analog voltage from an input pin and prints it to the console.

## Hardware Setup
- Connect an analog sensor (e.g., a potentiometer) to **Pin 26** (ADC0).
- For a potentiometer, connect the outer pins to 3.3V and GND, and the middle pin to Pin 26.

## How it Works
1. Initializes `ADC(Pin(26))` to configure GP26 as an analog input.
2. The ADC reads 16-bit values range from 0 to 65535 (`read_u16`).
3. These readings are multiplied by a `conversion_factor` (`3.3 / 65535`) to map the raw ADC value to a voltage range of 0.0V to 3.3V.
4. It continuously reads and prints the voltage to the console every 0.1 seconds.
