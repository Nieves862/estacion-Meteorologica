from sensores import Sensor

# Creamos los objetos (Instanciación)
sensor_temp = Sensor("Temperatura", "A0")
sensor_hum = Sensor("Humedad", "A1")

# Usamos los métodos
sensor_temp.tomar_lectura()
sensor_hum.tomar_lectura()

from sensores import SensorAlerta

termometro = SensorAlerta("Termómetro ProA", "A0")
termometro.tomar_lectura()
termometro.verificar_alerta(30)

