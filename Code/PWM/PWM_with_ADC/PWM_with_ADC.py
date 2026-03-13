from machine import Pin, PWM, ADC
import time

ADC_pin = ADC(Pin(26))
PWM_pin = PWM(Pin(16))

PWM_pin.freq(1000)   # 1kHz PWM

while True:
    Pot_value = ADC_pin.read_u16()
    
    PWM_pin.duty_u16(Pot_value)
    
    print(Pot_value)
    time.sleep(0.05)
