# buttonChecker.py
# Functions to read button inputs

from machine import Pin
from time import sleep

def buttonSetup (pins):
    """
    Set up three GPIO pins as input

    e.g.
    buttonSetup(12, 24, 27)
    """

    return [
        Pin(pins[0], Pin.IN, Pin.PULL_DOWN),
        Pin(pins[1], Pin.IN, Pin.PULL_DOWN),
        Pin(pins[2], Pin.IN, Pin.PULL_DOWN)
    ]

def buttonRead (pins):
    """
    Read three pin inputs and return value of pin that is high

    Only one pin should be high at a time
    """
    values = [
        pins[0].value(),
        pins[1].value(),
        pins[2].value()
    ]
    x = values.count(1)

    if x > 1: return None
    
    pin = values.index(1) if 1 in values else None

    return None if pin is None else pin+1

def waitForButton(pins):
    """
    Pause game until one button is pressed

    Returns;
    1, 2 or 3 depending on which button is pressed
    """
    
    button = None

    # wait until button is pressed
    while button is None:
        button = buttonRead(pins)
        sleep(0.05)

    # wait until button is released
    while buttonRead(pins) is not None:
        sleep(0.05)

    return button