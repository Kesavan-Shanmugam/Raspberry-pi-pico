from machine import Pin,PWM
from servo import Servo
from time import sleep

#initialize PWM on GPIO
servo = Servo(Pin(0))

#sweep the servo from 0 to 180 degrees and back
while True:
    for angle in range (0,180,5):
        servo.write(angle)
        sleep(0.1)
    
    for angle in range (180,0,-5):
        servo.write(angle)
        sleep(0.1)
    