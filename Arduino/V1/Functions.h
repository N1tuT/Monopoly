// Functions.h
//  -------------------------------------------------------------
//  Project:    Monopoly
//  Author:     N1tuT
//  Date:       05 JAN 2025
//  Version:    v1.0
//  -------------------------------------------------------------
//  Core data definitions for game
//
//  File declares all shared game structures
//  and global state used across project
//
//  IMPORTANT:
//  - file contains declarations only
//  - all data defined in 'Functions.cpp'
//  -------------------------------------------------------------


#pragma once
#include <Arduino.h>
#include <FastLED.h>

// pin assignments
#define pLedPlayer  22
#define pLedHouses  23

// LED definitions
#define numLedPlayer  160
#define numLedHouses  29
#define LEDType       WS2812B

extern CRGB playerLeds[numLedPlayer];
extern CRGB houseLeds[numLedHouses];

uint16_t LEDindex(uint8_t tile);

void setupLEDs();
void showPlayerPos();
void movePlayer(int roll);
void showPropHouse();

// Total number of spaces on board
#define BOARD_SIZE 40

// Max number of players
#define PLAYER_COUNT 4

// index of player whose turn it currently is
extern uint8_t currentPlayer;

// player turn logic
void doTurn();        // contains all player turn logic / functions
void resolveTile();   // carries out tile logic

// Stores dice roll and if it is a double
struct DiceResult {
  uint8_t total;  // sum of dice
  bool isDouble;  // double flag
};
DiceResult rollDice();

// Price table row meanings
enum PriceRow {
  // ---------------------------------------------------------
  // enum values describe what each row in
  // BoardData::prices table represents

  // prices[row][space]

  // e.g.
  //   prices[RENT][10]    ->  base rent for space 10
  //   prices[HOUSE3][24]  ->  rent with 3 houses on space 24
  // ---------------------------------------------------------

  PRICE = 0,  // purchase price of property
  RENT,       // rent with 0 houses
  HOUSE1,     // rent with 1 house
  HOUSE2,     // rent with 2 houses
  HOUSE3,     // rent with 3 houses
  HOUSE4,     // rent with 4 houses
  HOTEL,      // rent with hotel
  MORTGAGE,   // mortgage value of property

  // Total number of price rows
  priceRowCount
};
#define PRICE_ROWS priceRowCount

// Tile type meanings
enum TileType {
  //
  // enum values describe what each row in
  // BoardData::tileType table represents
  //
  // tileType[row][space]
  // 
  //  rows:
  //  - category: action, property, nothing
  //  - colour:   chonce, chest, tax, SFE, station, utility, (colours), jail
  //
  // e.g.
  //    tileType[Category][10]  ->  category for tile 10
  //    tileType[Colour][20]    ->  colour for tile 20
  //

  CATEGORY = 0,
  COLOUR,

  // Total number of tileType rows
  tileTypeRows
};
#define TILE_TYPE_ROWS tileTypeRows

// Static board data
struct BoardData {
  // ---------------------------------------------------------
  // struct containing data that NEVER changes
  // board layout and pricing rules
  //
  //  places:   all names of places on board
  //  prices:   pricing info of every property
  //  ---------------------------------------------------------

  const char* const places[BOARD_SIZE];
  const int prices[PRICE_ROWS][BOARD_SIZE];
  const char* const tileType[TILE_TYPE_ROWS][BOARD_SIZE];

};
extern const BoardData board;

int findTileIndex (const char* target) {};

// Dynamic property states
struct PropertyState {
  // ---------------------------------------------------------
  // struct tracking ownership & development
  // per property on board
  // 
  //  owner:      owner per tile
  //    -1 = unowned
  //    0+ = owner id
  //
  //  house_num:  number of houses per tile
  //    0 = none
  //    1-4 = houses
  //    5 = hotel
  // ---------------------------------------------------------

  int8_t owner[BOARD_SIZE];
  uint8_t house_num[BOARD_SIZE];

};
extern PropertyState propertyState;

// Player states
struct Player {
  // ---------------------------------------------------------
  // struct repressenting all data per player
  // 
  //  pos:      current board position
  //  money:    current balance
  //  sick:     true if affected by illness
  //  firstLap: true if player passes go for 1st time
  // ---------------------------------------------------------

  uint8_t pos;
  uint32_t money;
  bool sick;
  uint8_t sickCount;
  bool firstLap;

};
extern Player players[PLAYER_COUNT];


