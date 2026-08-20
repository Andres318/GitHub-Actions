import os


def env(name):
    return os.getenv(name, "NO_DEFINIDO")


def quiz(name, obtained, expected):
    correct = obtained == expected
    print(f"[Reto {name}]")
    print(f"resultado obtenido: {obtained}")
    print(f"resultado esperado: {expected}")
    print(f"estado: {'OK' if correct else 'INCORRECTO'}")
    print()
    return correct


def main():
    results = []

    results.append(quiz("1 - Nombre", env("QUIZ_NOMBRE"), "Ada Lovelace"))
    results.append(quiz("2 - Lenguaje", env("QUIZ_LENGUAJE"), "Python"))
    results.append(quiz("3 - Numero", env("QUIZ_NUMERO"), "42"))
    results.append(quiz("4 - Entorno", env("QUIZ_ENTORNO"), "production"))
    results.append(quiz("5 - Funcion habilitada", env("QUIZ_FUNCION"), "true"))

    nombre = env("QUIZ_NOMBRE")
    lenguaje = env("QUIZ_LENGUAJE")
    combinacion = f"{nombre} programa en {lenguaje}"
    results.append(
        quiz(
            "6 - Combinacion",
            combinacion,
            "Ada Lovelace programa en Python",
        )
    )

    total = len(results)
    correctas = sum(results)
    print(f"Resultado final: {correctas}/{total} retos correctos")

    if correctas != total:
        raise SystemExit("El quiz no fue completado correctamente")


if __name__ == "__main__":
    main()