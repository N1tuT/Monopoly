// ---------------------------------------------------
// File:       players.h
// Project:    Monopoly
// Author:     N1tuT
// Version:    v1.0
// ---------------------------------------------------

#pragma once
#include "config.h"

struct Player {
    uint8_t pos;
    uint32_t money;
    bool sick;
    uint8_t sickCount;
    bool firstLap;
};

extern Player players[PLAYER_COUNT];
extern uint8_t currentPlayer;