// MegaSaturnv 2017-02-23

unsigned byte number1 = 0
unsigned byte number2 = 0

void setup() {
  pinMode(but1_0, INPUT_PULLUP);
  pinMode(but1_1, INPUT_PULLUP);
  pinMode(but1_2, INPUT_PULLUP);
  pinMode(but1_3, INPUT_PULLUP);
  
  pinMode(but2_0, INPUT_PULLUP);
  pinMode(but2_1, INPUT_PULLUP);
  pinMode(but2_2, INPUT_PULLUP);
  pinMode(but2_3, INPUT_PULLUP);
  
  pinMode(out0, INPUT_PULLUP);
  pinMode(out1, INPUT_PULLUP);
  pinMode(out2, INPUT_PULLUP);
  pinMode(out3, INPUT_PULLUP);
}

void loop() {
  bitWrite(number1,0,!digitalRead(but1_0))
  
}