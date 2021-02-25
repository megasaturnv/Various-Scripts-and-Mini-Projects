#include "LedControl.h"
// download from - http://playground.arduino.cc/Main/LedControl
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
// download from - http://hmario.home.xs4all.nl/arduino/LiquidCrystal_I2C/
LedControl lc = LedControl(12, 11, 10, 1);
int mode = 1;
float actualPi = 3.14159265358;
unsigned long previousMillis = 0; 
int face = 0;
const long interval = 1000;  
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);  // Set the LCD I2C address


void setup() {
  attachInterrupt(0, gogogo, RISING);
  lcd.begin(16, 2);              // initialize the lcd
  lc.shutdown(0, false);
  /* Set the brightness to a medium values */
  lc.setIntensity(0, 0);
  /* and clear the display */
  lc.clearDisplay(0);
  // initialize serial:
  
  Serial.begin(115200);

}
double numofTerms = 35000;
float pi = 0;

void loop() {

  if (mode == 1) {
    pi = 0;
     unsigned long currentMillis = millis();

        if (currentMillis - previousMillis >= interval) {
          previousMillis = currentMillis;
         if(face == 0){
           face = 1;
         }
         else{
           face = 0;
         }
        }
    writeFace();
    writeStart();
  }
  else {
    int time = 0;
  face = 2;
   // writeFace();
      Serial.println("Working...");
      for (float k = 0.0; k <= numofTerms; k++) {
        pi += 4.0 * ( pow((-1.0), k) ) * ( 1.0 / (2.0 * k + 1) );

        unsigned long currentMillis = millis();
        if (currentMillis - previousMillis >= interval) {
          previousMillis = currentMillis;
          lcd.home ();
          lcd.clear();
          lcd.print(pi, 7);
          Serial.print("Iteration: ");
          Serial.print(k);
          Serial.print(" Pi = ");
          Serial.print(pi, 7);
          Serial.println("");
          //Serial.print(".");
          time++;
           if(face == 2){
           face = 3;
         }
         else{
           face = 2;
         }
          writeFace();
        }
        //  numofTerms++;

      }
      Serial.println(" ");
      Serial.println(" ");
      Serial.print("Final calculation of Pi is: ");
      Serial.print(pi, 7);
      lcd.setCursor ( 0, 1 );
       face = 4;
      writeFace();
      Serial.println("");
      if (actualPi > pi) {
        float tempval = (actualPi - pi) / ((actualPi + pi) / 2) * 100;
        lcd.print("-");
        lcd.print(tempval, 4);

        Serial.println(tempval, 7);
        Serial.print("-");
      }
      else {
        float tempval = (pi - actualPi) / ((pi + actualPi) / 2) * 100;
        lcd.print("+");
        lcd.print(tempval, 4);
        Serial.println(tempval, 7);
        Serial.print("+");
      }
      lcd.print("%");
      delay(5000);
      // lcd.print(((actualPi/100))*pi,7);
      lcd.setCursor ( 0, 1 );
      lcd.print("in ");
      Serial.print(" Taking: ");
      Serial.print(time);
      lcd.print(time);
       lcd.print(" seconds");
      face = 4;
      writeFace();
      Serial.println(" Seconds to complete");
      Serial.println("Of course Pi really is 3.14159265358... but I had to look it up.");
      delay(10000);
      mode = 1;
      lcd.clear();
      
    


  }
  
  
}

void writeFace() {
  byte q1[8] = {B00000000, B00000000, B00011111, B00010001, B10110001, B00000111, B00000000, B00000000};
  byte smile[8] = {B00000010, B01001010, B10000010, B10111000, B10100000, B10000010, B01001010, B00000010};
  byte think[8] = {B00000001, B10001001, B10000011, B10111000, B10100000, B10000011, B10001001, B00000001};
  byte think2[8] = {B00000000, B10001001, B10000010, B10111000, B10100000, B10000010, B10001001, B00000000};
  byte pi[8] = {B00000010, B10000001, B01111111, B00000001, B00000001, B01111111, B10000001, B01000001};
  lc.clearDisplay(0);

  //  delay(delaytime);
 
if(face == 0){
  lc.setRow(0, 0, pi[0]);
  lc.setRow(0, 1, pi[1]);
  lc.setRow(0, 2, pi[2]);
  lc.setRow(0, 3, pi[3]);
  lc.setRow(0, 4, pi[4]);
  lc.setRow(0, 5, pi[5]);
  lc.setRow(0, 6, pi[6]);
  lc.setRow(0, 7, pi[7]);
}

if(face == 1){
  lc.setRow(0, 0, q1[0]);
  lc.setRow(0, 1, q1[1]);
  lc.setRow(0, 2, q1[2]);
  lc.setRow(0, 3, q1[3]);
  lc.setRow(0, 4, q1[4]);
  lc.setRow(0, 5, q1[5]);
  lc.setRow(0, 6, q1[6]);
  lc.setRow(0, 7, q1[7]);
}

if(face == 2){
  lc.setRow(0, 0, think[0]);
  lc.setRow(0, 1, think[1]);
  lc.setRow(0, 2, think[2]);
  lc.setRow(0, 3, think[3]);
  lc.setRow(0, 4, think[4]);
  lc.setRow(0, 5, think[5]);
  lc.setRow(0, 6, think[6]);
  lc.setRow(0, 7, think[7]);
}
if(face == 3){
  lc.setRow(0, 0, think2[0]);
  lc.setRow(0, 1, think2[1]);
  lc.setRow(0, 2, think2[2]);
  lc.setRow(0, 3, think2[3]);
  lc.setRow(0, 4, think2[4]);
  lc.setRow(0, 5, think2[5]);
  lc.setRow(0, 6, think2[6]);
  lc.setRow(0, 7, think2[7]);
}
if(face == 4){
  lc.setRow(0, 0, smile[0]);
  lc.setRow(0, 1, smile[1]);
  lc.setRow(0, 2, smile[2]);
  lc.setRow(0, 3, smile[3]);
  lc.setRow(0, 4, smile[4]);
  lc.setRow(0, 5, smile[5]);
  lc.setRow(0, 6, smile[6]);
  lc.setRow(0, 7, smile[7]);

}
}


void writeStart() {
lcd.home ();                   // go home
  lcd.print("Hey! Wanna see ");
  lcd.setCursor ( 0, 1 );        // go to the next line
  lcd.print ("me calculate Pi?");

}
void gogogo()
{
  mode++;
  Serial.println(mode);
}

