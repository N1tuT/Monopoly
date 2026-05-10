// ---------------------------------------------------
// File:       config.h
// Project:    Monopoly
// Author:     N1tuT
// Version:    v1.0
// ---------------------------------------------------

#pragma once
#include <Arduino.h>

// Board & players
constexpr uint8_t BOARD_SIZE = 40;
constexpr uint8_t PLAYER_COUNT = 4;

// Pins
constexpr uint8_t PIN_LED_PLAYER = 22;
constexpr uint8_t PIN_LED_HOUSES = 23;

// LED config
constexpr uint16_t NUM_LED_PLAYER = 160;
constexpr uint16_t NUM_LED_HOUSES = 29;

// Global constants
constexpr uint32_t JAIL_FEE = 50;