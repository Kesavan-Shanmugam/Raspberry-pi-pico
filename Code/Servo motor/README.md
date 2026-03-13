# Servo Motor Control

This folder demonstrates how to control standard servo motors using Pulse Width Modulation (PWM) on the Raspberry Pi Pico.

**Note:** Both examples rely on a custom `servo.py` library which must be present on the Pico to provide the `Servo` class.

## Hardware Setup
- Connect the servo's control signal wire (usually yellow, orange, or white) to **Pin 0** on the Pico.
- Connect the servo's power wire (red) to VBUS (5V) if the servo requires 5V, or 3.3V if it's a 3.3V micro-servo.
- Connect the servo's ground wire (brown or black) to a GND pin on the Pico.

## Examples

### 1. `servo` (Fixed Angles)
This script demonstrates basic absolute positioning.
- **File**: `servo.py`
- **Functionality**: Loops infinitely, commanding the servo to turn to specific angles: 0°, 30°, 60°, 90°, 120°, 150°, and 180°, pausing 1 second at each position.

### 2. `servo_using_for_loop` (Smooth Sweeping)
This script demonstrates smooth movement using iterative steps.
- **File**: `using_for_loop.py`
- **Functionality**: Uses a `for` loop to sweep the servo continuously from 0 to 180 degrees in 5-degree increments (with a 0.1s delay between steps), and then sweeps back from 180 to 0 degrees.
