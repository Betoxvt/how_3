// C++ code
//
int arduino = 0;

int alerta = 0;

int bomba = 0;

int sinal_flex = 0;

int ACIONA_BOMBA_ULTRA = 0;

int ACIONA_ALERTA_ULTRA = 0;

int PARA_BOMBA_ULTRA = 0;

int PARA_ALERTA_ULTRA = 0;

int distancia = 0;

int ACIONA_BOMBA_FLEX = 0;

int ACIONA_ALERTA_FLEX = 0;

int PARA_BOMBA_FLEX = 0;

int PARA_ALERTA_FLEX = 0;

long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);  // Clear the trigger
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  // Sets the trigger pin to HIGH state for 10 microseconds
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  // Reads the echo pin, and returns the sound wave travel time in microseconds
  return pulseIn(echoPin, HIGH);
}

void setup()
{
  pinMode(11, OUTPUT);
  pinMode(A0, INPUT);
  Serial.begin(9600);
  pinMode(7, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(8, OUTPUT);
}

void loop()
{
  ACIONA_ALERTA_ULTRA = 120;
  ACIONA_BOMBA_ULTRA = 150;
  PARA_ALERTA_ULTRA = 150;
  PARA_BOMBA_ULTRA = 190;
  ACIONA_ALERTA_FLEX = 930;
  ACIONA_BOMBA_FLEX = 880;
  PARA_ALERTA_FLEX = 880;
  PARA_BOMBA_FLEX = 770;
  digitalWrite(11, HIGH);
  distancia = 0.01723 * readUltrasonicDistance(2, 2);
  sinal_flex = analogRead(A0);
  Serial.println(sinal_flex);
  if (distancia > ACIONA_ALERTA_ULTRA && sinal_flex < ACIONA_ALERTA_FLEX) {
    alerta = 0;
    noTone(7);
    digitalWrite(12, LOW);
  } else {
    alerta = 1;
    delay(1000); // Wait for 1000 millisecond(s)
    tone(7, 523, 1000); // play tone 60 (C5 = 523 Hz)
    digitalWrite(12, HIGH);
    delay(1000); // Wait for 1000 millisecond(s)
    noTone(7);
    digitalWrite(12, LOW);
  }
  if (distancia > ACIONA_BOMBA_ULTRA && sinal_flex < ACIONA_BOMBA_FLEX) {
    bomba = 0;
    digitalWrite(8, LOW);
  } else {
    bomba = 1;
    digitalWrite(8, HIGH);
  }
  while (alerta == 1 || bomba == 1) {
    distancia = 0.01723 * readUltrasonicDistance(2, 2);
    sinal_flex = analogRead(A0);
    Serial.println(sinal_flex);
    if (distancia <= ACIONA_ALERTA_ULTRA || sinal_flex >= ACIONA_ALERTA_FLEX) {
      alerta = 1;
      delay(1000); // Wait for 1000 millisecond(s)
      tone(7, 523, 1000); // play tone 60 (C5 = 523 Hz)
      digitalWrite(12, HIGH);
      delay(1000); // Wait for 1000 millisecond(s)
      noTone(7);
      digitalWrite(12, LOW);
    }
    if (distancia <= ACIONA_BOMBA_ULTRA || sinal_flex >= ACIONA_BOMBA_FLEX) {
      bomba = 1;
      digitalWrite(8, HIGH);
    }
    if (alerta == 1) {
      if (distancia < PARA_ALERTA_ULTRA || sinal_flex > PARA_ALERTA_FLEX) {
        alerta = 1;
        delay(1000); // Wait for 1000 millisecond(s)
        tone(7, 523, 1000); // play tone 60 (C5 = 523 Hz)
        digitalWrite(12, HIGH);
        delay(1000); // Wait for 1000 millisecond(s)
        noTone(7);
        digitalWrite(12, LOW);
      }
      if (distancia >= PARA_ALERTA_ULTRA && sinal_flex <= PARA_ALERTA_FLEX) {
        alerta = 0;
        noTone(7);
        digitalWrite(12, LOW);
      }
    } else {
      alerta = 0;
      noTone(7);
      digitalWrite(12, LOW);
    }
    if (bomba == 1) {
      if (distancia < PARA_BOMBA_ULTRA || sinal_flex > PARA_BOMBA_FLEX) {
        bomba = 1;
        digitalWrite(8, HIGH);
      }
      if (distancia >= PARA_BOMBA_ULTRA && sinal_flex <= PARA_BOMBA_FLEX) {
        bomba = 0;
        digitalWrite(8, LOW);
      }
    } else {
      bomba = 0;
      digitalWrite(8, LOW);
    }
  }
}