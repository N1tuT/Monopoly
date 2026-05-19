# cardDict.py
# Stores Communal Melons and Chonce card data

from machine import Pin

communal_melons_custom = {
    1: {
        "text": "You're off to uni\nMove to Paddington",
        "action": "MOVE",
        "result": "Paddington St"
    },
    2: {
        "text": "You got food poisoning.\nBuy diarrhoea meds",
        "action": "PAY",
        "amount": 50,
        "result": None
    },
    3: {
        "text": "Freshers flu isn't for you\nCURES FRESHERS FLU\nKeep until needed or sell",
        "action": "GET_OUT_OF_JAIL",
        "result": None
    },
    4: {
        "text": "Someone buys you drinks",
        "action": "GAIN",
        "amount": 25,
        "result": None
    },
    5: {
        "text": "Well done! You won a drinking competition",
        "action": "GAIN",
        "amount": 100,
        "result": None
    },
    6: {
        "text": "Your friend got paid\nDrinks on them!",
        "action": "GAIN",
        "amount": 50,
        "result": None
    },
    7: {
        "text": "It's your birthday",
        "action": "GROUP_PAY",
        "amount": 10,
        "result": None
    },
    8: {
        "text": "You somehow get a refund from teacher trikes",
        "action": "GAIN",
        "amount": 20,
        "result": None
    },
    9: {
        "text": "Your parents found your drugs, you need to restock",
        "action": "PAY",
        "amount": 50,
        "result": None
    },
    10: {
        "text": "Boo! You gave everyone food poisoning",
        "action": "GROUP_PAY",
        "amount": 50,
        "result": None
    },
    11: {
        "text": "You have a hangover and need to buy painkillers",
        "action": "PAY",
        "amount": 50,
        "result": None
    },
    12: {
        "text": "There was a noise complaint for your party",
        "action": "PAY",
        "amount": 15,
        "result": None
    },
    13: {
        "text": "Juan makes you go climbing",
        "action": "PAY",
        "amount": 100,
        "result": None
    },
    14: {
        "text": "You're a party animal\nYou got Freshers' Flu",
        "action": "JAIL",
        "result": None
    },
    15: {
        "text": "Move forwards 3 spaces",
        "action": "MOVE",
        "result": 3
    },
    16: {
    "text": "Your flatmate forgot to pay you back\nCollect £50",
    "action": "GAIN",
    "amount": 50,
    "result": None
}
}

chonce_custom = {
    1: {
        "text": "It's nothing some meds can't fix\nCURES FRESHERS FLU\nKeep until needed or sell",
        "action": "GET_OUT_OF_JAIL",
        "result": None
    },
    2: {
        "text": "You won a cycling competition",
        "action": "GAIN",
        "amount": 100,
        "result": None
    },
    3: {
        "text": "You got a job offer",
        "action": "GAIN",
        "amount": 50,
        "result": None
    },
    4: {
        "text": "You won a chess competition",
        "action": "GAIN",
        "amount": 100,
        "result": None
    },
    5: {
        "text": "You're clean!\nYour STD test came back clean",
        "action": "GAIN",
        "amount": 20,
        "result": None
    },
    6: {
        "text": "You got full marks on a test",
        "action": "GAIN",
        "amount": 10,
        "result": None
    },
    7: {
        "text": "You made new friends",
        "action": "GAIN",
        "amount": 25,
        "result": None
    },
    8: {
        "text": "Your date buys you dinner",
        "action": "GAIN",
        "amount": 50,
        "result": None
    },
    9: {
        "text": "You get your bursary",
        "action": "BURSARY",
        "amount": 50,
        "rounds": 3,
        "result": "gain extra when passing Go for next 3 rounds"
    },
    10: {
        "text": "Pay fine or take Chonce",
        "action": "PAY_OR_CHONCE",
        "amount": 10,
        "result": None
    },
    11: {
        "text": "Drunk driving fine",
        "action": "PAY",
        "amount": 15,
        "result": None
    },
    12: {
        "text": "You have a one-night stand.\nBuy the morning after pill",
        "action": "PAY",
        "amount": 50,
        "result": None
    },
    13: {
        "text": "Make general repairs",
        "action": "REPAIRS",
        "amount_per_house": 25,
        "amount_per_hotel": 100,
        "result": None
    },
    14: {
        "text": "Move forwards 2 spaces",
        "action": "MOVE",
        "result": 2
    },
    15: {
        "text": "Advance to Go",
        "action": "MOVE",
        "result": "Go"
    },
    16: {
        "text": "You kissed one too many people at freshers\nYOU GOT FRESHERS' FLU",
        "action": "JAIL",
        "result": None
    }
}

# -------------------------
# London Monopoly cards
# -------------------------

london_community_chest = {
    1: {
        "text": "Advance to Go\nCollect £200",
        "action": "MOVE",
        "result": "Go",
        "amount": 200
    },
    2: {
        "text": "Bank error in your favour\nCollect £200",
        "action": "GAIN",
        "amount": 200,
        "result": None
    },
    3: {
        "text": "Doctor's fee\nPay £50",
        "action": "PAY",
        "amount": 50,
        "result": None
    },
    4: {
        "text": "From sale of stock you get £50",
        "action": "GAIN",
        "amount": 50,
        "result": None
    },
    5: {
        "text": "Freshers' flu cure",
        "action": "GET_OUT_OF_JAIL",
        "result": None
    },
    6: {
        "text": "Go to Quarantine\nDo not pass Go, do not collect £200",
        "action": "JAIL",
        "result": None
    },
    7: {
        "text": "Holiday fund matures\nReceive £100",
        "action": "GAIN",
        "amount": 100,
        "result": None
    },
    8: {
        "text": "Income tax refund\nCollect £20",
        "action": "GAIN",
        "amount": 20,
        "result": None
    },
    9: {
        "text": "It is your birthday\nCollect £10 from every player",
        "action": "GROUP_GAIN",
        "amount": 10,
        "result": None
    },
    10: {
        "text": "Life insurance matures\nCollect £100",
        "action": "GAIN",
        "amount": 100,
        "result": None
    },
    11: {
        "text": "Pay hospital fees of £100",
        "action": "PAY",
        "amount": 100,
        "result": None
    },
    12: {
        "text": "Pay school fees of £50",
        "action": "PAY",
        "amount": 50,
        "result": None
    },
    13: {
        "text": "Receive £25 consultancy fee",
        "action": "GAIN",
        "amount": 25,
        "result": None
    },
    14: {
        "text": "You are assessed for street repairs\n£40 per house\n£115 per hotel",
        "action": "REPAIRS",
        "amount_per_house": 40,
        "amount_per_hotel": 115,
        "result": None
    },
    15: {
        "text": "You have won second prize in a beauty contest\nCollect £10",
        "action": "GAIN",
        "amount": 10,
        "result": None
    },
    16: {
        "text": "You inherit £100",
        "action": "GAIN",
        "amount": 100,
        "result": None
    }
}

london_chance = {
    1: {
        "text": "Advance to Go\nCollect £200",
        "action": "MOVE",
        "result": "Go",
        "amount": 200
    },
    2: {
        "text": "Advance to Sussex\nIf you pass Go, collect £200",
        "action": "MOVE",
        "result": "Sussex",
        "amount": 0
    },
    3: {
        "text": "Advance to Bath",
        "action": "MOVE",
        "result": "Bath"
    },
    4: {
        "text": "Advance to Nottingham\nIf you pass Go, collect £200",
        "action": "MOVE",
        "result": "Nottingham",
        "amount": 0
    },
    5: {
        "text": "Advance to the nearest Station\nIf unowned, you may buy it from the Bank. If owned, pay owner twice the normal rent",
        "action": "MOVE_NEAREST",
        "result": "STATION",
        "rent_multiplier": 2
    },
    6: {
        "text": "Advance to the nearest Station\nIf unowned, you may buy it from the Bank. If owned, pay owner twice the normal rent",
        "action": "MOVE_NEAREST",
        "result": "STATION",
        "rent_multiplier": 2
    },
    7: {
        "text": "Advance token to nearest Utility\nIf unowned, you may buy it from the Bank. If owned, throw dice and pay owner ten times the amount thrown",
        "action": "MOVE_NEAREST",
        "result": "UTILITY",
        "rent_multiplier": 10
    },
    8: {
        "text": "Bank pays you dividend of £50",
        "action": "GAIN",
        "amount": 50,
        "result": None
    },
    9: {
        "text": "Get Out of Jail Free",
        "action": "GET_OUT_OF_JAIL",
        "result": None
    },
    10: {
        "text": "Go Back 3 Spaces",
        "action": "MOVE",
        "result": -3
    },
    11: {
        "text": "Go to Jail\nGo directly to Jail, do not pass Go, do not collect £200",
        "action": "JAIL",
        "result": None
    },
    12: {
        "text": "Make general repairs on all your property\nFor each house pay £25\nFor each hotel pay £100",
        "action": "REPAIRS",
        "amount_per_house": 25,
        "amount_per_hotel": 100,
        "result": None
    },
    13: {
        "text": "Speeding fine £15",
        "action": "PAY",
        "amount": 15,
        "result": None
    },
    14: {
        "text": "Take a trip to King's Cross Station\nIf you pass Go, collect £200",
        "action": "MOVE",
        "result": "King's Cross St",
        "amount": 200
    },
    15: {
        "text": "You have been elected Chairman of the Board\nPay each player £50",
        "action": "GROUP_PAY",
        "amount": 50,
        "result": None
    },
    16: {
        "text": "Your building loan matures\nCollect £150",
        "action": "GAIN",
        "amount": 150,
        "result": None
    }
}

def cardSetSetup(pin):
    """
    Set up the card set selector pin.

    If the pin reads 0, use custom cards.
    If the pin reads 1, use London cards.
    """

    return Pin(pin, Pin.IN, Pin.PULL_DOWN)

def selectCardSet(card_pin):
    """
    Select card dictionaries based on the card selector pin.

    Returns:
    communal_melons, chonce
    """

    if card_pin.value() == 1:
        return london_community_chest, london_chance

    return communal_melons_custom, chonce_custom

