from machine import Pin
import time

button = Pin(15, Pin.IN, Pin.PULL_DOWN) #Set pin 15 as an input a pull down resister

while True:                 #loop forever
    print(button.value())   #read the digital sate of the button
    time.sleep(0.1)