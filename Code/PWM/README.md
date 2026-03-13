# PWM (Pulse Width Modulation)

This folder contains examples demonstrating how to use Pulse Width Modulation (PWM) on the Raspberry Pi Pico. PWM is useful for dimming LEDs, controlling motors, and producing varying average voltage levels.

## Examples

### 1. `PWM_50%_power`
A simple example demonstrating how to set a fixed PWM duty cycle.
- **File**: `50_power.py`
- **Setup**: Connect a measuring device (like an oscilloscope or multimeter) or an LED (with a resistor) to **Pin 16**.
- **Functionality**: Initializes PWM on GP16 with a frequency of 1 kHz. It calculates a 50% duty cycle (`int(0.5 * 65535)`) and applies it, effectively outputting half the maximum voltage.

### 2. `PWM_with_ADC`
An interactive example that maps an analog input to a PWM output duty cycle. This is perfect for an LED dimmer circuit.
- **File**: `PWM_with_ADC.py`
- **Setup**: 
  - Connect a potentiometer to **Pin 26** (ADC0) to act as the analog input.
  - Connect an LED (with a resistor) to **Pin 16** for the PWM output.
- **Functionality**: Continuously reads the 16-bit analog value (0-65535) from the potentiometer and passes it directly to `duty_u16()` for the PWM signal. As you turn the potentiometer, the LED brightness changes proportionally.
