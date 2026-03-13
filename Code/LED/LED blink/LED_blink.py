from machine import Pin
import time

led = Pin(16, Pin.OUT) #set up pin 16

while True:        #loop forever
     led.value(1)  #turn on led
     time.sleep(1) #sleep or delay 1 sec
 
     led.value(0)  #turn off led
     time.sleep(1) #sleep 1 sec