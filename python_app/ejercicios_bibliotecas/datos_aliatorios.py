import random

# Simulamos 5 mediciones de humedad
for i in range(5):
    humedad_simulada = random.randint(20, 100)
    print(f"Medición de prueba {i+1}: {humedad_simulada}%")

