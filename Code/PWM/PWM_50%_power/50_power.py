from machine import Pin,PWM
import time

PWM_Pin = PWM(Pin(16))

MAX= 65535

PWM_Pin.freq(1000)

while True:
    PWM_value = int(0.5 * MAX)
    
    PWM_Pin.duty_u16(PWM_value)