"""
Lectura y escritura de archivos con manejo explícito de excepciones.

Incluye exportación/importación en JSON de los listados (diccionarios) en memoria.
"""

import json


def exportar_matrices_json(ruta, usuarios, vehiculos, estacionamiento):
    """Guarda usuarios, vehículos y estacionamiento en un único archivo JSON."""
    datos = {
        "usuarios": usuarios,
        "vehiculos": vehiculos,
        "estacionamiento": estacionamiento,
    }
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)
    except (OSError, TypeError) as exc:
        print(f"Error al exportar: {exc}")
        return False
    return True


def importar_matrices_json(ruta):
    """
    Carga los listados desde JSON. Devuelve (usuarios, vehiculos, estacionamiento)
    o None si falla la lectura o el formato.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
    except FileNotFoundError:
        print("No se encontró el archivo.")
        return None
    except json.JSONDecodeError:
        print("El archivo no tiene formato JSON válido.")
        return None
    except OSError as exc:
        print(f"Error al leer el archivo: {exc}")
        return None

    try:
        usuarios = datos["usuarios"]
        vehiculos = datos["vehiculos"]
        estacionamiento = datos["estacionamiento"]
    except (KeyError, TypeError):
        print('El archivo debe contener las claves "usuarios", "vehiculos" y "estacionamiento".')
        return None

    return usuarios, vehiculos, estacionamiento
