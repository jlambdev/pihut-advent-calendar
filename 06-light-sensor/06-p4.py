# Imports
from machine import ADC, Pin, PWM
import time

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

lightsensor = ADC(Pin(26))
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

buzzer.freq(523)

def warningtone():
    buzzer.duty_u16(32768)
    time.sleep(0.1)
    buzzer.duty_u16(0)
    time.sleep(0.4)

while True: 
    light = lightsensor.read_u16()
    lightpercent = round(light/65535*100,1)
    print(str(lightpercent) +"%")
    
    time.sleep(1)

    if lightpercent <= 30: # If percentage is less than or equal to 30
        
        red.value(1) # Red LED on
        amber.value(0)
        green.value(0)
        warningtone()

    elif 30 < lightpercent < 60: # If percentage is between 30 and 60
        
        red.value(0)
        amber.value(1) # Amber LED on
        green.value(0)

    elif lightpercent >= 60: # If percentage is greater than or equal to 60
        
        red.value(0)
        amber.value(0)
        green.value(1) # Green LED on
