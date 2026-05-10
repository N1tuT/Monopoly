// ---------------------------------------------------
// File:       LEDs.h
// Project:    Monopoly
// Author:     N1tuT
// Version:    v1.0
// ---------------------------------------------------

#pragma once
#include <FastLED.h>
#include "config.h"

extern CRGB playerLeds[NUM_LED_PLAYER];
extern CRGB houseLeds[NUM_LED_HOUSES];

uint16_t LEDindex(uint8_t tile);

void setupLEDs();
void showPlayerPos();
void movePlayer(int roll);
void showPropHouse();