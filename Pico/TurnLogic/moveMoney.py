# moveMoney.py
# Functions for moving money between players and Student Finance

from Dictionaries.boardPosDict import board
from Dictionaries.boardPosDict import findTileIndex
from Dictionaries.playerDict import players

def payPlayer(payer, payee, amount):
    """
    Move money from one player to another.
    """

    players[payer]["money"] -= amount
    players[payee]["money"] += amount
    return

def paySFE(payer, amount):
    """
    Move money from a player into the Student Finance.
    """
    
    pos = findTileIndex("Student Finance")
    board[pos]["price"] += amount
    players[payer]["money"] -= amount

def receiveSFE(payee):
    """
    Give the Student Finance pot to a player, then reset the pot.
    """

    pos = findTileIndex("Student Finance")
    amount = board[pos]["price"]
    board[pos]["price"] = 0
    players[payee]["money"] += amount

def payBank(payer, amount):
    """
    Take money from a player and pay the bank.
    """

    players[payer]["money"] -= amount

def bankPays(payee, amount):
    """
    Take money from the bank and pay player.
    """
    
    players[payee]["money"] += amount