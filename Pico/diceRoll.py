# diceRoll.py

from machine import ADC
from time import ticks_ms
import random

def seedFromAnalog(pin):
    """
    Seed the random number generator using an analogue pin.

    Pico ADC pins:
    GP26 = ADC0
    GP27 = ADC1
    GP28 = ADC2
    """

    adc = ADC(pin)
    seed = ticks_ms()

    for _ in range(32):
        seed ^= adc.read_u16()

    random.seed(seed)

def rollDice():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    
    if d1 == d2:
        double = True
    else:
        double = False
    
    return d1, d2, False

