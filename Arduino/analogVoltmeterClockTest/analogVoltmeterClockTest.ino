#define pwmPin 11
#define voltmeterMin 70
#define voltmeterMax 255

void setup() {
  Serial.begin(9600);
  pinMode(pwmPin, OUTPUT);
  analogWrite(pwmPin, voltmeterMin);

  /*delay(3000);
  analogWrite(pwmPin, voltmeterMax);
  delay(3000);*/
}

void loop() {
  //byte pwmInt = int((float(millis() % 60000) / 60000) * 255);
  byte pwmInt = map((float(millis() % 60000) / 60), 0, 1000, voltmeterMin, voltmeterMax+1);
  analogWrite(pwmPin, pwmInt);
  Serial.println("Set: " + String(pwmInt));
  delay(100);
}
