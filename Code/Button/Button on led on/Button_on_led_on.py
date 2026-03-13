from machine import Pin
import time

button = Pin(15, Pin.IN, Pin.PULL_DOWN) #Set pin 15 as an input a pull down resister
led = Pin(16, Pin.OUT)

while True:                 #loop forever
    
    if button.value() == 1: #if the buttom pressed, then turn on led
        led.value(1)
        #print(button.value())
        #time.sleep(0.1)
    
    else:                   #if its not pressed, then turn off led
        led.value(0)
        #print(button.value())
        #time.sleep(0.1)
    