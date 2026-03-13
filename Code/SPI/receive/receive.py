from machine import SPI,Pin
import time

#initialize SPI0 on pico, baudrate or clock speed 1 MHZ, set clock idle low, set first clock edge, set sck = 18, mosi = 19, miso = 16
SPI = SPI(0, baudrate = 1000000, polarity = 0, phase = 0, sck = Pin(18), mosi = Pin(19), miso = Pin(16))

CS = Pin(17, Pin.OUT)   #chip select pin as output
CS.value(1)             #slave deselect

while True:
    CS.value(0)         #slave select
    data = SPI.read(5)  #read 5 byte
    CS.value(1)         #slave deselect
    time.sleep(1)