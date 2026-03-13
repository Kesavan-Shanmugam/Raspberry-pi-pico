# UART Communication

This folder contains examples demonstrating how to use UART (Universal Asynchronous Receiver-Transmitter) for serial communication on the Raspberry Pi Pico.

## Hardware Setup
For all examples, UART1 is initialized on the following default pins:
- **TX (Transmit)**: Pin 4 (GP4)
- **RX (Receive)**: Pin 5 (GP5)
The baud rate is set to 9600.

## Examples

### 1. `Transmit` (Pico A)
Demonstrates sending data over UART.
- **File**: `transmit.py`
- **Functionality**: Continuously sends the string `'ON/n'` and then `'OFF'` over UART1, with a 2-second delay between transmissions.

### 2. `receive` (Pico B)
Demonstrates receiving data and using it to control hardware.
- **File**: `receive.py`
- **Setup**: Besides UART, this script assumes an LED is connected to the pin named `"LED"` (which usually maps to the onboard LED on the Pico, GP25).
- **Functionality**: Continuously checks if data is available (`UART2.any()`). If it is, it reads and decodes the message. If the message is exactly `'ON'`, it turns on the LED. If it's `'OFF'`, it turns it off.

### 3. `self transmit and receive` (Loopback Test)
A self-contained test to verify UART functionality by sending and receiving on the same board.
- **File**: `Self_T_R.py`
- **Setup**: **Connect TX (Pin 4) directly to RX (Pin 5) with a jumper wire.** Connect an external LED to **Pin 16**.
- **Functionality**: The script writes `'ON'` to UART1. Because TX is connected to RX, it immediately reads `'ON'` from the buffer and turns on the LED on Pin 16. It then writes `'OFF'`, reads it, and turns the LED off.
