from machine import Pin,UART
import time

#Initialize UART1 on pico A, Tx pin is GP4, Rx pin is GP5
UART1 = UART(1, baudrate=9600, tx = Pin(4), rx= Pin(5))

while True:
    UART1.write('ON/n') #send 'ON' message to pico B
    time.sleep(2)
    
    UART1.write('OFF') #send 'OFF' message to pico B
    time.sleep(2)