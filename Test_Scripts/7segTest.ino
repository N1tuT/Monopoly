/*
  ------------------------------------------------------------
  Project: Monopoly
  Author: N1tuT
  Date: 29 DEC 2025
  Version: v1.0

  Description:
  This script controls a TM1637 4-Digit 7-segment LED display.
  The display runs through numbers 0-999, testing each works
  accordingly.
  ------------------------------------------------------------
*/



#include <TM1637Display.h>

// Define the connections pins
#define CLK 3
#define DIO 2

// Create a display object of type TM1637Display
TM1637Display display = TM1637Display(CLK, DIO);

// Create an array that turns all segments ON
const uint8_t allON[] = { 0xff, 0xff, 0xff, 0xff };

// Create an array that turns all segments OFF
const uint8_t allOFF[] = { 0x00, 0x00, 0x00, 0x00 };

void setup() {
  // Set the brightness to 5 (0=dimmest 7=brightest)
  display.setBrightness(0);

  // Set all segments ON
  display.setSegments(allON);
  delay(2000);
  display.clear();
}

void loop() {

  // Show counter 0-9999
  int i;
  for (i = 0; i < 10000; i++) {
    display.showNumberDec(i);
    delay(50);
  }
  delay(2000);
  display.clear();
}