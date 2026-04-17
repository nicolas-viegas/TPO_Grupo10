from parking.constantes import (
    MATRIZ_ESTACIONAMIENTO,
    MATRIZ_USUARIOS,
    MATRIZ_VEHICULOS,
)
from parking import facturacion
from parking import gestion_cupos
from parking import ordenamiento
from parking import usuarios
from parking import vehiculos


def ejecutar_aplicacion():
    usuarios_mat = [fila[:] for fila in MATRIZ_USUARIOS]
    vehiculos_mat = [fila[:] for fila in MATRIZ_VEHICULOS]
    estacionamiento_mat = [fila[:] for fila in MATRIZ_ESTACIONAMIENTO]

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
            print("[4] Listado general (todas las matrices)")
            print("[5] Ordenar una matriz por columna")
            print("[6] Facturación / reportes sobre matrices")
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
                    usuarios.alta_usuario(usuarios_mat)
                elif sub == "2":
                    usuarios.listar_usuarios(usuarios_mat)
                elif sub == "3":
                    usuarios.consultar_usuario(usuarios_mat)
                elif sub == "4":
                    usuarios.modificar_usuario(usuarios_mat)
                elif sub == "5":
                    usuarios.baja_usuario(usuarios_mat)

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
                    vehiculos.alta_vehiculo(vehiculos_mat, usuarios_mat)
                elif sub == "2":
                    vehiculos.listar_vehiculos(vehiculos_mat)
                elif sub == "3":
                    vehiculos.baja_vehiculo(vehiculos_mat, estacionamiento_mat)

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
                    gestion_cupos.asignar_cupo(vehiculos_mat, estacionamiento_mat)
                elif sub == "2":
                    gestion_cupos.listar_estacionamiento(estacionamiento_mat)
                elif sub == "3":
                    gestion_cupos.liberar_cupo(estacionamiento_mat)
                elif sub == "4":
                    gestion_cupos.consultar_cupo(estacionamiento_mat, vehiculos_mat)

                input("\nPresione ENTER para continuar.")

        elif opcion == "4":
            print("\n--- USUARIOS ---")
            usuarios.listar_usuarios(usuarios_mat)
            print("\n--- VEHÍCULOS ---")
            vehiculos.listar_vehiculos(vehiculos_mat)
            print("\n--- ESTACIONAMIENTO (ocupados) ---")
            gestion_cupos.listar_estacionamiento(estacionamiento_mat)

        elif opcion == "5":
            ordenamiento.flujo_ordenar_matriz(usuarios_mat, vehiculos_mat, estacionamiento_mat)

        elif opcion == "6":
            facturacion.menu_facturacion_y_lambdas(vehiculos_mat, estacionamiento_mat)

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")
