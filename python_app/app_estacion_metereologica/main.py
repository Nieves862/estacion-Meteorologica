import serial
import mysql.connector
import sys

class EstacionReceptora:
    # Constructor: Define qué necesita la clase para dar vida al objeto
    def __init__(self, puerto_com, baudios, db_host, db_user, db_pass, db_name, db_port=3306):
        self.puerto_com = puerto_com
        self.baudios = baudios                
        try:
            # Intentamos conectar con el hardware (Arduino)
            self.arduino = serial.Serial(puerto_com, baudios, timeout=1)                    
            # Intentamos conectar con la Base de Datos (MySQL) utilizando las variables del constructor
            self.db = mysql.connector.connect(
                host=db_host,
                user=db_user,
                password=db_pass,
                database=db_name,
                port=db_port
            )
            self.cursor = self.db.cursor()
            print(f"📡 Objeto Estación creado. Conectado a {puerto_com} y MySQL con éxito.")            
        except serial.SerialException:
            print(f"❌ ERROR CRÍTICO: No se pudo abrir el puerto {puerto_com}. Verificá que no esté abierto el Monitor Serie de Arduino IDE.")
            sys.exit()
        except mysql.connector.Error as err:
            print(f"❌ ERROR CRÍTICO EN MYSQL: {err}")
            sys.exit()
            
    # Método: Escucha el puerto USB en tiempo real y procesa el texto
    def recibir_y_guardar(self):
        # Leer línea desde el cable USB (vienen bytes, decodificamos a texto)
        linea = self.arduino.readline().decode('utf-8').strip()        
        
        # Este print te muestra lo que viaja por el cable (lo podés dejar o borrar)
        if linea:
            print(f"➔ Texto crudo recibido del USB: '{linea}'")
            
        # Condición principal: Si hay datos y no es un mensaje de "ERROR" de Arduino
        if linea and "ERROR" not in linea:
            
            # 📌 AQUÍ VA EL BLOQUE TRY
            try:
                # El Arduino envía: "64.00,23.30" -> Lo dividimos por la coma
                datos = linea.split(',')
                
                # Convertimos primero a float (porque viene con punto) y luego a int (entero)
                humedad_act = int(float(datos[0]))      # Traduce '64.00' -> 64.0 -> 64
                temperatura_act = int(float(datos[1]))  # Traduce '23.30' -> 23.3 -> 23             
                
                # Ejecutamos el método interno para insertar en MySQL
                self.__insertar_en_db(temperatura_act, humedad_act)                
                print(f"🟩 [NUEVA MEDICIÓN] Humedad: {humedad_act}% | Temp: {temperatura_act}°C ➔ ¡Guardado exitosamente!")
            
            # El except va justo al terminar el try para atrapar fallos si un dato viene roto
            except (ValueError, IndexError) as e:
                print(f"⚠️ Error de procesamiento: {e}")      
            
    # Método privado: Se encarga exclusivamente del SQL (Encapsulamiento)
    def __insertar_en_db(self, temp, hum):
        sql = "INSERT INTO mediciones (temperatura, humedad) VALUES (%s, %s)"
        self.cursor.execute(sql, (temp, hum))
        self.db.commit() # Confirmamos el guardado en el disco rígido

# --- EJECUCIÓN DEL PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    # Instanciamos el objeto 'mi_estacion' pasándole los datos de configuración reales
    mi_estacion = EstacionReceptora(
        puerto_com='COM3',                      		    # Revisar puerto en cada compu
        baudios=9600, 
        db_host='127.0.0.1',                     		    # localhost
        db_user='root', 
        db_pass='root',                          			# Contraseña local de MySQL
        db_name='estacionmetereologica_proa',               # Tu esquema de base de datos
        db_port=3306
    )
    
    print("🚀 Iniciando monitoreo continuo... Presioná Ctrl+C para detener.")       
    # Bucle infinito de escucha utilizando el método del objeto
    try:
        while True:
            mi_estacion.recibir_y_guardar()
    except KeyboardInterrupt:
        print("\n🛑 Monitoreo detenido por el usuario. Conexiones cerradas.")
        
        