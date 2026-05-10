// ---------------------------------------------------
// File:       gameFlow.cpp
// Project:    Monopoly
// Author:     N1tuT
// Version:    v1.0
// ---------------------------------------------------

#include "gameFlow.h"
#include "dice.h"
#include "players.h"
#include "boardData.h"
#include "propertyState.h"
#include "LEDs.h"

// Ownership helpers
static inline bool isOwnable (uint8_t pos) {
    return board.category[pos] == PROPERTY;
}

static inline bool isUnowned (uint8_t pos) {
    return propertyState.owner[pos] == -1; 
}

static inline bool isOwnedbyOther (uint8_t pos) {
    int8_t owner = propertyState.owner[pos];
    return (owner >= 0) && (owner != currentPlayer);
}

static uint8_t numOwned (uint8_t pos) {
    int8_t owner = propertyState.owner[pos];
    if (owner < 0) return 0;

    uint8_t count = 0;

    if (board.colour[pos] == STATION) {
        constexpr uint8_t stations[] = {5, 15, 25, 35};

        for (uint8_t i = 0; i < 4; i++) {
            if (propertyState.owner[stations[i]] == owner) {
                count++;
            }
        }
        return count;
    }

    if (board.colour[pos] == UTILITY) {
        constexpr uint8_t utilities[] = {12, 28, 36};

        for (uint8_t i = 0; i < 3; i++) {
            if (propertyState.owner[utilities[i]] == owner) {
                count++;
            }
        }
        return count;
    }

    return 0;
}

// money transfer helpers
static bool payPlayer (uint8_t from, uint8_t to, uint32_t amount) {
    if (players[from].money < amount) return false; // if player is bankrupt

    players[from].money -= amount;
    players[to].money += amount;
    return true;
}

static bool paySFE (uint32_t amount) {
    if (players[currentPlayer].money < amount) return false; // if player is bankrupt
    
    players[currentPlayer].money -= amount;
    // add to SFE
    return true;
}

static void receiverFromBank (uint32_t amount) {
    players[currentPlayer].money += amount;
}

// Rent helpers
uint32_t rentFromHouses (uint8_t pos, uint8_t houses) {
    switch (houses) {
        case 0: return board.prices[RENT][pos];
        case 1: return board.prices[HOUSE1][pos];
        case 2: return board.prices[HOUSE2][pos];
        case 3: return board.prices[HOUSE3][pos];
        case 4: return board.prices[HOUSE4][pos];
        case 5: return board.prices[HOTEL][pos];
        default: return 0;
    }
}

static uint32_t calcRent (uint8_t pos, uint8_t diceTotal) {
    // Stations
    if (board.colour[pos] == STATION) {
        int count = numOwned(pos);
        return rentFromHouses(pos, count);
    }

    // Utilities
    if (board.colour[pos] == UTILITY) {
        int count = numOwned(pos);

        switch (count) {
            case 0: return 0;
            case 1: return (uint32_t)diceTotal * 3
            case 2: return (uint32_t)diceTotal * 6
            case 3: return (uint32_t)diceTotal * 9
            default: return 0;
        }
    }

    // Properties
    uint8_t houses = propertyState.house_num[pos];
    return rentFromHouses(pos, count);
}

// Jail helper
static bool inJail () {
    Player &p = players[currentPlayer];
    
    p.sickCount++;

    // jail longer than 3 turns and paid fee
    if (p.sickCount >= 3 && paySFE(JAIL_FEE)) {
        return false;   // no longer in jail
    } else {
        // bankrupcy logic
        return false;
    }

    // choose to pay SFE
    // if (choseBuyCure && paySFE(JAIL_FEE)) {
    //     return false;
    // }

    return true;
}


// Jail function
void goToJail () {
    Player &p = players[currentPlayer];

    p.sick = true;
    p.sickCount = 0;
    p.pos = findTileIndex("Freshers' Flu");
    // move player LED to jail
}


// Game flow functions
void doTurn() {
    Player &p = players[currentPlayer];


    if (p.sick) {
        if (inJail(currentPlayer)) {
            return;
        }

        // leave jail
        p.sick = false;
        p.sickCount = 0;
        p.pos = findTileIndex("Get Well Soon");
        return;
    }


    int dCount = 0;

    while (true) {
        DiceResult roll = rollDice();

        movePlayer(roll.total);
        resolveTile();

        if (!roll.isDouble) break;

        dCount++;

        if (dCount >= 3) {
            goToJail(currentPlayer);
            return;
        }
    }
};

void resolveTile() {

};