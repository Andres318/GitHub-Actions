from datetime import datetime, timezone
import os
import platform


def main():
    now_utc = datetime.now(timezone.utc)
    now_local = datetime.now()

    print("=== Verificación de cron en GitHub Actions ===")
    print(f"Timestamp UTC: {now_utc.isoformat()}")
    print(f"Fecha local: {now_local.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Python version: {platform.python_version()}")
    print(f"Repositorio: {os.getenv('GITHUB_REPOSITORY', 'No disponible')}")
    print(f"Evento: {os.getenv('GITHUB_EVENT_NAME', 'manual')}")
    print("Estado del cron: funcionando correctamente")

    datos = {
        "cron_status": "ok",
        "workflow": "github-actions-cron",
        "mensaje": "El cron está ejecutándose correctamente.",
    }

    for clave, valor in datos.items():
        print(f"{clave}: {valor}")


if __name__ == "__main__":
    main()
