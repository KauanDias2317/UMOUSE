#include <ESP32Servo.h>

#define trigRight 21
#define echoRight 18
#define trigFront 32
#define echoFront 23
#define trigLeft 25
#define echoLeft 35

#define servoE 27
#define servoD 17

#define VEL_SOM 0.034

Servo servoMotor1;
Servo servoMotor2;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  servoMotor1.attach(servoE);
  servoMotor2.attach(servoD);

  pinMode(trigRight, OUTPUT);
  pinMode(trigFront, OUTPUT);
  pinMode(trigLeft, OUTPUT);

  pinMode(echoRight, INPUT);
  pinMode(echoFront, INPUT);
  pinMode(echoLeft, INPUT);

}

void girarRodaE() {
  for (int pos = 0; pos <= 180; pos += 1){
    servoMotor1.write(pos);
  }
}

void girarRodaD() {
  for (int pos = 0; pos <= 180; pos += 1){
    servoMotor2.write(pos);
  }
}

int dispararSensor(int trig, int echo) {
  long duracao;
  float distancia;

  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  duracao = pulseIn(echo, HIGH);
  distancia = duracao * VEL_SOM / 2;

  return distancia;
}

bool checarParede(int distancia) {
  if (distancia < 100) {
    return true;
  }

  else {
    return false;
  }
}

void loop() {
  int sensorE;
  int sensorF;
  int sensorD;

  sensorE = checarParede(dispararSensor(trigLeft, echoLeft));
  sensorF = checarParede(dispararSensor(trigFront, echoFront));
  sensorD = checarParede(dispararSensor(trigRight, echoRight));

  if (sensorF) {
    girarRodaE();
  }
  else if (!sensorE) {
    girarRodaD();
  }
  else {
    girarRodaE();
    girarRodaD();
  }

  delay(10); // this speeds up the simulation
}
