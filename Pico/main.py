# main.py

import pSelect
import buttonChecker
import DebugTools.gameLogger as logger
import ErrorTools.errorHandler as eHandler
import ledHandler as lHandler
import diceRoll
import activationHandler as aHandler
import TurnLogic.posAction as posAct


# -------------------------
# Pin allocation
# -------------------------

ERROR_LED_PIN = 19
BUTTON_PINS = [9, 10, 11]
PLAYER_SELECT_PINS = [12, 13, 14]
POS_LED = 20
PROP_LED = 21

POS_LED_NUM = 130
PROP_LED_NUM = 200
JAIL = 20

SEED_PIN = 26
ACTIVE_PINS = [2, 3, 4, 5]

# -------------------------
# Setup
# -------------------------

eHandler.errorPinSetup(ERROR_LED_PIN)

buttons = buttonChecker.buttonSetup(BUTTON_PINS)
pSelect.pSelectSetup(PLAYER_SELECT_PINS)

pos_LED = lHandler.ledSetup(POS_LED, POS_LED_NUM)
prop_LED = lHandler.ledSetup(PROP_LED, PROP_LED_NUM)
lHandler.jail = JAIL

diceRoll.seedFromAnalog(SEED_PIN)

active_pins = aHandler.activeSetup(ACTIVE_PINS)

# -------------------------
# Pre-game logic
# -------------------------

# turn off all LEDs, then do running animation
lHandler.clearLeds(pos_LED)
lHandler.clearLeds(prop_LED)
lHandler.ledRun(pos_LED, 1)
lHandler.ledRun(prop_LED, 2)

# wait for button to be pressed to start game
buttonChecker.waitForButton(buttons)

# read player number selection after start button
player_num = pSelect.pSelectRead(PLAYER_SELECT_PINS)

if player_num == "ERROR" or player_num is None:
    eHandler.errorFlag("Player number selection wiring broken")

else:
    logger.startGameTimer()

    # -------------------------
    # Main game logic
    # -------------------------
    
    # move all players to start
    for x in range(1, player_num+1):
        lHandler.movePlayer(pos_LED, x, 0)

    while True:
        # Loop through each active player in order.
        for player in range(1, player_num + 1):

            # Turn on the current player's active indicator.
            active_pin = active_pins[player - 1]
            active_pin.high()

            # Count how many doubles the player rolls during this turn.
            dcount = 0

            # This loop only repeats if the player rolls a double.
            while True:

                # Wait for the dice-roll button.
                if buttonChecker.waitForButton(buttons) == 2:
                    continue

                # Roll the dice.
                d1, d2, double = diceRoll.rollDice()

                # If the player rolled a double, increase their doubles count.
                if double:
                    dcount += 1

                    # Three doubles sends the player to jail.
                    if dcount >= 3:
                        lHandler.arrestPlayer(pos_LED, player)
                        break

                # Move the player by the dice total.
                lHandler.movePlayer(pos_LED, player, d1 + d2)

                action = posAct.handlePos(player)
                if action == "FRESHERS_FLU":
                    lHandler.arrestPlayer(pos_LED, player)

                if action == "FOR_SALE":
                    purchase = buttonChecker.waitForButton(buttons)
                    if purchase == 3:
                        posAct.buyProp(player)
                    elif purchase == 2:
                        continue
                
                if action == "UNKNOWN_ACTION":
                    eHandler.errorFlag("Unknown action detected")

                # If the player did not roll a double, their turn ends.
                if not double:
                    if buttonChecker.waitForButton(buttons) == 2:
                        break

            # Turn off the current player's active indicator.
            active_pin.low()




# -------------------------
# End game cleanup
# -------------------------

logger.stopGameTimer()