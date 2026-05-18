import json


def cargar_cuentas():

    with open("parking/cuentas.json", "r", encoding="utf-8") as archivo:
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