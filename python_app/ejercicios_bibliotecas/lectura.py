import platform

sistema = platform.system()
procesador = platform.processor()

print(f"La estación está corriendo en: {sistema}")
print(f"Tipo de procesador: {procesador}")
