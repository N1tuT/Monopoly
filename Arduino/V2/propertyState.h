// ---------------------------------------------------
// File:       propertyState.h
// Project:    Monopoly
// Author:     N1tuT
// Version:    v1.0
// ---------------------------------------------------

#pragma once
#include "config.h"

struct PropertyState {
    int8_t owner[BOARD_SIZE];
    uint8_t house_num[BOARD_SIZE];
};

extern PropertyState propertyState;