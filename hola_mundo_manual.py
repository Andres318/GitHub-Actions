import os

# Lee la variable de entorno pasada desde GitHub Actions
lenguaje = os.getenv("LENGUAJE_PARAM", "No se ha definido la variable")
nombre = os.getenv("NOMBRE_PARAM", "No se ha definido la variable")

print(f"El lenguaje recibido es: {lenguaje}")
print(f"El nombre recibido es: {nombre}")
