# Push Button Inputs

This folder contains functional examples showing how to handle push button inputs on the Raspberry Pi Pico.

## Examples

### 1. `Button sate`
This basic example reads the state of a push button and prints it to the console.
- **File**: `Button_state.py`
- **Setup**: Connect a push button to **Pin 15**. The code uses an internal pull-down resistor (`Pin.PULL_DOWN`), meaning the pin reads `0` when not pressed. Connect the other side of the button to 3.3V, so it reads `1` when pressed.
- **Functionality**: Loops infinitely, printing the digital state of the button (1 or 0) every 0.1 seconds.

### 2. `Button on led on`
This example combines an input button with an output LED.
- **File**: `Button_on_led_on.py`
- **Setup**: Connect a push button to **Pin 15** (pull-down). Connect an LED (with a suitable resistor) to **Pin 16**.
- **Functionality**: When the button holds a high value (pressed), it turns on the LED connected to GP16. When the button is released, the LED turns off.
