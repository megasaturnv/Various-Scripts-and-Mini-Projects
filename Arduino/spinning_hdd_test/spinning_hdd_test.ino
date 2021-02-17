void setup() {
  pinMode(A0, INPUT);
  pinMode(13, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  digitalWrite(13, HIGH);
  digitalWrite(2, HIGH);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  delay(2000);
}

void loop() {
  byte x = analogRead(A0);
  digitalWrite(13, LOW);
  digitalWrite(2, LOW);
  digitalWrite(3, HIGH);
  delay(x);
  digitalWrite(3, LOW);
  digitalWrite(4, HIGH);
  delay(x);
  digitalWrite(4, LOW);
  digitalWrite(13, HIGH);
  digitalWrite(2, HIGH);
  delay(x);
}
