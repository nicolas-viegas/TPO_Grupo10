"""
-----------------------------------------------------------------------------------------------
Título: Sistema de estacionamiento — TP Programación I
Fecha: Abril 2026
Autor: Grupo 10

Descripción:
    Estacionamiento con 3 pisos: 1 motos, 2 autos, 3 camionetas (5 cupos por piso).
    Lógica modular en el paquete `parking` (constantes, utilidades, CRUD, cupos,
    ordenamiento por campo, reportes). Los datos son listas de diccionarios. Incluye
    manejo de excepciones para entradas
    inválidas, división por cero, interrupción del usuario y operaciones de archivo.
    Punto de entrada: main().
-----------------------------------------------------------------------------------------------
"""

from parking.menus_principal import ejecutar_aplicacion


def main():
    ejecutar_aplicacion()


if __name__ == "__main__":
    main()
