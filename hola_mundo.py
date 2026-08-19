import os

def main():
    nombre = os.getenv("USERNAME", "No se ha definido la variable de entorno USERNAME")
    print(f"¡Hola, {nombre} desde GitHub!")


if __name__ == "__main__":
    main()