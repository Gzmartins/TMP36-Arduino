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
