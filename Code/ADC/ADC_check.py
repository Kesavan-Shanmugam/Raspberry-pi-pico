from machine import Pin, ADC
import time
# set up pin 26 as an analog input
pot = ADC(Pin(26))
#constant to covert range to 0 to 3.3
conversion_factor = 3.3/65535

while True:
    #read analog input
    pot_voltage = pot.read_u16()*conversion_factor
    
    print(pot_voltage)
    time.sleep(0.1) 