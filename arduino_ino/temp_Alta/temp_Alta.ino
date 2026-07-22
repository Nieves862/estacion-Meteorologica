#include "DHT.h"

// Definición de pines y tipo de sensor
#define DHTPIN 2        // Pin digital donde conectamos la señal (S) del DHT11
#define DHTTYPE DHT11   // Definimos que el sensor es un DHT11
const int pinLedAlerta = 13;

// Inicializamos el objeto del sensor dht
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  pinMode(pinLedAlerta, OUTPUT);
  Serial.begin(9600); // Iniciamos comunicación serie para la compu
  
  Serial.println("--- Iniciando Estacion Eco-Intelligence ---");
  dht.begin(); // Encendemos el sensor DHT11
}

void loop() {
  // El DHT11 es un sensor lento, esperamos 2 segundos entre lecturas
  delay(2000);

  // Leemos la humedad y la temperatura en Celsius
  float humedad = dht.readHumidity();
  float temperatura = dht.readTemperature();

  // Sistema de seguridad: Verificamos si el sensor está mal cableado o desconectado
  if (isnan(humedad) || isnan(temperatura)) {
    Serial.println("Error crítico: No se puede leer el sensor DHT11. Revisar cables.");
    return; // Sale del loop y vuelve a intentar
  }

  // Mostramos los datos reales en el Monitor Serie
  Serial.print("Humedad Ambiente: ");
  Serial.print(humedad);
  Serial.print(" % | ");
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" C");

  // Lógica de alerta: Si la temperatura supera los 30°C, encendemos el LED
  if (temperatura > 30) {
    digitalWrite(pinLedAlerta, HIGH);
  } else {
    digitalWrite(pinLedAlerta, LOW);
  }
}

