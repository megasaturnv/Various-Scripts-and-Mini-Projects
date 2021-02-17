#define batteryVoltageSensorPin A7

bool condition = true;
String str = "";

void setup() {
  Serial.begin(1200);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  delay(100);
}

String batteryvoltagesensor() {
  float voltage = analogRead(batteryVoltageSensorPin) * (5.0 / 102.3);
  return String(voltage);
}

void loop() {
  digitalWrite(13, (!digitalRead(13)));
  condition = !condition;
  str = "";
  
  if (condition) {
    str = "True";
  } else {
    str = "False";
  }
  Serial.println(str);

  condition = !condition;
  str = "";
  
  str = condition ? "true" : "false";
  Serial.println(str);

condition = !condition;
  delay(5000);
}

