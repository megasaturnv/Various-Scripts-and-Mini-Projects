// MegaSaturnv 2017-02-23

bool state = false;

bool digitalReadDebounce(int pin) {
  if (digitalRead(pin) == LOW) {
    delay(50);
    bool debounceRunning = true;
    while (debounceRunning) {
      if (digitalRead(pin) == HIGH) {
        debounceRunning = false;
      }
    }
    return true;
  }
  return false;
}

bool digitalReadDebounce2(byte pin) {
  while (!digitalRead(pin)) {
    delay(50);
    if (digitalRead(pin)) {
      return true;
    }
  }
  return false;
}

void setup() {
  pinMode(2, INPUT_PULLUP);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}

void loop() {
  if (digitalReadDebounce2(2) == true) {
    state = !state;
    if (state) {
      digitalWrite(13, HIGH);
    } else {
      digitalWrite(13, LOW);
    }
  }
}

