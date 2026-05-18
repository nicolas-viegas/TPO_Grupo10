"""
-----------------------------------------------------------------------------------------------
Título: Sistema de estacionamiento — TP Programación I
Fecha: Abril 2026
Autor: Grupo 10

Descripción:
    Estacionamiento con 3 pisos: 1 motos, 2 autos, 3 camionetas (15 cupos por piso).
    Lógica modular en el paquete `parking` (constantes, utilidades, CRUD, cupos,
    ordenamiento por campo, reportes). Los datos son listas de diccionarios. Incluye
    manejo de excepciones para entradas
    inválidas, división por cero, interrupción del usuario y operaciones de archivo.
    Punto de entrada: main().
-----------------------------------------------------------------------------------------------
"""

"""
-----------------------------------------------------------------------
Título: Sistema de estacionamiento — TP Programación I
Fecha: Abril 2026
Autor: Grupo 10
-----------------------------------------------------------------------
"""

from parking.auth import iniciar_sesion
from parking.menus_principal import ejecutar_aplicacion


def main():

    while True:

        usuario_logueado = iniciar_sesion()

        if usuario_logueado:
            ejecutar_aplicacion(usuario_logueado)
            break

        else:
            print("\nAcceso denegado. Intente nuevamente.\n")


if __name__ == "__main__":
    main()