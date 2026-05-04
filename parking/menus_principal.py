from parking.constantes import (
    ESTACIONAMIENTO_INICIAL,
    USUARIOS_INICIAL,
    VEHICULOS_INICIAL,
)
from parking import facturacion
from parking import gestion_cupos
from parking import ordenamiento
from parking import usuarios
from parking import vehiculos


def ejecutar_aplicacion():
    lista_usuarios = [dict(u) for u in USUARIOS_INICIAL]
    lista_vehiculos = [dict(v) for v in VEHICULOS_INICIAL]
    lista_estacionamiento = [dict(e) for e in ESTACIONAMIENTO_INICIAL]

    try:
        _bucle_principal(lista_usuarios, lista_vehiculos, lista_estacionamiento)
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario (Ctrl+C). Fin.")


def _bucle_principal(lista_usuarios, lista_vehiculos, lista_estacionamiento):
    while True:
        while True:
            opciones = 6
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de usuarios")
            print("[2] Gestión de vehículos")
            print("[3] Gestión de estacionamiento")
            print("[4] Listado general (usuarios, vehículos, estacionamiento)")
            print("[5] Ordenar un listado por campo")
            print("[6] Facturación / reportes")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()

            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones + 1)]:
                break
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0":
            print("Fin del programa.")
            return

        if opcion == "1":
            while True:
                while True:
                    sub_opciones = 5
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > USUARIOS")
                    print("---------------------------")
                    print("[1] Alta de usuario")
                    print("[2] Listar usuarios")
                    print("[3] Consultar usuario por ID")
                    print("[4] Modificar usuario")
                    print("[5] Baja de usuario")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()

                    sub = input("Seleccione una opción: ")
                    if sub in [str(i) for i in range(0, sub_opciones + 1)]:
                        break
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if sub == "0":
                    break
                if sub == "1":
                    usuarios.alta_usuario(lista_usuarios)
                elif sub == "2":
                    usuarios.listar_usuarios(lista_usuarios)
                elif sub == "3":
                    usuarios.consultar_usuario(lista_usuarios)
                elif sub == "4":
                    usuarios.modificar_usuario(lista_usuarios)
                elif sub == "5":
                    usuarios.baja_usuario(lista_usuarios)

                input("\nPresione ENTER para continuar.")

        elif opcion == "2":
            while True:
                while True:
                    sub_opciones = 3
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > VEHÍCULOS")
                    print("---------------------------")
                    print("[1] Alta de vehículo")
                    print("[2] Listar vehículos")
                    print("[3] Baja de vehículo")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()

                    sub = input("Seleccione una opción: ")
                    if sub in [str(i) for i in range(0, sub_opciones + 1)]:
                        break
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if sub == "0":
                    break
                if sub == "1":
                    vehiculos.alta_vehiculo(lista_vehiculos, lista_usuarios)
                elif sub == "2":
                    vehiculos.listar_vehiculos(lista_vehiculos)
                elif sub == "3":
                    vehiculos.baja_vehiculo(lista_vehiculos, lista_estacionamiento)

                input("\nPresione ENTER para continuar.")

        elif opcion == "3":
            while True:
                while True:
                    sub_opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > ESTACIONAMIENTO")
                    print("(Piso 1: motos | Piso 2: autos | Piso 3: camionetas)")
                    print("---------------------------")
                    print("[1] Asignar cupo")
                    print("[2] Listar cupos ocupados")
                    print("[3] Liberar cupo")
                    print("[4] Consultar cupo")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()

                    sub = input("Seleccione una opción: ")
                    if sub in [str(i) for i in range(0, sub_opciones + 1)]:
                        break
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if sub == "0":
                    break
                if sub == "1":
                    gestion_cupos.asignar_cupo(lista_vehiculos, lista_estacionamiento)
                elif sub == "2":
                    gestion_cupos.listar_estacionamiento(lista_estacionamiento)
                elif sub == "3":
                    gestion_cupos.liberar_cupo(lista_estacionamiento)
                elif sub == "4":
                    gestion_cupos.consultar_cupo(lista_estacionamiento, lista_vehiculos)

                input("\nPresione ENTER para continuar.")

        elif opcion == "4":
            print("\n--- USUARIOS ---")
            usuarios.listar_usuarios(lista_usuarios)
            print("\n--- VEHÍCULOS ---")
            vehiculos.listar_vehiculos(lista_vehiculos)
            print("\n--- ESTACIONAMIENTO (ocupados) ---")
            gestion_cupos.listar_estacionamiento(lista_estacionamiento)

        elif opcion == "5":
            ordenamiento.flujo_ordenar_matriz(lista_usuarios, lista_vehiculos, lista_estacionamiento)

        elif opcion == "6":
            facturacion.menu_facturacion_y_lambdas(
                lista_usuarios, lista_vehiculos, lista_estacionamiento
            )

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")
