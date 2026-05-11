# errorHandler.py
# Functions to define and activate error LED indicator

from machine import Pin
from DebugTools.gameLogger import writeErrorLog

def errorPinSetup(error_pin):
    """
    Setup GPIO output pin for error LED.
    """
    
    global error_led
    error_led = Pin(error_pin, Pin.OUT)
    return error_led


def errorFlag(error_msg):
    """
    Turn on error LED and write error to log.
    """

    error_led.value(1)
    writeErrorLog(error_msg)