# =====================================================================
# CLASE DE POO AVANZADA - PROYECTO ESTACIÓN METEOROLÓGICA
# =====================================================================

# 1. CLASE AUXILIAR PARA LA COLABORACIÓN
class Alerta:
    """Clase que colabora con la estación para clasificar el peligro"""
    def evaluar(self, temp):
        if temp >= 35:
            return "🔥 ALERTA: CALOR EXTREMO"
        elif temp <= 15:
            return "❄️ ALERTA: FRÍO EXTREMO"
        else:
            return "🟩 ESTADO: ÓPTIMO"
        
# 2. CLASE BASE (PADRE)
class EstacionBase:
    # --- VARIABLE DE CLASE ---
    institucion = "Escuela Experimental PRoA Sede Río Tercero"
    unidad_medida = "°C"
    def __init__(self, nombre, temperatura):
        self.nombre = nombre
        self.temperatura = temperatura
        # --- COLABORACIÓN DE CLASES ---
        # Guardamos un objeto de la clase Alerta dentro de nuestro atributo
        self.procesador_alertas = Alerta()
    # --- MÉTODO ESPECIAL __str__ ---
    def __str__(self):
        """Define cómo se imprime el objeto en consola"""
        diagnostico = self.procesador_alertas.evaluar(self.temperatura)
        return f"📡 [{self.institucion}] - {self.nombre}\n🌡️  Temperatura: {self.temperatura}{self.unidad_medida}\n📢 Diagnóstico: {diagnostico}"
    # --- REDEFINICIÓN DE OPERADORES MATEMÁTICOS (+) ---
    def __add__(self, otra_estacion):
        """Permite sumar las temperaturas de dos estaciones: estacion1 + estacion2"""
        return self.temperatura + otra_estacion.temperatura
    # --- REDEFINICIÓN DE OPERADORES RELACIONALES (>) ---
    def __gt__(self, otra_estacion):
        """Permite comparar cuál estación tiene mayor temperatura: estacion1 > estacion2"""
        return self.temperatura > otra_estacion.temperatura
    
# 3. HERENCIA (CLASE HIJA)
class EstacionAvanzada(EstacionBase):
    """Hereda todo de EstacionBase pero le agrega la variable Humedad"""
    def __init__(self, nombre, temperatura, humedad):
        # Invocamos al constructor del padre para no repetir código (super)
        super().__init__(nombre, temperatura)
        self.humedad = humedad
    # Redefinimos el __str__ del padre para agregarle el dato de humedad
    def __str__(self):
        reporte_padre = super().__str__() # Trae lo que armó el padre
        return f"{reporte_padre}\n💧 Humedad: {self.humedad}%"
# =====================================================================
# 🧪 PRUEBA DEL HARDWARE
# =====================================================================
if __name__ == "__main__":
    print("=== PROBANDO NUESTROS OBJETOS METEOROLÓGICOS ===")
    # Instanciamos dos estaciones (una Base y una Avanzada con Herencia)
    estacion_aula = EstacionBase("Sensor Aula 5to", 37)
    estacion_patio = EstacionAvanzada("Sensor Patio Principal", 22, 65)
    # 1. Probando el método especial __str__ y la Colaboración con Alerta
    print("\n--- 📝 Reporte Estación 1 (Base):")
    print(estacion_aula)     
    print("\n--- 📝 Reporte Estación 2 (Heredada/Avanzada):")
    print(estacion_patio)
    print("\n" + "="*40)
    print("🚀 DEMOSTRACIÓN DE REDEFINICIÓN DE OPERADORES")
    print("="*40)
    # 2. Probando la Redefinición del operador Matemático (+)
    suma_temperaturas = estacion_aula + estacion_patio
    promedio = suma_temperaturas / 2
    print(f"➕ Suma de temperaturas de ambos bancos de trabajo: {suma_temperaturas}°C")
    print(f"📊 Promedio térmico del colegio: {promedio}°C")
    # 3. Probando la Redefinición del operador Relacional (>)
    if estacion_aula > estacion_patio:
        print(f"\n🚩 ¡Alerta! El objeto '{estacion_aula.nombre}' registra más calor que '{estacion_patio.nombre}'.")
    else:
        print(f"\n🚩 El objeto '{estacion_patio.nombre}' tiene mayor o igual temperatura.")
