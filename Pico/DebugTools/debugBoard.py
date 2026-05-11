# debugBoard.py
# Terminal tool to print board position data

import sys
from pathlib import Path

PICO_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(PICO_DIR))

from Dictionaries.boardPosDict import board


def printBoardPosition(pos):
    """
    Print all stored data for one board position.
    """

    if pos not in board:
        print("ERROR: invalid board position")
        return

    tile = board[pos]

    print("----------------------------")
    print("Board position:", pos)
    print("Name:", tile["name"])
    print("Type:", tile["type"])
    print("Group:", tile["group"])
    print("Price:", tile["price"])
    print("Mortgage:", tile["mortgage"])
    print("Owner:", tile["owner"])
    print("Houses:", tile["houses"])
    print("Mortgaged:", tile["mortgaged"])

    print("Rent:")
    print("  0 houses:", tile["rent"][0])
    print("  1 house:", tile["rent"][1])
    print("  2 houses:", tile["rent"][2])
    print("  3 houses:", tile["rent"][3])
    print("  4 houses:", tile["rent"][4])
    print("  Hotel:", tile["rent"][5])
    print("----------------------------")


if len(sys.argv) < 2:
    print("Usage: python debugBoard.py <board_position>")
else:
    position = int(sys.argv[1])
    printBoardPosition(position)