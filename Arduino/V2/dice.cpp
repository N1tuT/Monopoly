// ---------------------------------------------------
// File:       dice.cpp
// Project:    Monopoly
// Author:     N1tuT
// Version:    v1.0
// ---------------------------------------------------

#include "dice.h"

DiceResult rollDice() {
    DiceResult d;

    uint8_t die1 = random(1, 7);
    uint8_t die2 = random(1, 7);

    d.total = die1 + die2;
    d.isDouble = (die1 == die2);

    return d;
};