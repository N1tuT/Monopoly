# cardLogic.py

from Dictionaries.boardPosDict import findTileIndex
from Dictionaries.playerDict import players
from ledHandler import movePlayer, movePlayerTo
from TurnLogic import moveMoney as money
import random

def pickCard(card_set):
    
    """
    Pick a random card from the given card set and apply its action.
    """

    pull = random.randint(1,16)
    card = card_set[pull]

    return card


# called when card["action"] is "MOVE"
def handleMoveCard(card, leds, player):
    result = card["result"]
    old_pos = players[player]["pos"]

    if card["action"] == "MOVE":
        if isinstance(result, str):
            destination = findTileIndex(result)
            movePlayerTo(leds, player, destination)

            if destination < old_pos:
                money.bankPays(player, 200)

        elif isinstance(result, int):
            destination = (old_pos + result) % 40
            movePlayer(leds, player, result)

            if result > 0 and destination < old_pos:
                money.bankPays(player, 200)
    
    elif card["action"] == "MOVE_NEAREST":
        destination, go_flag = findNearest(old_pos, card["result"])
        movePlayerTo(leds, player, destination)
        money.bankPays(player, 200) if go_flag else None


def findNearest(pos, target):
    STATION_POSITIONS = [5, 15, 25, 35]
    UTILITY_POSITIONS = [12, 28]
    BOARD_SIZE = 40

    positions = STATION_POSITIONS if target == "STATION" else UTILITY_POSITIONS
    
    distance = []
    for x in range(len(positions)):
        forward_distance = (positions[x] - pos) % 40
        backward_distance = (pos - positions[x]) % 40

        ideal_distance = min(forward_distance, backward_distance)

        distance.append(ideal_distance)
    
    target_distance = min(distance)

    target_index = distance.index(target_distance)
    target_pos = positions[target_index]

    
    spaces = abs(pos - target_pos)
    go = spaces > (BOARD_SIZE - positions[-1])

    return target_pos, go





