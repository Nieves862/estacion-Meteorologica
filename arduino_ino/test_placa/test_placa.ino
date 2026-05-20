  // C++

void setup() {
  // Inicializamos el pin 13 como salida (LED integrado 'L')
  pinMode(13, OUTPUT);
  
  // Inicializamos la comunicación serial a 9600 baudios
  Serial.begin(9600);
  
  Serial.println("--- INICIANDO TEST DE HARDWARE ---");
  Serial.println("Placa: Arduino UNO R3 detectada.");
}

void loop() {
  // Encendemos el LED
  digitalWrite(13, HIGH);
  Serial.println("[TEST] LED Interno: ENCENDIDO (HIGH)");
  delay(1000); // Esperamos 1 segundo

  // Apagamos el LED
  digitalWrite(13, LOW);
  Serial.println("[TEST] LED Interno: APAGADO (LOW)");
  delay(1000); // Esperamos 1 segundo
}

