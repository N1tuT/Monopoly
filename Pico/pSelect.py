# pSelect.py
# Functions to select number of players at start of game

from machine import Pin

def pSelectSetup (pins):
    """
    Set up three GPIO pins as inputs

    e.g.
    pSelectSetup(12, 13, 14)
    """

    Pin(pins[0], Pin.IN, Pin.PULL_DOWN).value()
    Pin(pins[1], Pin.IN, Pin.PULL_DOWN).value()
    Pin(pins[2], Pin.IN, Pin.PULL_DOWN).value()

def pSelectRead (pins):
    """
    Read three pin inputs and return value of pin that is high

    Only one pin should be high at a time
    """

    x = pins.count(1)

    if x > 1: return "ERROR"
    
    pin = pins.index(1) if 1 in pins else None

    return None if pin is None else pin+2

