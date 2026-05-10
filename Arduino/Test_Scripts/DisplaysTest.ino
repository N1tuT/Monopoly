/*
  ------------------------------------------------------------
  Project: Monopoly
  Author: N1tuT
  Date: 29 DEC 2025
  Version: v1.0

  Description:
  This script tests the use of a multiplexer to daisy chain
  four oled displays, each displaying something different.

  The script also tests out potential screens that will be
  used during the game of monopoly.
  ------------------------------------------------------------
*/


// Libraries
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#include <Fonts/FreeSans9pt7b.h>

// I2C addresses
#define TCA_ADDR 0x70         // TCA9548A default address
#define OLED_ADDR 0x3C        // SSD1306 I2C OLEDs

// OLED config
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1         // Usually no reset pin on I2C modules

// OLED object
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Select TCA9548A channel
void tcaSelect(uint8_t channel) {
  if (channel > 3) return;
  Wire.beginTransmission(TCA_ADDR);
  Wire.write(1 << channel);
  Wire.endTransmission();
}

// Check if I2C device exists at address
bool probeI2C(uint8_t addr) {
  Wire.beginTransmission(addr);
  return (Wire.endTransmission() == 0);
}

// Prepare OLED for a given player index
bool preparePlayerDisplay(uint8_t playerIndex) {

  uint8_t channel = playerIndex;

  // Select the correct TCA9548A channel
  tcaSelect(channel);
  delay(5);

  // Check if an OLED exists on this channel
  if (!probeI2C(OLED_ADDR)) {
    return false;
  }

  // Initialise the OLED on this channel
  if (!display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR)) {
    return false;
  }

  // Clear screen buffer
  display.clearDisplay();

  // White text on black background
  display.setTextColor(SSD1306_WHITE);

  return true;  // Display is ready
}


/*
SCREENS
*/

// Light all pixels on OLED on given channel
void showAllPixelsOn(uint8_t channel) {
  tcaSelect(channel);
  delay(5);

  // Check if an OLED is actually present on this channel
  if (!probeI2C(OLED_ADDR)) {
    Serial.print(F("OLED "));
    Serial.print(channel+1);
    Serial.println(F(": no OLED found"));
    return;
  }

  // Init display while THIS channel is selected
  if (!display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR)) {
    Serial.print(F("Channel "));
    Serial.print(channel+1);
    Serial.println(F(": SSD1306 begin() failed"));
    return;
  }

  // Turn every pixel on (white)
  display.clearDisplay();
  display.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, SSD1306_WHITE);

  // Put channel label in black so you can identify it
  display.setTextSize(2);
  display.setTextColor(SSD1306_BLACK);
  display.setCursor(1, 1);
  display.print(F("Player "));
  display.print(channel+1);

  display.display();

  Serial.print(F("Channel "));
  Serial.print(channel);
  Serial.println(F(": OLED lit (all pixels on)"));
}

void pressToJoin(uint8_t playerCount) {

  for (uint8_t playerIndex = 0; playerIndex < playerCount; playerIndex++) {

    if (!preparePlayerDisplay(playerIndex)){
      continue;
    }

    uint8_t playerNumber = playerIndex + 1;

    /*************************************************
     *  Draw welcome message
     *************************************************/

    // Top line
    display.setTextSize(2);
    display.setCursor(0, 0);
    display.print(F("Player "));
    display.print(playerNumber);

    // Big player number
    display.setTextSize(3.5);
    display.setCursor(20, 30);
    display.println(F("Join"));

    // Send buffer to display
    display.display();
  }
}

void showWelcomeScreens(uint8_t playerCount) {

  for (uint8_t playerIndex = 0; playerIndex < playerCount; playerIndex++) {

    if (!preparePlayerDisplay(playerIndex)){
      continue;
    }

    uint8_t playerNumber = playerIndex + 1;

    /*************************************************
     *  Draw welcome message
     *************************************************/
    //display.setFont(&FreeSans9pt7b);

    // Top line
    display.setTextSize(1.7);
    display.setCursor(0, 0);
    display.println(F("Welcome Player"));

    // Big player number
    display.setTextSize(3);
    display.setCursor(centerX("1", 3), centerY(3));
    display.print(playerNumber);

    // Bottom text
    display.setTextSize(1.7);
    display.setCursor(0, 48);
    display.println(F("to Monopoly:"));
    display.println(F("Uni Edition"));

    // Send buffer to display
    display.display();
  }
}


/*
FUNCTIONS
*/

int16_t centerX(const char* text, uint8_t textSize) {
  uint16_t textWidth = strlen(text) * 6 * textSize;
  return (SCREEN_WIDTH - textWidth) / 2;
}

int16_t centerY(uint8_t textSize) {
  uint16_t textHeight = 8 * textSize;
  return (SCREEN_HEIGHT - textHeight) / 2;
}

void setup() {
  Serial.begin(115200);
  while (!Serial) {;}

  Wire.begin();  // Mega: SDA=20, SCL=21

  Serial.println(F("\nTCA9548A + SSD1306 OLED test: ALL PIXELS ON"));

  // Check TCA presence
  if (!probeI2C(TCA_ADDR)) {
    Serial.print(F("ERROR: TCA9548A not found at 0x"));
    Serial.println(TCA_ADDR, HEX);
    Serial.println(F("Check SDA/SCL wiring and address jumpers"));
  } else {
    Serial.print(F("TCA9548A found at 0x"));
    Serial.println(TCA_ADDR, HEX);
  }

  // Light up every OLED you have connected across channels
  for (uint8_t ch = 0; ch < 3; ch++) {
    showAllPixelsOn(ch);
    delay(250);
  }

  Serial.println(F("Done. Displays should stay lit."));
}

void loop() {

  const uint8_t players = 4;

  pressToJoin(players);
  delay(5000);
  showWelcomeScreens(players);
  delay(5000);
}


