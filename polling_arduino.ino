int a = 2;
int b = 3;
int c = 4;

void setup() {
  Serial.begin(9600);
  pinMode(a, INPUT_PULLUP);
  pinMode(b, INPUT_PULLUP);
  pinMode(c, INPUT_PULLUP);
}

void loop() {
  if (!digitalRead(a)) {
    Serial.println("A");
    delay(300);
  }

  if (!digitalRead(b)) {
    Serial.println("B");
    delay(300);
  }

  if (!digitalRead(c)) {
    Serial.println("C");
    delay(300);
  }
}