import network
import socket
import time
from machine import Pin

# LED
led = Pin(1, Pin.OUT)
state = "OFF"

# WiFi Details
ssid = "iot"
password = "12345678"

# ---------------------------
# WiFi Connect
# ---------------------------
def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while wlan.isconnected() == False:
        print("Connecting, please wait...")
        time.sleep(1)

    print("Connected")
    print("IP Address:", wlan.ifconfig()[0])

# ---------------------------
# Web Page
# ---------------------------
def web_page(state):
    html = f"""<!DOCTYPE html>
<html>
<body>
<h2>Pico W LED Control</h2>

<form action="/on">
<input type="submit" value="Turn ON">
</form>

<form action="/off">
<input type="submit" value="Turn OFF">
</form>

<p>LED state: {state}</p>

</body>
</html>
"""
    return html

# ---------------------------
# Open Socket
# ---------------------------
def open_socket():
    address = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
    s = socket.socket()
    s.bind(address)
    s.listen(1)
    return s

connect()
s = open_socket()

try:
    while True:
        client = s.accept()[0]
        request = client.recv(1024)
        request = request.decode()

        try:
            path = request.split()[1]
        except IndexError:
            pass

        print("Request:",path)

        if path == "/on?":
            led.value(1)
            state = "ON"


        elif path == "/off?":
            led.value(0)
            state = "OFF"


        html = web_page(state)
        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        client.send(html)
        client.close()

except OSError as e:
    print("Error: connection terminated")
