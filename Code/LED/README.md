# LED Control

This simple example demonstrates how to control a digital output pin to blink an LED.

## Files
- The project is inside the `LED blink` folder.
- `LED_blink.py`: Turns an external LED on and off at regular intervals.

## Hardware Setup
- Connect an LED to **Pin 16**. Remember to wire the LED in series with an appropriate current-limiting resistor (e.g., 220Ω or 330Ω) connecting to GND.

## How it Works
1. Sets up GP16 as a digital output (`Pin(16, Pin.OUT)`).
2. Enters an infinite `True` loop.
3. Sets the pin value to `1` (HIGH) to turn the LED on.
4. Pauses for 1 second (`time.sleep(1)`).
5. Sets the pin value to `0` (LOW) to turn the LED off.
6. Pauses for 1 second before repeating the cycle.
