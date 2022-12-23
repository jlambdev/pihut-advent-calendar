from machine import Pin
import time

#Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

counter = 1 

while counter < 21:
    
    print(counter) 
    
    # Red ON
    red.value(1)
    amber.value(0)
    green.value(0)
    
    time.sleep(0.1)
    
    # Amber ON
    red.value(0)
    amber.value(1)
    green.value(0)
    
    time.sleep(0.1)
    
    # Green ON
    red.value(0)
    amber.value(0)
    green.value(1)
    
    time.sleep(0.1) 
    
    counter += 1

# Turn all lights off
red.value(0)
amber.value(0)
green.value(0)
