// MegaSaturnv 2017-02-23

long var = 0;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(9, INPUT);
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  Serial.println("Ready");
  delay(1000);
}

void loop() {
  digitalWrite(13, HIGH);
  var = pulseIn(9,HIGH,10000);
  delay(500);
  Serial.println("Delay: "+String(var));
  digitalWrite(13, LOW);
  delay(10000);
}

