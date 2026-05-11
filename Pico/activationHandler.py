# activationHandler.py

from machine import Pin

def activeSetup(pins):
    active_pins = []

    for x in pins:
        act = Pin(pins[x], Pin.OUT)
        act.low()
        active_pins.append(act)
    
    return active_pins