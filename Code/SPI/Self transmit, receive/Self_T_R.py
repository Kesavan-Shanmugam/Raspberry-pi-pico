from machine import SPI, Pin
import time

#initialize SPI0 on pico, baudrate or clock speed 1 MHZ, set clock idle low, set first clock edge, set sck = 18, mosi = 19, miso = 16
spi = SPI(0, baudrate=1000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))

led = Pin(15, Pin.OUT)   # separate pin


while True:
    # ---- ON ----
    tx = b'ON'                      #transmit data byte
    rx = bytearray(len(tx))         #receive buffer, same length transmit    
    spi.write_readinto(tx, rx)      #SPI send and receive together
    print("RX :", rx.decode())

    if rx == b'ON':
        led.value(1)

    time.sleep(1)

    # ---- OFF ----
    tx = b'OFF'                     #transmit data byte
    rx = bytearray(len(tx))         #receive buffer, same length transmit   
    spi.write_readinto(tx, rx)      #SPI send and receive together
    print("RX :", rx.decode())

    if rx == b'OFF':
        led.value(0)

    time.sleep(1)
