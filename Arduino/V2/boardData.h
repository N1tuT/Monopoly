// ---------------------------------------------------
// File:       boardData.h
// Project:    Monopoly
// Author:     N1tuT
// Version:    v1.0
// ---------------------------------------------------

#pragma once
#include "config.h"

enum PriceRow {
    PRICE = 0,
    RENT,
    HOUSE1,
    HOUSE2,
    HOUSE3,
    HOUSE4,
    HOTEL,
    MORTGAGE,

    priceRowCount
};
constexpr uint8_t PRICE_ROWS = priceRowCount;

enum TileColour : uint8_t {
    NONE = 0,

    // Property colours
    PURPLE,
    LBLUE,
    PINK,
    ORANGE,
    RED,
    YELLOW,
    GREEN,
    BLUE,

    // Ownable special
    STATION,
    UTILITY,

    // Action subtypes
    CHONCE,
    CHEST,
    GO,
    FLU,
    SFE
};

enum TileCatagory : uint8_t {
    ACTION = 0,
    PROPERTY,
    JAIL
};


struct BoardData {
    const char* const places[BOARD_SIZE];
    const int prices[PRICE_ROWS][BOARD_SIZE];
    const TileCatagory[BOARD_SIZE];
    const TileColour colour[BOARD_SIZE];
};
extern const BoardData board;

int findTileIndex (const char* target);