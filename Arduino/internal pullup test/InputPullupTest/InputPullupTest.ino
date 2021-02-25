// MegaSaturnv 2017-02-23

int inputPin = 14;

void setup() {
  Serial.begin(9600);
  Serial.println("Ready!");
  delay(1000);
  pinMode(inputPin, INPUT_PULLUP);
}

void loop() {
  int sensorVal = digitalRead(inputPin);
  Serial.println(sensorVal);
}



