# activationHandler.py

from machine import Pin
global active_pins
active_pins = []

def activeSetup(pins):
    for x in range(len(pins)):
        act = Pin(pins[x], Pin.OUT)
        act.low()
        active_pins.append(act)
    
    return active_pins

def activate(player):
    active_pins[player].value(1)

def deactivate(player):
    active_pins[player].value(0)