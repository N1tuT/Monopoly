# boardPosDict.py
# Stores board position data for the Monopoly board

PLACE_NAMES = [
    "Go", "Cambridge", "Communal Melons", "Oxford", "Hangover Tax",
    "King's Cross St", "Harvard", "Chonce", "Yale", "MIT",
    "Get Well Soon", "Nottingham", "Electric", "Birmingham", "Warwick",
    "Euston St", "Durham", "Chonce", "Edinburgh", "Glasgow",
    "Student Finance", "Southhampton", "Communal Melons", "Brighton", "Sussex",
    "Paddington St", "UCL", "KCL", "Water", "Imperial",
    "Freshers' Flu", "Cardiff", "Gloucestershire", "Chonce", "Bristol",
    "Victoria St", "Gas", "Queen Mary", "Groceries Bill", "Bath"
]

PURCHASE_PRICE = [
    0, 60, 0, 60, 200, 200, 100, 0, 100, 120,
    0, 140, 150, 140, 160, 200, 180, 0, 180, 200,
    0, 220, 0, 220, 240, 200, 260, 260, 150, 280,
    0, 300, 300, 0, 320, 200, 150, 350, 100, 400
]

RENT_BASE = [
    0, 2, 0, 4, 0, 25, 6, 0, 6, 8,
    0, 10, 0, 10, 12, 25, 14, 0, 14, 16,
    0, 18, 0, 18, 20, 25, 22, 22, 0, 22,
    0, 26, 26, 0, 28, 25, 0, 35, 0, 50
]

RENT_1_HOUSE = [
    0, 10, 0, 20, 0, 25, 30, 0, 30, 40,
    0, 50, 0, 50, 60, 25, 70, 0, 70, 80,
    0, 90, 0, 90, 100, 25, 110, 110, 0, 120,
    0, 130, 130, 0, 150, 25, 0, 175, 0, 200
]

RENT_2_HOUSES = [
    0, 30, 0, 60, 0, 50, 90, 0, 90, 100,
    0, 150, 0, 150, 180, 50, 200, 0, 200, 220,
    0, 250, 0, 250, 300, 50, 330, 330, 0, 360,
    0, 390, 390, 0, 450, 50, 0, 500, 0, 600
]

RENT_3_HOUSES = [
    0, 90, 0, 180, 0, 100, 270, 0, 270, 300,
    0, 450, 0, 450, 500, 100, 550, 0, 550, 600,
    0, 700, 0, 700, 750, 100, 800, 800, 0, 850,
    0, 900, 900, 0, 1000, 100, 0, 1100, 0, 1400
]

RENT_4_HOUSES = [
    0, 160, 0, 320, 0, 200, 400, 0, 400, 450,
    0, 625, 0, 625, 700, 200, 750, 0, 750, 800,
    0, 875, 0, 875, 925, 200, 975, 975, 0, 1025,
    0, 1100, 1100, 0, 1200, 200, 0, 1300, 0, 1500
]

RENT_HOTEL = [
    0, 250, 0, 450, 0, 0, 550, 0, 660, 600,
    0, 750, 0, 750, 900, 0, 950, 0, 950, 1000,
    0, 1050, 0, 1050, 1100, 0, 1150, 1150, 0, 1200,
    0, 1275, 1275, 0, 1400, 0, 0, 1500, 0, 2000
]

MORTGAGE = [
    0, 30, 0, 30, 0, 100, 50, 0, 200, 60,
    0, 70, 0, 70, 80, 0, 90, 0, 90, 100,
    0, 110, 0, 110, 120, 0, 130, 130, 0, 140,
    0, 150, 150, 0, 160, 0, 0, 175, 0, 200
]

TILE_TYPES = [
    "ACTION", "PROPERTY", "ACTION", "PROPERTY", "ACTION",
    "PROPERTY", "PROPERTY", "ACTION", "PROPERTY", "PROPERTY",
    "NONE", "PROPERTY", "PROPERTY", "PROPERTY", "PROPERTY",
    "PROPERTY", "PROPERTY", "ACTION", "PROPERTY", "PROPERTY",
    "ACTION", "PROPERTY", "ACTION", "PROPERTY", "PROPERTY",
    "PROPERTY", "PROPERTY", "PROPERTY", "PROPERTY", "PROPERTY",
    "ACTION", "PROPERTY", "PROPERTY", "ACTION", "PROPERTY",
    "PROPERTY", "PROPERTY", "PROPERTY", "ACTION", "PROPERTY"
]

TILE_GROUPS = [
    "GO", "PURPLE", "CHEST", "PURPLE", "TAX",
    "STATION", "LBLUE", "CHONCE", "LBLUE", "LBLUE",
    "NA", "PINK", "UTILITY", "PINK", "PINK",
    "STATION", "ORANGE", "CHONCE", "ORANGE", "ORANGE",
    "SFE", "RED", "CHEST", "RED", "RED",
    "STATION", "YELLOW", "YELLOW", "UTILITY", "YELLOW",
    "FLU", "GREEN", "GREEN", "CHONCE", "GREEN",
    "STATION", "UTILITY", "BLUE", "TAX", "BLUE"
]


board = {}

for pos in range(40):
    board[pos] = {
        "name": PLACE_NAMES[pos],
        "type": TILE_TYPES[pos],
        "group": TILE_GROUPS[pos],

        "price": PURCHASE_PRICE[pos],
        "rent": {
            0: RENT_BASE[pos],
            1: RENT_1_HOUSE[pos],
            2: RENT_2_HOUSES[pos],
            3: RENT_3_HOUSES[pos],
            4: RENT_4_HOUSES[pos],
            5: RENT_HOTEL[pos]
        },
        "mortgage": MORTGAGE[pos],

        # Mutable game data
        "owner": None,
        "houses": 0,
        "mortgaged": False
    }


def findTileIndex(target):
    """
    Find a tile position by name.

    Returns the board position if found.
    Returns -1 if not found.
    """

    for pos in board:
        if board[pos]["name"] == target:
            return pos

    return "ERROR"