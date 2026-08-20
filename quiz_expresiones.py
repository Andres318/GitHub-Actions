import json
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


def json_quiz(name, variable, expected):
    raw_value = env(variable)
    try:
        obtained = json.loads(raw_value)
        display_value = obtained
    except json.JSONDecodeError:
        obtained = raw_value
        display_value = f"JSON invalido: {raw_value}"

    correct = obtained == expected
    print(f"[Reto {name}]")
    print(f"resultado obtenido: {display_value}")
    print(f"resultado esperado: {expected}")
    print(f"estado: {'OK' if correct else 'INCORRECTO'}")
    print()
    return correct


def main():
    results = []

    results.append(quiz("1 - Nombre", env("QUIZ_NOMBRE"), "Ada Lovelace"))
    results.append(quiz("2 - Lenguaje", env("QUIZ_LENGUAJE"), "Python"))
    results.append(quiz("3 - Numero entero", env("QUIZ_NUMERO"), "42"))
    results.append(quiz("4 - Entorno", env("QUIZ_ENTORNO"), "production"))
    results.append(quiz("5 - Booleano", env("QUIZ_FUNCION"), "true"))

    results.append(quiz("6 - Hexadecimal convertido", env("QUIZ_HEXADECIMAL"), "26"))
    results.append(quiz("7 - Flotante calculado", env("QUIZ_FLOAT"), "3.14159"))

    nombre = env("QUIZ_NOMBRE")
    lenguaje = env("QUIZ_LENGUAJE")
    combinacion = f"{nombre} programa en {lenguaje}"
    results.append(
        quiz(
            "8 - Combinacion",
            combinacion,
            "Ada Lovelace programa en Python",
        )
    )

    results.append(
        json_quiz(
            "9 - fromJSON numero",
            "QUIZ_FROMJSON_NUMERO",
            100,
        )
    )
    results.append(
        json_quiz(
            "10 - fromJSON flotante",
            "QUIZ_FROMJSON_FLOAT",
            2.71828,
        )
    )
    results.append(
        json_quiz(
            "11 - fromJSON booleano",
            "QUIZ_FROMJSON_BOOLEANO",
            True,
        )
    )
    results.append(
        json_quiz(
            "12 - toJSON lista",
            "QUIZ_TOJSON_LISTA",
            ["Python", "GitHub Actions", "JSON"],
        )
    )
    results.append(
        json_quiz(
            "13 - toJSON objeto",
            "QUIZ_TOJSON_OBJETO",
            {
                "nombre": "Ada Lovelace",
                "lenguaje": "Python",
                "nivel": "avanzado",
            },
        )
    )

    total = len(results)
    correctas = sum(results)
    print(f"Resultado final: {correctas}/{total} retos correctos")

    if correctas != total:
        raise SystemExit("El quiz no fue completado correctamente")


if __name__ == "__main__":
    main()