from datetime import datetime
import random
import time

# Simulamos un ciclo de 5 mediciones
print("--- Iniciando Registro de la Estación Meteorológica ---")

for i in range(5):
    # 1. Capturamos la hora exacta
    ahora = datetime.now()
    hora_formateada = ahora.strftime("%H:%M:%S")
    
    # 2. Simulamos el dato del sensor de humedad
    humedad = random.randint(30, 90)
    
    # 3. Mostramos el reporte combinado
    print(f"[{i+1}] A las {hora_formateada} la humedad es de {humedad}%")
    
    # 4. Esperamos 2 segundos entre mediciones para que no sea instantáneo
    time.sleep(2)

print("--- Registro finalizado ---")
