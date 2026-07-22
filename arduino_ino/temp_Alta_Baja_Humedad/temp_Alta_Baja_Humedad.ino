// C++
#include "DHT.h"
#define DHTPIN 2        // Pin digital de señal del DHT11
#define DHTTYPE DHT11   // Tipo de sensor
const int pinLedCalor = 13; // LED Rojo (Opción 1 - Alertas Altas)
const int pinLedFrio = 12;  // LED Azul (Opción 2 - Alertas Bajas)
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  pinMode(pinLedCalor, OUTPUT);
  pinMode(pinLedFrio, OUTPUT);
  Serial.begin(9600);  
  Serial.println("--- Estación Eco-Intelligence: Temp Altas , Bajas y Humedad Activas ---");
  dht.begin();
}

void loop() {
  // El DHT11 requiere un tiempo de estabilidad de 2 segundos
  delay(2000); 
  // Capturamos las dos variables solicitadas
  float humedad = dht.readHumidity();       // Humedad Ambiente
  float temperatura = dht.readTemperature(); // Temperatura (C)
  // Control de cables sueltos o errores de lectura física
  if (isnan(humedad) || isnan(temperatura)) {
    Serial.println("Error de lectura: Revisar conexiones del DHT11");
    return;
  }

  // --- "IMPRESIÓN EN MONITOR SERIAL" ---
  
  // Enviamos los datos puros. Ejemplo de lo que viajará por el cable: 86,12
  Serial.print(humedad);
  Serial.print(",");
  Serial.println(temperatura);  

  // --- LÓGICA DE CONTROL MULTICONDICIONAL ---
  if (temperatura > 30) {
    // Opción 1: Alerta de Temperatura Alta
    digitalWrite(pinLedCalor, HIGH);
    digitalWrite(pinLedFrio, LOW);
  } 
  else if (temperatura < 15) {
    // Opción 2: Alerta de Temperatura Baja
    digitalWrite(pinLedCalor, LOW);
    digitalWrite(pinLedFrio, HIGH);
  } 
  else {
    // Estado Óptimo: Temperatura ambiente normal (ambos apagados)
    digitalWrite(pinLedCalor, LOW);
    digitalWrite(pinLedFrio, LOW);
  }
}

