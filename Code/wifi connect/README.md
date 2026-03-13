# WiFi Connect and Web Server

This example demonstrates how to connect the Raspberry Pi Pico W to a local Wi-Fi network and host a simple web server to control an LED over the internet.

**Note:** This code requires a **Raspberry Pi Pico W**, as the standard Pico does not have a Wi-Fi module.

## Files
- `wifi_connect.py`: Connects to Wi-Fi, starts a socket server, and serves an HTML page with buttons to toggle an LED.

## Hardware Setup
- The code uses **Pin 1** (`led = Pin(1, Pin.OUT)`) for the output LED. Connect an LED (with a suitable resistor) to GP1. 
*(Note: If you want to use the Pico W's onboard LED, the pin designation is usually `"LED"` instead of `1`)*.

## How it Works
1. **Network Setup**: You must enter your network credentials in the `ssid` and `password` variables.
2. **Connection (`connect()`)**: It initializes the WLAN interface in Station mode (`STA_IF`), activates it, and attempts to connect. It loops until the connection is successful, printing the assigned IP address to the console.
3. **Web Server (`open_socket()`)**: Binds a standard socket to port 80 (HTTP) to listen for incoming connections from a web browser.
4. **Main Loop**: 
   - Accepts incoming client connections.
   - Reads the HTTP request (e.g., `GET /on? HTTP/1.1`) to parse the requested path.
   - If the path is `/on?`, it drives GP1 high. If `/off?`, it drives it low.
   - It generates an HTML page with two interactive forms (buttons) reflecting the current state, sends the HTTP response back to the client, and closes the connection.

To use this, run the script, find the IP address printed in the console (e.g., `192.168.1.100`), and enter that address into a web browser on a device connected to the same network.
