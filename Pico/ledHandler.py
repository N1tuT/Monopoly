# ledHandler.py
# Functions for controlling game LEDs, player positions, houses, hotels, and jail movement

from machine import Pin
from neopixel import NeoPixel
from time import sleep
from Dictionaries.playerDict import players
from Dictionaries.boardPosDict import board

global led_off
global green
global red
global colours
global jail

brightness = 5

led_off = (0, 0, 0)
green = (0, brightness, 0)
red = (brightness, 0, 0)
colours = [
    (brightness, 0, 0),
    (0, 0, brightness),
    (0, brightness, 0),
    (brightness, brightness, 0),
]
jail = 0    ## this needs updating


def ledSetup (pin, led_count):
    """
    Set up WS2812B LED strip
    
    pin: Pico GPIO pin connected to LED DIN
    led_count: number of LEDs
    """

    led_pin = Pin(pin, Pin.OUT)
    leds = NeoPixel(led_pin, led_count)

    return leds

def clearLeds(leds):
    """
    Turn all LEDs off.
    """

    for i in range(len(leds)):
        leds[i] = led_off

    leds.write()

def ledRun(leds, strip):
    """
    Running LED animation down the strip

    RGBY for strip 1
    Green for strip 2
    """

    clearLeds(leds)
    time = 0.025

    if strip == 1:
        for x in range(len(leds)):
            leds[x] = colours[x % len(colours)]
            leds.write()
            sleep(time)
            leds[x] = led_off
            leds.write()
            sleep(time)
    elif strip == 2:
        for x in range(len(leds)):
            leds[x] = green
            leds.write()
            sleep(time)
            leds[x] = led_off
            leds.write()
            sleep(time)
    else:
        return "ERROR"

def movePlayer(leds, player, move_amount):
    """
    Move one player from old board position to new board position.
    """

    old = players[player]["pos"]
    player_index = player - 1

    move_amount = (move_amount + old) % 40

    old_index = old * 4 + player_index
    new_index = move_amount * 4 + player_index

    leds[old_index] = led_off
    leds[new_index] = players[player]["colour"]

    players[player]["pos"] = move_amount

    leds.write()

def movePlayerTo(leds, player, destination):
    """
    Move one player from old board position to a specified destination
    """

    old = players[player]["pos"]
    player_index = player - 1
    old_index = old * + player_index
    new_index = destination * + player_index

    leds[old_index] = led_off
    leds[new_index] = players[player]["colour"]

    players[player]["pos"] = destination
    leds.write()

def addHouse(leds, pos):
    """
    Add one house to a board position and update the LEDs.

    Each board position uses 4 LEDs.

    If the position has 0-3 houses:
    - Increase the house count by 1
    - Turn the next house LED green

    If the position already has 4 houses:
    - Increase the house count to 5
    - Treat this as a hotel
    - Turn all 4 LEDs for that position red

    If the position already has 5 houses/hotel:
    - Return "ERROR"
    """

    
    if board[pos]["houses"] >= 5:
        return "ERROR"

    board[pos]["houses"] += 1
    house_num = board[pos]["houses"]

    if house_num <= 4:
        house_index = pos * 4 + (house_num - 1)
        leds[house_index] = green
    else:
        for x in range(pos * 4, pos * 4+4):
            leds[x] = red
    
    leds.write()

def arrestPlayer(leds, player):
    """
    Move player to jail
    """

    old = players[player]["pos"]
    player_index = player - 1

    old_index = old * 4 + player_index
    new_index = jail * 4 + player_index

    leds[old_index] = led_off
    leds[new_index] = players[player]["colour"]

    players[player]["pos"] = jail
    players[player]["jail"] = True

    leds.write()


