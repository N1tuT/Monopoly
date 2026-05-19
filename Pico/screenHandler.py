# screenHandler.py

from library.ssd1306 import SSD1306_I2C # type: ignore
from machine import Pin, SoftI2C
import time
import random

global PCA
global OLED
global screen_width
global screen_height
global screens

current_channel = None
PCA = 0x70
OLED = 0x3C
screen_width = 128
screen_height = 64
screens = []

# -----------------------------
# I2C / PCA / OLED setup
# -----------------------------

def screenSetup(sda, scl, frequency, num):
    global i2c
    i2c = SoftI2C(sda=Pin(sda), scl=Pin(scl), freq=frequency)
    setOleds(num)
    clearAllScreens()

def select_channel(ch):
    global current_channel

    if ch < 0 or ch > 7:
        raise ValueError("PCA channel must be between 0 and 7")

    if current_channel != ch:
        try:
            i2c.writeto(PCA, bytes([1 << ch]))
            current_channel = ch
            time.sleep_ms(2)
        except OSError as e:
            print("Failed to select PCA channel", ch)
            print("I2C scan:", [hex(x) for x in i2c.scan()])
            raise e

def setOleds(num):
    for ch in range(num):
        select_channel(ch)
        
        oled = SSD1306_I2C(
            screen_width, 
            screen_height, 
            i2c, 
            addr=OLED
            )
        screens.append(oled)


# -----------------------------
# Screen helpers
# -----------------------------
def writeText(ch, text, x=0, y=0):
    select_channel(ch)
    clearScreen(ch)
    screens[ch].text(text, x, y)
    screens[ch].show()

def clearAllScreens():
    for ch in range(len(screens)):
        select_channel(ch)
        screens[ch].fill(0)
        screens[ch].show()

def clearScreen(ch):
    select_channel(ch)
    screens[ch].fill(0)
    screens[ch].show()

# -----------------------------
# Drawing helpers
# -----------------------------
def draw_filled_circle(oled, cx, cy, r, colour):
    for y in range(-r, r + 1):
        for x in range(-r, r + 1):
            if x * x + y * y <= r * r:
                oled.pixel(cx + x, cy + y, colour)


def draw_rounded_rect(oled, x, y, w, h, r, colour):
    oled.fill_rect(x + r, y, w - 2 * r, h, colour)
    oled.fill_rect(x, y + r, w, h - 2 * r, colour)

    draw_filled_circle(oled, x + r, y + r, r, colour)
    draw_filled_circle(oled, x + w - r - 1, y + r, r, colour)
    draw_filled_circle(oled, x + r, y + h - r - 1, r, colour)
    draw_filled_circle(oled, x + w - r - 1, y + h - r - 1, r, colour)

DIE_SIZE = 50
DIE_RADIUS = 7
DIE_Y = 7

LEFT_DIE_X = 9
RIGHT_DIE_X = 69

PIP_RADIUS = 4


def draw_die(oled, x, y, value):
    # Draw rounded white die body
    draw_rounded_rect(oled, x, y, DIE_SIZE, DIE_SIZE, DIE_RADIUS, 1)

    # Pip positions
    left = x + 13
    centre = x + DIE_SIZE // 2
    right = x + DIE_SIZE - 13

    top = y + 13
    middle = y + DIE_SIZE // 2
    bottom = y + DIE_SIZE - 13

    # Centre pip for 1, 3, and 5
    if value == 1 or value == 3 or value == 5:
        draw_filled_circle(oled, centre, middle, PIP_RADIUS, 0)

    # Diagonal pips for 2, 3, 4, 5, and 6
    if value >= 2:
        draw_filled_circle(oled, left, top, PIP_RADIUS, 0)
        draw_filled_circle(oled, right, bottom, PIP_RADIUS, 0)

    # Other diagonal pips for 4, 5, and 6
    if value >= 4:
        draw_filled_circle(oled, right, top, PIP_RADIUS, 0)
        draw_filled_circle(oled, left, bottom, PIP_RADIUS, 0)

    # Middle side pips for 6
    if value == 6:
        draw_filled_circle(oled, left, middle, PIP_RADIUS, 0)
        draw_filled_circle(oled, right, middle, PIP_RADIUS, 0)


def draw_two_dice(ch, left_value, right_value):
    select_channel(ch)
    oled = screens[ch]

    oled.fill(0)

    draw_die(oled, LEFT_DIE_X, DIE_Y, left_value)
    draw_die(oled, RIGHT_DIE_X, DIE_Y, right_value)

    oled.show()

# -----------------------------
# Dice rolling animation
# -----------------------------

def roll_dice(ch, frames=16):
    for _ in range(frames):
        draw_two_dice(
            ch,
            random.randint(1, 6),
            random.randint(1, 6)
        )