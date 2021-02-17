#include <Wire.h>

int mode = 1;
unsigned long previousMillis = 0;
const long interval = 1000;

void setup() {
  //attachInterrupt(0, gogogo, RISING);
  Serial.begin(9600);
}

double numofTerms = 1000000000;
float pi = 0;

void loop() {
  if (mode == 1) {
    pi = 0;
    unsigned long currentMillis = millis();

    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis;
    }
    mode = 2;
  } else {
    int time = 0;
    Serial.println("Working...");
    for (float k = 0.0; k <= numofTerms; k++) {
      pi += 4.0 * ( pow((-1.0), k) ) * ( 1.0 / (2.0 * k + 1) );

      unsigned long currentMillis = millis();
      if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;
        //Serial.print("Iteration: ");
        //Serial.print(k);
        Serial.print("Pi = ");
        Serial.print(pi, 32);
        Serial.println("");
        //Serial.print(".");
        time++;
      }
      //  numofTerms++;
    }
    Serial.println(" ");
    Serial.println(" ");
    Serial.print("Final calculation of Pi is: ");
    Serial.print(pi);
    Serial.println("");
    // lcd.print(((actualPi/100))*pi,7);
    Serial.print(" Taking: ");
    Serial.print(time);
    Serial.println(" Seconds to complete");
    delay(1000000);
    mode = 1;
  }
}

void gogogo() {
  mode++;
  Serial.println(mode);
}
