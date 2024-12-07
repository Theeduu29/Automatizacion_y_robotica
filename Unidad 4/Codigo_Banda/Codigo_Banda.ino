int in1 = 7;   // Pin para controlar la dirección 1
int in2 = 8;   // Pin para controlar la dirección 2
int enA = 9;   // Pin para la velocidad del motor (PWM)

void setup() {
    pinMode(in1, OUTPUT);
    pinMode(in2, OUTPUT);
    pinMode(enA, OUTPUT);
}

void loop() {
    // Movimiento hacia adelante
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    analogWrite(enA, 200);  // Velocidad media

    delay(5000);  // Ejecutar por 5 segundos

    // Parar la banda
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    delay(2000);

    // Movimiento hacia atrás
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    analogWrite(enA, 150);  // Velocidad baja

    delay(5000);

    // Parar la banda
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    delay(2000);
}
