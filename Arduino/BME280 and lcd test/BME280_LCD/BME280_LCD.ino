// MegaSaturnv 2017-02-23

/*The circuit:
 * LCD RS pin to digital pin 12
 * LCD Enable pin to digital pin 11
 * LCD D4 pin to digital pin 5
 * LCD D5 pin to digital pin 4
 * LCD D6 pin to digital pin 3
 * LCD D7 pin to digital pin 2
 * LCD R/W pin to ground
 * 10K resistor:
 * ends to +5V and ground
 * wiper to LCD VO pin (pin 3)
*/

#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define BME_SCK 13
#define BME_MISO 12
#define BME_MOSI 11
#define BME_CS 10

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme; // I2C
//Adafruit_BME280 bme(BME_CS); // hardware SPI
//Adafruit_BME280 bme(BME_CS, BME_MOSI, BME_MISO,  BME_SCK);

#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  Serial.begin(9600);
  Serial.println(F("BME280 test"));
  lcd.begin(16, 2);
  if (!bme.begin()) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    lcd.setCursor(0, 0);
    lcd.print("Cannot find a");
    lcd.setCursor(0, 1);
    lcd.print("BME280 sensor :(");
    while (1);
  }
  delay(200);
}

void loop() {
  digitalWrite(13, HIGH);
  float temp = bme.readTemperature();
  Serial.print("Temperature = ");
  Serial.print(temp);
  Serial.println(" *C");
  lcd.setCursor(0, 0);
  lcd.print(temp, 2);
  lcd.print("C");

  float pres = bme.readPressure() / 100.0F;
  Serial.print("Pressure = ");
  Serial.print(pres);
  Serial.println(" hPa");
  lcd.setCursor(7, 0);
  lcd.print(pres, 1);
  lcd.print("hPa");

  float alt = bme.readAltitude(SEALEVELPRESSURE_HPA);
  Serial.print("Approx. Altitude = ");
  Serial.print(alt);
  Serial.println(" m");
  lcd.setCursor(0, 1);
  lcd.print(alt, 3);
  lcd.print("m");

  float hum = bme.readHumidity();
  Serial.print("Humidity = ");
  Serial.print(hum);
  Serial.println(" %");
  lcd.setCursor(9, 1);
  lcd.print(hum, 3);
  lcd.print("%");

  Serial.println();
  delay(100);
  digitalWrite(13, LOW);
  delay(1900);
  lcd.clear();
}
