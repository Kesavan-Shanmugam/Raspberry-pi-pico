from machine import I2C, Pin
import time 

#initialize I2C on pico, set clock pin and data pin, standard frequency 100KHZ
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)

addr = 0x08   # slave address

while True: 
    i2c.writeto(addr, b'ON')
    print("Sent ON")
    time.sleep(1)

    i2c.writeto(addr, b'OFF')
    print("Sent OFF")
    time.sleep(1)
