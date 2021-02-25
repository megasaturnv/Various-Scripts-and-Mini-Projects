// MegaSaturnv 2017-02-23

int inputPin = 13;
int loopcount = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("Ready!");
  Serial.println(inputPin);
  
}

void loop() {
  pinMode(inputPin, INPUT);
  int sensorVal = digitalRead(inputPin);
  Serial.println(sensorVal);
  delay(500);
  pinMode(inputPin, INPUT_PULLUP);
  delay(500);
}



