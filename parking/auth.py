import json
import os

def cargar_cuentas():
    ruta_base = os.path.dirname(__file__)
    ruta_cuentas = os.path.join(ruta_base, "cuentas.json")

    try:
        with open(ruta_cuentas, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Error crítico: No se encontró el archivo de configuración en {ruta_cuentas}.")
        return []
    except json.JSONDecodeError:
        print("Error crítico: El archivo cuentas.json posee un formato inválido.")
        return []


def iniciar_sesion():

    cuentas = cargar_cuentas()

    usuario_ingresado = input("Usuario: ").strip()

    if not usuario_ingresado:
        print("Debe ingresar un usuario.")
        return None

    password_ingresada = input("Contraseña: ").strip()

    if not password_ingresada:
        print("Debe ingresar una contraseña.")
        return None

    for cuenta in cuentas:

        if (
            cuenta["usuario"] == usuario_ingresado
            and cuenta["password"] == password_ingresada
        ):

            print("\nInicio de sesión exitoso\n")
            return cuenta

    print("\nUsuario o contraseña incorrectos\n")
    return None