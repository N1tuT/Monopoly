# posAction.py

from Dictionaries.boardPosDict import board
from Dictionaries.playerDict import players
import moveMoney


def handlePos(player):
    """
    Handle the board position that a player has landed on.

    Checks the tile type and sends the player to the correct handler.
    """

    global pos
    pos = players[player]["pos"]
    tile = board[pos]

    if tile["type"] == "ACTION":
        return handleAction(player)
    elif tile["type"] == "PROPERTY":
        return handleProp(player)
    elif tile["type"] == "NONE":
        return None
    else:
        return "ERROR"
    

## PROPERTY HANDLING ##
def handleProp(player):
    """
    Handle a property tile.

    If unowned, return FOR_SALE.
    If owned by the current player, return OWN.
    If owned by another player, charge rent.
    """

    tile = board[pos]
    owner = tile["owner"]

    if owner is None:
        return "FOR_SALE"
    elif owner == player:
        return "OWN"
    
    return chargeRent(player)

def chargeRent(player):
    """
    Charge rent from the current player to the property owner.
    """

    tile = board[pos]
    owner = tile["owner"]
    houses = tile["houses"]
    rent = tile["rent"][houses]

    moveMoney.payPlayer(player, owner, rent)
    return "RENT_PAID"

def buyProp(player):
    """
    Buy the property at the given board position.
    """

    price = board[pos]["price"]
    moveMoney.payBank(player, price)
    board[pos]["owner"] = player

## ACTION HANDLING ##
def handleAction(player):
    """
    Handle an action tile.
    """
    group = board[pos]["group"]

    if group == "TAX":
        tax_charge = board[pos]["price"]
        moveMoney.paySFE(player, tax_charge)
        return "Tax paid"

    if group == "CHEST":
        return "COMMUNAL_MELONS"

    if group == "CHONCE":
        return "CHONCE"

    if group == "GO":
        moveMoney.bankPays(player, 200)
        return "Go passed"

    if group == "SFE":
        moveMoney.receiveSFE(player)
        return "Received student finance"

    if group == "FLU":
        return "FRESHERS_FLU"

    return "UNKNOWN_ACTION"