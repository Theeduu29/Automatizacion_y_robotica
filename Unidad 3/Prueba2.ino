#include <SoftwareSerial.h>
SoftwareSerial BT1(10,11); // RX, TX recordar que se cruzan

// Pines para los motores
int inputs[4] = {2, 4, 7, 8};
int enables[2] = {5, 6};

// Matrices para estados y velocidades
int mestados[5][4] = {
  {1, 0, 1, 0},  // Avanzar
  {0, 1, 0, 1},  // Reversa
  {0, 0, 0, 0},  // Detenerse
  {0, 1, 1, 0},  // Izquierda
  {1, 0, 0, 1}   // Derecha
};
int velocidades[5][2] = {
  {150, 150},
  {150, 150},
  {0, 0},
  {130, 130},
  {130, 130}
};

// Pines para sensores infrarrojos
const int sensorPin1 = 9;
const int sensorPin2 = 3;

void setup() {
  Serial.begin(9600);
  BT1.begin(9600);
  BT1.setTimeout(10);

  // Configurar pines de motores como salida
  for (int i = 0; i < 4; i++) {
    pinMode(inputs[i], OUTPUT);
  }

  // Configurar pines de sensores como entrada
  pinMode(sensorPin1, INPUT);
  pinMode(sensorPin2, INPUT);
}

void loop() {
  // Detectar obstáculos
  int value1 = digitalRead(sensorPin1);  // Sensor infrarrojo 1
  int value2 = digitalRead(sensorPin2);  // Sensor infrarrojo 2

  // Si algún sensor detecta un obstáculo, detener el carrito
  if (value1 == HIGH || value2 == HIGH) {
    Serial.println("¡Obstáculo detectado! Deteniendo el carrito.");
    detenerCarrito();
    return;  // No continuar con comandos Bluetooth mientras haya un obstáculo
  }

  // Control por Bluetooth
  if (BT1.available() > 0) {
    byte numero = (byte)BT1.read();
    Serial.println(numero);

    int estado = -1;

    // Comandos Bluetooth
    if (numero == 83) estado = 0; // Avanzar
    if (numero == 87) estado = 1; // Reversa
    if (numero == 88) estado = 2; // Detenerse
    if (numero == 65) estado = 3; // Izquierda
    if (numero == 68) estado = 4; // Derecha

    // Si el comando es válido, actualizar motores
    if (estado != -1) {
      for (int i = 0; i < 4; i++) {
        digitalWrite(inputs[i], mestados[estado][i]);
        Serial.println(String(inputs[i]) + " estado: " + String(mestados[estado][i]));
      }

      for (int i = 0; i < 2; i++) {
        analogWrite(enables[i], velocidades[estado][i]);
        Serial.println(String(enables[i]) + " velocidad: " + String(velocidades[estado][i]));
      }
    }
  }
}

// Función para detener el carrito
void detenerCarrito() {
  for (int i = 0; i < 4; i++) {
    digitalWrite(inputs[i], mestados[2][i]);  // Usar el estado "detenerse"
  }
  for (int i = 0; i < 2; i++) {
    analogWrite(enables[i], velocidades[2][i]);
  }
}
