from machine import Pin,UART
import time

#Initialize UART2 on pico B, Tx pin is GP4, Rx pin is GP5
UART2 = UART(1, baudrate=9600, tx = Pin(4), rx= Pin(5))

led = Pin("LED", Pin.OUT)

while True:
    if UART2.any():
        
        message = UART2.read().decode() #read the value store in variable
        print(message)                  #print the message
        
        if(message == 'ON'):            
            led.value(1)
            
        elif(messge == 'OFF'):
            led.value(0)
    