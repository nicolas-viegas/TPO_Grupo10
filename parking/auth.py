import json
import os


def cargar_cuentas():

    ruta_base = os.path.dirname(__file__)

    ruta_cuentas = os.path.join(ruta_base, "cuentas.json")

    with open(ruta_cuentas, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def iniciar_sesion():

    cuentas = cargar_cuentas()

    usuario_ingresado = input("Usuario: ")
    password_ingresada = input("Contraseña: ")

    for cuenta in cuentas:

        if (
            cuenta["usuario"] == usuario_ingresado
            and cuenta["password"] == password_ingresada
        ):

            print("\nInicio de sesión exitoso\n")
            return cuenta

    print("\nUsuario o contraseña incorrectos\n")
    return None