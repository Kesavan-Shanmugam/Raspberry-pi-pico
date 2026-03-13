from machine import Pin,UART
import time

#Initialize UART1 on pico , Tx pin is GP4, Rx pin is GP5
UART1 = UART(1, baudrate=9600, tx = Pin(4), rx= Pin(5))

led = Pin(16, Pin.OUT)

while True:
    
    UART1.write('ON') #send 'ON' message to pico 
    time.sleep(1)
    
    if UART1.any():
        
        message =UART1.read().decode()
        print(message)
        
        if(message == 'ON'):
            led.value(1)
            
    UART1.write('OFF') #send 'OFF' message to pico  
    time.sleep(1)

    if UART1.any():
        
        message =UART1.read().decode()
        print(message)
        
        if(message == 'OFF'):
            led.value(0)