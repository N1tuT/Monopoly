// ---------------------------------------------------
// File:       players.cpp
// Project:    Monopoly
// Author:     N1tuT
// Version:    v1.0
// ---------------------------------------------------

#include "players.h"

Player players[PLAYER_COUNT] = {
    {0, 1500, false, 0, true},
    {0, 1500, false, 0, true},
    {0, 1500, false, 0, true},  
    {0, 1500, false, 0, true},
};

uint8_t currentPlayer = 0;