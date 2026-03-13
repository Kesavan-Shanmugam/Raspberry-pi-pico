from machine import I2C, Pin
import time

#initialize I2C on pico, set clock pin and data pin, standard frequency 100KHZ
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)
addr = 0x08   # slave address

while True:
    data = i2c.readfrom(addr, 2)   # read 2 bytes
    print(data)
    time.sleep(1)
