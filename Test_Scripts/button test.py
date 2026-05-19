from machine import Pin
import time


# -----------------------------
# Output pins: choose active circuit
# -----------------------------

Pin(6, Pin.OUT).value(0)
Pin(7, Pin.OUT).value(0)
Pin(8, Pin.OUT).value(0)
Pin(9, Pin.OUT).value(1)

b1 = Pin(10, Pin.IN, Pin.PULL_DOWN)
b2 = Pin(11, Pin.IN, Pin.PULL_DOWN)
b3 = Pin(12, Pin.IN, Pin.PULL_DOWN)


while 1:
    print(b1.value(), b2.value(), b3.value())
    time.sleep_ms(1)