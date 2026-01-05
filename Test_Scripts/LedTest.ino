/*
  ------------------------------------------------------------
  Project: Monopoly
  Author: N1tuT
  Date: 28 DEC 2025
  Version: v1.0

  Description:
  This script controls a WS2812B LED strip using the FastLED
  library. The LEDs are divided into groups of four, with each
  group displaying a repeating colour pattern representing
  each player:
    - Red
    - Blue
    - Green
    - Yellow

  This script is designed to test the LED hardware and verify
  that all connections are working correctly. It lights up
  every space on the board with the specified player colours,
  making any faulty LEDs or wiring issues easy to identify.
  ------------------------------------------------------------
*/

#include <FastLED.h>

#define pPlayer 22                                            // data pin for PLAYER LEDs
#define pHouses 23                                            // data pin for HOUSES LEDs
#define nLEDPlayer 16                                         // number of LEDs in the PLAYER strip
#define nLEDHouses 16                                         // number of LEDs in the HOUSES strip

// Define LED colour array and position array
CRGB colours[4] = {CRGB::Red, CRGB::Blue, CRGB::Green, CRGB::Yellow};
CRGB pos[nLEDPlayers];                                        // array of all LEDs in the PLAYER strip
CRGB pos[nLEDHouses];                                         // array of all LEDs in the HOUSES strip

void setup() {
  FastLED.addLeds<WS2812B, pPlayer, GRB>(pos, nLedPlayer);    // initiate LED strip
  FastLED.setBrightness(2);
}

void loop() {
  int places = nLEDPlayer / 4;                              // number of PLAYER places around the board
  int property = nLEDHouses / 4;                            // number of HOUSES places around the board
  
  // Loop to turn on all PLAYER LEDs in specific colours
  int lPlayer;
  for (int i = 0; i < places; i++) {
    // increment loop by four
    lPlayer = 4 * i;

    // set each LED as specific colour
    pos[0 + lPlayer] = CRGB::Red;
    pos[1 + lPlayer] = CRGB::Blue;
    pos[2 + lPlayer] = CRGB::Green;
    pos[3 + lPlayer] = CRGB::Yellow;
  }

  // Loop to turn on all HOUSES LEDs in specific colour
  int lHouses;
  for (int i = 0; i < places; i++) {
    // increment loop by four
    lHouses = 4 * i;

    // set each LED as specific colour
    pos[0 + lHouses] = CRGB::Green;
    pos[1 + lHouses] = CRGB::Green;
    pos[2 + lHouses] = CRGB::Green;
    pos[3 + lHouses] = CRGB::Red;
  }

  FastLED.show();
}