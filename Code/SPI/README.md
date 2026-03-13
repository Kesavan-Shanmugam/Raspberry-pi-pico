# SPI Communication

This folder contains examples demonstrating how to use the SPI (Serial Peripheral Interface) protocol on the Raspberry Pi Pico. SPI is a fast, synchronous serial communication protocol often used for displays, SD card readers, and sensor interfacing.

## Hardware Setup
For all examples in this section, SPI0 is initialized on the following default pins:
- **SCK (Serial Clock)**: Pin 18 (GP18)
- **MOSI (Master Out Slave In / TX)**: Pin 19 (GP19)
- **MISO (Master In Slave Out / RX)**: Pin 16 (GP16)
- **CS (Chip Select)**: Pin 17 (GP17) - *Manually managed via digital output in transmit/receive tests.*

The clock runs at 1 MHz, with Polarity 0 (clock idle low) and Phase 0 (trigger on first edge).

## Examples

### 1. `transmit` (SPI Transmit Only)
Demonstrates basic data transmission to an SPI slave.
- **File**: `transmit.py`
- **Functionality**: Drives the Chip Select (CS) pin low to select the slave, transmits the byte string `b'ON'`, pulls the CS pin high to deselect, and pauses for 1 second.

### 2. `receive` (SPI Receive Only)
Demonstrates reading data from an SPI slave.
- **File**: `receive.py`
- **Functionality**: Selects the slave via CS, reads 5 bytes of data via `SPI.read(5)`, deselects the slave, and waits 1 second before doing it again.

### 3. `Self transmit, receive` (SPI Loopback)
A helpful testing script that verifies the SPI bus is working correctly by sending and receiving data simultaneously on the same bus.
- **File**: `Self_T_R.py`
- **Setup**: **Connect MISO (Pin 16) directly to MOSI (Pin 19) with a jumper wire.** Connect an LED to Pin 15.
- **Functionality**: The script sends `b'ON'` and `b'OFF'` strings over MOSI using `write_readinto()`. Since MOSI and MISO are physically shorted, the same string is immediately read back into the receive buffer (`rx`). If it receives `b'ON'`, it turns on an LED on Pin 15. If it receives `b'OFF'`, it turns off the LED.
