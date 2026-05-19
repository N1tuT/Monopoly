from machine import Pin
from neopixel import NeoPixel
from time import sleep

LED_PIN = 4       # GPIO pin connected to DIN on the LED strip
NUM_LEDS = 300     # number of LEDs on your strip

strip = NeoPixel(Pin(LED_PIN), NUM_LEDS)

# Set all LEDs to white
for i in range(NUM_LEDS):
    strip[i] = (10, 10, 10)

strip.write()

while True:
    sleep(1)