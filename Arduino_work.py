const int sensorPin = A0;
const int ledFrio = 2;
const int ledCalor = 3;
const int buzzer = 4;

void setup() {
  pinMode(ledFrio, OUTPUT);
  pinMode(ledCalor, OUTPUT);
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int leitura = analogRead(sensorPin);
  float tensao = leitura * 5.0 / 1023.0;
  float temperaturaC = (tensao - 0.5) * 100;

  Serial.print("Temperatura: ");
  Serial.print(temperaturaC);
  Serial.println(" C");

if (temperaturaC < 2) {
    digitalWrite(ledFrio, HIGH);
    digitalWrite(ledCalor, LOW);
    digitalWrite(buzzer, HIGH);
  } else if (temperaturaC > 8) {
    digitalWrite(ledFrio, LOW);
    digitalWrite(ledCalor, HIGH);
    digitalWrite(buzzer, HIGH);
  } else {
    digitalWrite(ledFrio, LOW);
    digitalWrite(ledCalor, LOW);
    digitalWrite(buzzer, LOW);
  }

  delay(1000);
}
