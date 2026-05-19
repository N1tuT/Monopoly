from machine import Pin, SoftI2C
import time
import random
from ssd1306 import SSD1306_I2C


# -----------------------------
# I2C / PCA / OLED setup
# -----------------------------

i2c = SoftI2C(sda=Pin(14), scl=Pin(15), freq=400000)

PCA = 0x70
OLED = 0x3C

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

current_channel = None


def select_channel(ch):
    global current_channel

    if current_channel != ch:
        i2c.writeto(PCA, bytes([1 << ch]))
        current_channel = ch
        time.sleep_ms(2)


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


# -----------------------------
# Dice settings
# -----------------------------

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


def draw_two_dice(oled, left_value, right_value):
    oled.fill(0)
    draw_die(oled, LEFT_DIE_X, DIE_Y, left_value)
    draw_die(oled, RIGHT_DIE_X, DIE_Y, right_value)
    oled.show()


# -----------------------------
# Create all 4 screens
# -----------------------------

screens = []

for ch in range(4):
    select_channel(ch)
    print("Channel", ch, [hex(x) for x in i2c.scan()])

    oled = SSD1306_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, i2c, addr=OLED)
    screens.append(oled)

    oled.fill(0)
    oled.text("READY", 40, 28)
    oled.show()


# -----------------------------
# Dice rolling animation
# -----------------------------

def roll_screen(ch, oled, final_left=None, final_right=None):
    """
    Animate one screen rolling two dice.
    If final_left/final_right are not provided, random final values are chosen.
    """

    if final_left is None:
        final_left = random.randint(1, 6)

    if final_right is None:
        final_right = random.randint(1, 6)

    # Fast rolling frames
    for i in range(12):
        select_channel(ch)

        left = random.randint(1, 6)
        right = random.randint(1, 6)

        draw_two_dice(oled, left, right)

        # Gradually slow down
        time.sleep(0.03 + i * 0.015)

    # Flash the final result once
    select_channel(ch)
    oled.fill(0)
    oled.show()
    time.sleep(0.08)

    select_channel(ch)
    draw_two_dice(oled, final_left, final_right)

    return final_left, final_right


def roll_all_screens_fast_flip():
    final_values = []

    for ch in range(4):
        final_values.append((random.randint(1, 6), random.randint(1, 6)))

    for frame in range(24):
        for ch, oled in enumerate(screens):
            select_channel(ch)
            draw_two_dice(
                oled,
                random.randint(1, 6),
                random.randint(1, 6)
            )

        if frame < 18:
            time.sleep_ms(0)
        else:
            time.sleep_ms(5 + (frame - 18) * 6)

    for ch, oled in enumerate(screens):
        select_channel(ch)
        draw_two_dice(oled, final_values[ch][0], final_values[ch][1])

    return final_values


def roll_one_screen_fast(ch):
    """
    Fast rolling animation on one screen only.
    ch = PCA channel number, 0 to 3.
    """

    oled = screens[ch]

    final_left = random.randint(1, 6)
    final_right = random.randint(1, 6)

    # Fast flipping frames
    for _ in range(25):
        select_channel(ch)

        draw_two_dice(
            oled,
            random.randint(1, 6),
            random.randint(1, 6)
        )

        # 0 means flip as fast as the display can update
        time.sleep_ms(0)

    # Final result
    select_channel(ch)
    draw_two_dice(oled, final_left, final_right)

    return final_left, final_right

# -----------------------------
# Main loop
# -----------------------------

while True:
    result = roll_one_screen_fast(3)  # only screen/channel 0
    print("Screen 0 result:", result)
    time.sleep(1)

