//MegaSaturnv 2017-07-05
//Arduino simple digitalRead with software debounce

//Digital read an pin with software debounce. Pin should be set as: pinMode(pin, INPUT_PULLUP) in setup().
//Arduino ATMEGA328P (and some other ATMEL chips) have internal pull-up resistors. Pin is active when connected to GND
//Projects where pins are active high (with pull down resistors) should modify lines 7 and 11 below, as indicated
//This function will return true if input is active for at least 50ms and then released. The function will return false if input is not active
bool digitalReadDebounce(int pin) {
  if (digitalRead(pin) == LOW) { // <- Change to '== HIGH' if pin is active high
    delay(50);
    bool debounceRunning = true;
    while (debounceRunning) {
      if (digitalRead(pin) == HIGH) { // <- Change to '== LOW' if pin is active high
        debounceRunning = false;
      }
    }
    delay(50);
    return true;
  }
  return false;
}
