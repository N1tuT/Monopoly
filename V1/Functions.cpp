// Functions.cpp
#include "Functions.h"

// Static board definition
const BoardData board = {
    // ---------------------------------------------------------
    //  contains all IMMUTABLE board data:
    //  - Tile names
    //  - Price tables (purchase, rent, mortgage)
    // ---------------------------------------------------------

    // names
    { "Go", "Cambridge", "Communal Melons", "Oxford", "Hangover Tax", "King's Cross St", "Harvard", "Chonce", "Yale", "MIT", "Get Well Soon",
    "Nottingham", "Electric", "Birmingham", "Warwick", "Euston St", "Durham", "Chonce", "Edinburgh", "Glasgow", "Student Finance",
    "Southhampton", "Communal Melons", "Brighton", "Sussex", "Paddington St", "UCL", "KCL", "Water", "Imperial", "Freshers' Flu",
    "Cardiff", "Gloucestershire", "Chonce", "Bristol", "Victoria St", "Gas", "Queen Mary", "Groceries Bill", "Bath" },

    // prices
    {{0, 60,     0,  60,     200,    200,    100,    0,  100,    120,    0,  140,    150,    140,    160,    200,    180,    0,  180,    200,    0,  220,    0,  220,    240,    200,    260,    260,    150,    280,    0,  300,    300,    0,  320,    200,    150,    350,    100,    400},
    {0, 2,      0,  4,      0,      25,     6,      0,  6,      8,      0,  10,     0,      10,     12,     25,     14,     0,  14,     16,     0,  18,     0,  18,     20,     25,     22,     22,     0,      22,     0,  26,     26,     0,  28,     25,     0,      35,     0,      50},
    {0, 10,     0,  20,     0,      50,     30,     0,  30,     40,     0,  50,     0,      50,     60,     50,     70,     0,  70,     80,     0,  90,     0,  90,     100,    50,     110,    110,    0,      120,    0,  130,    130,    0,  150,    50,     0,      175,    0,      200},
    {0, 30,     0,  60,     0,      100,    90,     0,  90,     100,    0,  150,    0,      150,    180,    100,    200,    0,  200,    220,    0,  250,    0,  250,    300,    100,    330,    330,    0,      360,    0,  390,    390,    0,  450,    100,    0,      500,    0,      600},
    {0, 90,     0,  180,    0,      200,    270,    0,  270,    300,    0,  450,    0,      450,    500,    200,    550,    0,  550,    600,    0,  700,    0,  700,    750,    200,    800,    800,    0,      850,    0,  900,    900,    0,  1000,   200,    0,      1100,   0,      1400},
    {0, 160,    0,  320,    0,      0,      400,    0,  400,    450,    0,  625,    0,      625,    700,    0,      750,    0,  750,    800,    0,  875,    0,  875,    925,    0,      975,    975,    0,      1025,   0,  1100,   1100,   0,  1200,   0,      0,      1300,   0,      1500},
    {0, 250,    0,  450,    0,      0,      550,    0,  660,    600,    0,  750,    0,      750,    900,    0,      950,    0,  950,    1000,   0,  1050,   0,  1050,   1100,   0,      1150,   1150,   0,      1200,   0,  1275,   1275,   0,  1400,   0,      0,      1500,   0,      2000},
    {0, 30,     0,  30,     0,      100,    50,     0,  200,    60,     0,  70,     0,      70,     80,     0,      90,     0,  90,     100,    0,  110,    0,  110,    120,     0,     130,    130,    0,      140,    0,  150,    150,    0,  160,    0,      0,      175,    0,      200}}
};

// Dynamic property state
PropertyState propertyState = {
    //  ---------------------------------------------------------
    //  tracks ownership & development per property tile
    //  data changes throughout game
    //  ---------------------------------------------------------

    // property owner
    { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},

    // property's number of houses
    { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }
};

// Player state
Player players[PLAYER_COUNT] = {
    // Initial state for all players at start of game

    {0, 1500, false, true},
    {0, 1500, false, true},
    {0, 1500, false, true},
    {0, 1500, false, true}
};

// Turn tracking
// index of current player
uint8_t currentPlayer = 0;