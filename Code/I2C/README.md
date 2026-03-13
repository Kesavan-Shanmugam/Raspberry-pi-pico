# I2C Communication

This folder contains examples demonstrating how to use the I²C (Inter-Integrated Circuit) protocol on the Raspberry Pi Pico for device communication and interfacing with peripherals like an OLED display.

## Examples

### 1. `OLED`
Demonstrates how to interface with an SSD1306 OLED display over I2C to display text.
- **File**: `OLED.py`
- **Hardware Setup**: Connect an I2C OLED display. Connect the SDA line to **Pin 8** and the SCL line to **Pin 9**.
- **Functionality**: Initializes I2C0 at 400kHz. Clears the display and writes "Hello, KESAVAN" starting at coordinate (0,0).
- **Libraries**: This code requires the `ssd1306.py` library to be present on the Pico to function.

### 2. `transmit` (I2C Master)
Demonstrates sending data over I2C to another device acting as a slave.
- **File**: `transmit.py`
- **Hardware Setup**: Connect the Pico's I2C lines to a slave device. Connect SDA to **Pin 0** and SCL to **Pin 1**.
- **Functionality**: Initializes I2C0 at 100kHz. It continuously writes byte strings (`b'ON'` and `b'OFF'`) to the slave device at address `0x08`, pausing 1 second between transmissions.

### 3. `receive` (I2C Master Reading)
Demonstrates reading data over I2C from a slave device.
- **File**: `receive.py`
- **Hardware Setup**: Connect the Pico's I2C lines to a slave device. Connect SDA to **Pin 0** and SCL to **Pin 1**.
- **Functionality**: Initializes I2C0 at 100kHz. It continuously requests and reads 2 bytes of data from the slave device at address `0x08` every 1 second, printing the received data to the console.
