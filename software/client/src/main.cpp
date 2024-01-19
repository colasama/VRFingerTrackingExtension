#include <Wire.h>
#include "Adafruit_MPR121.h"
#include <SimpleKalmanFilter.h>

#ifndef _BV
#define _BV(bit) (1 << (bit)) 
#endif

Adafruit_MPR121 cap = Adafruit_MPR121();
SimpleKalmanFilter simpleKalmanFilters[12];
void setup() {
  Serial.begin(115200);

  while (!Serial) {
    delay(10);
  }
  
  // Default address is 0x5A, if tied to 3.3V its 0x5B
  // If tied to SDA its 0x5C and if SCL then 0x5D
  if (!cap.begin(0x5B)) {
    Serial.println("MPR121 not found, check wiring?");
    while (1);
  }
  Serial.println("MPR121 found!");

  // Init the SimpleKalmanFilter
  for (int i = 0; i < 12; i ++) {
    SimpleKalmanFilter simpleKalmanFilter(2, 2, 0.01);
    simpleKalmanFilters[i] = simpleKalmanFilter;
  }
}

void loop() {
  // Transmit data by serial
  // TODO: UDP + WiFi
  Serial.print("\t\t\t\t\t\t\t\t\t\t\t\t\t 0x"); Serial.println(cap.touched(), HEX);
  Serial.print("Filt: ");
  for (uint8_t i=0; i<12; i++) {
    Serial.print(simpleKalmanFilters[i].updateEstimate(cap.filteredData(i))); Serial.print("\t");
  }
  delay(10);
  Serial.println();
}
