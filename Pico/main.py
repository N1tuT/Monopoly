# main.py

import time

import diceRoll
import buttonChecker

import ledHandler as lHandler
import activationHandler as aHandler
import screenHandler as sHandler
import segHandler as s7Handler


# -------------------------
# Pin allocation
# -------------------------

ERROR_LED_PIN = 5

BUTTON_PINS = [10, 11, 12]
PLAYER_SELECT_PINS = [2, 3, 4]

POS_LED_PIN = 0
PROP_LED_PIN = 1

POS_LED_NUM = 12        # eventually 160
PROP_LED_NUM = 12       # eventually 76

JAIL_POS = 20
CARD_SELECT_PIN = 6

SEED_PIN = 28
ACTIVE_PINS = [6, 7, 8, 9]

SCREEN_SDA = 14
SCREEN_SCL = 15
SCREEN_FREQ = 500000

SEG_CLK = 16
SEG_DIO = 17
SEG_BRIGHTNESS = 1


# -------------------------
# Game settings
# -------------------------

PLAYER_COUNT = 3

ROLL_BUTTON = 2
PLAYER_2_BUTTON = 1
QUIT_BUTTON = 3

MAIN_SCREEN = 1
PLAYER_1_SCREEN = 1
PLAYER_2_SCREEN = 2


# -------------------------
# Setup
# -------------------------

buttons = buttonChecker.buttonSetup(BUTTON_PINS)

# pSel = pSelect.pSelectSetup(PLAYER_SELECT_PINS)
pSel = PLAYER_COUNT

pos_LED = lHandler.ledSetup(POS_LED_PIN, POS_LED_NUM)
prop_LED = lHandler.ledSetup(PROP_LED_PIN, PROP_LED_NUM)

lHandler.jail = JAIL_POS

diceRoll.seedFromAnalog(SEED_PIN)

active_pins = aHandler.activeSetup(ACTIVE_PINS)

sHandler.screenSetup(
    SCREEN_SDA,
    SCREEN_SCL,
    SCREEN_FREQ,
    pSel
)

seg7 = s7Handler.setup7Seg(
    SEG_CLK,
    SEG_DIO,
    SEG_BRIGHTNESS
)


# -------------------------
# Pre-game logic
# -------------------------

lHandler.clearLeds(pos_LED)
lHandler.clearLeds(prop_LED)

lHandler.ledRun(pos_LED, 1)
lHandler.ledRun(prop_LED, 2)

aHandler.activate(1)

sHandler.writeText(MAIN_SCREEN, "Press any button")
seg7.show("HOLA")

for player in range(1, 5):
    lHandler.movePlayer(pos_LED, player, 0)

buttonChecker.waitForButton(buttons)

sHandler.clearScreen(MAIN_SCREEN)
sHandler.writeText(MAIN_SCREEN, "Roll Dice")
seg7.show("ROLL")


# -------------------------
# Main game loop
# -------------------------

while True:
    button = buttonChecker.waitForButton(buttons)

    if button == ROLL_BUTTON:
        player = 1
        screen = PLAYER_1_SCREEN

        sHandler.roll_dice(screen)

        d1, d2, double = diceRoll.rollDice()
        total = d1 + d2

        sHandler.draw_two_dice(screen, d1, d2)
        seg7.number(total)

        lHandler.movePlayer(pos_LED, player, 1)

    elif button == PLAYER_2_BUTTON:
        player = 2
        screen = PLAYER_2_SCREEN

        sHandler.roll_dice(screen)

        d1, d2, double = diceRoll.rollDice()
        total = d1 + d2

        sHandler.draw_two_dice(screen, d1, d2)
        seg7.number(total)

        lHandler.movePlayer(pos_LED, player, 1)

    elif button == QUIT_BUTTON:
        sHandler.clearScreen(MAIN_SCREEN)
        sHandler.writeText(MAIN_SCREEN, "Bye")

        seg7.show("BYE")
        time.sleep_ms(700)

        seg7.clear()
        sHandler.clearAllScreens()

        lHandler.clearLeds(pos_LED)
        lHandler.clearLeds(prop_LED)

        break