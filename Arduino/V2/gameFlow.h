// ---------------------------------------------------
// File:       gameFlow.h
// Project:    Monopoly
// Author:     N1tuT
// Version:    v1.0
// ---------------------------------------------------

#pragma once
#include "players.h"

// HELPERS
// ownership helpers
static inline bool isOwnable (uint8_t pos);
static inline bool isUnowned (uint8_t pos);
static inline bool isOwnedbyOther (uint8_t pos);
static uint8_t numOwned (uint8_t pos);

// money transfer helpers
static bool payPlayer (uint8_t from, uint8_t to, uint32_t amount);
static bool paySFE (uint32_t amount);
static void receiverFromBank (uint32_t amount);

// rent helpers
uint32_t rentFromHouses (uint8_t pos, uint8_t houses);
static uint32_t calcRent (uint8_t pos, uint8_t diceTotal);

// jail helpers
static bool inJail ()

// FUNCTIONS
// turn logic
void doTurn();
void resolveTile();

// jail logic
void goToJail();
