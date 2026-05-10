// ---------------------------------------------------
// File:       dice.h
// Project:    Monopoly
// Author:     N1tuT
// Version:    v1.0
// ---------------------------------------------------

#pragma once
#include <Arduino.h>

struct DiceResult {
    uint8_t total;
    bool isDouble;
};
DiceResult rollDice();
