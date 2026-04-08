# Importamos funcionalidades específicas de la biblioteca estándar
from random import uniform
from datetime import datetime

# 1. Simulamos la captura del sensor de la estación
# Generamos un número flotante (decimal) entre 15 y 35
temperatura = round(uniform(15.0, 35.0), 2)

# 2. Obtenemos la fecha y hora del sistema
ahora = datetime.now()

# Formateamos la hora para que sea legible (Hora:Minuto:Segundo)
hora_formateada = ahora.strftime("%H:%M:%S")

# 3. Resultado final (Lo que se enviaría luego a la DB)
print(f"Lectura guardada: {temperatura}°C a las {hora_formateada}")
