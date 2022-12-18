from machine import Pin

# Switch the on-board LED on and off
# Change value to 1 for on, 0 for off
onboardLED = Pin(25, Pin.OUT)
onboardLED.value(0)