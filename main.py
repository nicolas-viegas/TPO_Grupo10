"""
-----------------------------------------------------------------------------------------------
Título: Sistema de estacionamiento — TP Programación I
Fecha: Abril 2026
Autor: Grupo 10

Descripción:
    Estacionamiento con 3 pisos: 1 motos, 2 autos, 3 camionetas (30 cupos por piso).
    Matrices: usuarios, vehículos, estacionamiento.
    Primera entrega: datos ficticios hardcodeados, menú y CRUD de usuarios.


Pendientes:
    Facturación y funciones lambda para facturación.
-----------------------------------------------------------------------------------------------
"""

# ----------------------------------------------------------------------------------------------
# MÓDULOS
# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------
# CONSTANTES
# ----------------------------------------------------------------------------------------------
CUPOS_POR_PISO = 30
PISO_MOTOS = 1
PISO_AUTOS = 2
PISO_CAMIONETAS = 3

TARIFA_MENSUAL_MOTO = 50000
TARIFA_MENSUAL_AUTO = 70000
TARIFA_MENSUAL_CAMIONETA = 100000


# usuarios: [id_usuario, nombre, apellido, dni]
MATRIZ_USUARIOS = [
    [1, "Ana", "García", "28111222"],
    [2, "Luis", "Rodríguez", "35111222"],
    [3, "María", "Fernández", "40111222"],
    [4, "Pedro", "López", "20999888"],
]

# vehículos: [id_vehiculo, patente, tipo, id_usuario, tarifa_mensual]
# tipo: "moto" | "auto" | "camioneta"
MATRIZ_VEHICULOS = [
    [1, "AB123CD", "moto", 1, TARIFA_MENSUAL_MOTO],
    [2, "XY987ZZ", "auto", 1, TARIFA_MENSUAL_AUTO],
    [3, "AA000BB", "camioneta", 2, TARIFA_MENSUAL_CAMIONETA],
    [4, "MOTO99", "moto", 3, TARIFA_MENSUAL_MOTO],
    [5, "CD456EF", "auto", 4, TARIFA_MENSUAL_AUTO],
]

# estacionamiento: [piso, nro_estacionamiento (1-30), id_vehiculo que ocupa el cupo]
MATRIZ_ESTACIONAMIENTO = [
    [1, 5, 1],
    [1, 12, 4],
    [2, 3, 2],
    [2, 18, 5],
    [3, 1, 3],
]


# ----------------------------------------------------------------------------------------------
# FUNCIONES AUXILIARES
# ----------------------------------------------------------------------------------------------
def siguiente_id_usuario(usuarios):
    if not usuarios:
        return 1
    return max(fila[0] for fila in usuarios) + 1


def buscar_usuario_por_id(usuarios, id_usuario):
    for fila in usuarios:
        if fila[0] == id_usuario:
            return fila
    return None


def tarifa_mensual_por_tipo(tipo):
    if tipo == "moto":
        return TARIFA_MENSUAL_MOTO
    if tipo == "auto":
        return TARIFA_MENSUAL_AUTO
    if tipo == "camioneta":
        return TARIFA_MENSUAL_CAMIONETA
    return None


def siguiente_id_vehiculo(vehiculos):
    if not vehiculos:
        return 1
    return max(fila[0] for fila in vehiculos) + 1


def buscar_vehiculo_por_patente(vehiculos, patente):
    p = patente.strip().upper()
    for fila in vehiculos:
        if fila[1].strip().upper() == p:
            return fila
    return None


def buscar_vehiculo_por_id(vehiculos, id_vehiculo):
    for fila in vehiculos:
        if fila[0] == id_vehiculo:
            return fila
    return None


def piso_para_tipo(tipo):
    if tipo == "moto":
        return PISO_MOTOS
    if tipo == "auto":
        return PISO_AUTOS
    if tipo == "camioneta":
        return PISO_CAMIONETAS
    return None


def indice_cupo_piso_y_numero(estacionamiento, piso, nro_cupo):
    for i, e in enumerate(estacionamiento):
        if e[0] == piso and e[1] == nro_cupo:
            return i
    return None


def indice_cupo_por_id_vehiculo(estacionamiento, id_vehiculo):
    for i, e in enumerate(estacionamiento):
        if e[2] == id_vehiculo:
            return i
    return None


def primer_cupo_libre_en_piso(estacionamiento, piso):
    ocupados = {e[1] for e in estacionamiento if e[0] == piso}
    for n in range(1, CUPOS_POR_PISO + 1):
        if n not in ocupados:
            return n
    return None


def entero_positivo_desde_cadena(cadena):
    t = cadena.strip()
    if not t or not t.isdigit():
        return None
    return int(t)


# ----------------------------------------------------------------------------------------------
# CRUD USUARIOS
# ----------------------------------------------------------------------------------------------
def listar_usuarios(usuarios):
    if not usuarios:
        print("No hay usuarios cargados.")
        return
    print()
    print("ID | Nombre      | Apellido    | DNI")
    print("-" * 45)
    for u in usuarios:
        print(f"{u[0]:2} | {u[1]:11} | {u[2]:11} | {u[3]}")


def alta_usuario(usuarios):
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    dni = input("DNI: ").strip()
    if not nombre or not apellido or not dni:
        print("Error: todos los campos son obligatorios.")
        return usuarios
    nuevo_id = siguiente_id_usuario(usuarios)
    usuarios.append([nuevo_id, nombre, apellido, dni])
    print(f"Usuario dado de alta. ID asignado: {nuevo_id}")
    return usuarios


def consultar_usuario(usuarios):
    id_buscar = entero_positivo_desde_cadena(input("Ingrese ID de usuario: "))
    if id_buscar is None:
        print("ID inválido.")
        return
    u = buscar_usuario_por_id(usuarios, id_buscar)
    if u is None:
        print("No existe un usuario con ese ID.")
    else:
        print(f"ID: {u[0]} | {u[1]} {u[2]} | DNI: {u[3]}")


def modificar_usuario(usuarios):
    id_buscar = entero_positivo_desde_cadena(input("Ingrese ID de usuario a modificar: "))
    if id_buscar is None:
        print("ID inválido.")
        return usuarios
    u = buscar_usuario_por_id(usuarios, id_buscar)
    if u is None:
        print("No existe un usuario con ese ID.")
        return usuarios
    print("(Deje vacío para no cambiar el campo.)")
    nombre = input(f"Nombre [{u[1]}]: ").strip()
    apellido = input(f"Apellido [{u[2]}]: ").strip()
    dni = input(f"DNI [{u[3]}]: ").strip()
    if nombre:
        u[1] = nombre
    if apellido:
        u[2] = apellido
    if dni:
        u[3] = dni
    print("Usuario actualizado.")
    return usuarios


def baja_usuario(usuarios):
    id_buscar = entero_positivo_desde_cadena(input("Ingrese ID de usuario a eliminar: "))
    if id_buscar is None:
        print("ID inválido.")
        return usuarios
    for i, fila in enumerate(usuarios):
        if fila[0] == id_buscar:
            confirmar = input(f"¿Eliminar a {fila[1]} {fila[2]}? (s/n): ").strip().lower()
            if confirmar == "s":
                usuarios.pop(i)
                print("Usuario eliminado.")
            else:
                print("Operación cancelada.")
            return usuarios
    print("No existe un usuario con ese ID.")
    return usuarios


# ----------------------------------------------------------------------------------------------
# VEHÍCULOS Y ESTACIONAMIENTO
# ----------------------------------------------------------------------------------------------
def listar_vehiculos(vehiculos):
    if not vehiculos:
        print("No hay vehículos cargados.")
        return
    print()
    print("ID veh. | Patente   | Tipo      | ID usr | $ mensual")
    print("-" * 55)
    for v in vehiculos:
        tarifa = v[4] if len(v) > 4 else "-"
        print(f"{v[0]:7} | {v[1]:9} | {v[2]:9} | {v[3]:6} | {tarifa:9}")


def alta_vehiculo(vehiculos, usuarios):
    patente = input("Patente: ").strip().upper()
    if not patente:
        print("Error: la patente es obligatoria.")
        return vehiculos
    if buscar_vehiculo_por_patente(vehiculos, patente) is not None:
        print("Error: ya existe un vehículo con esa patente.")
        return vehiculos

    print("Tipo: [1] moto  [2] auto  [3] camioneta")
    ingresar_tipo = input("Seleccione tipo: ").strip()
    if ingresar_tipo == "1":
        tipo = "moto"
    elif ingresar_tipo == "2":
        tipo = "auto"
    elif ingresar_tipo == "3":
        tipo = "camioneta"
    else:
        print("Error: tipo inválido.")
        return vehiculos

    id_usuario = entero_positivo_desde_cadena(input("ID de usuario (titular): "))
    if id_usuario is None:
        print("Error: ID de usuario inválido.")
        return vehiculos
    if buscar_usuario_por_id(usuarios, id_usuario) is None:
        print("Error: no existe un usuario con ese ID.")
        return vehiculos

    tarifa = tarifa_mensual_por_tipo(tipo)
    nuevo_id = siguiente_id_vehiculo(vehiculos)
    vehiculos.append([nuevo_id, patente, tipo, id_usuario, tarifa])
    print(f"Vehículo dado de alta. ID: {nuevo_id}. Tarifa mensual: ${tarifa}")
    return vehiculos


def baja_vehiculo(vehiculos, estacionamiento):
    id_buscar = entero_positivo_desde_cadena(input("Ingrese ID de vehículo a eliminar: "))
    if id_buscar is None:
        print("ID inválido.")
        return vehiculos, estacionamiento
    v = buscar_vehiculo_por_id(vehiculos, id_buscar)
    if v is None:
        print("No existe un vehículo con ese ID.")
        return vehiculos, estacionamiento

    confirmar = input(f"¿Eliminar vehículo {v[1]} ({v[2]})? (s/n): ").strip().lower()
    if confirmar != "s":
        print("Operación cancelada.")
        return vehiculos, estacionamiento

    idx_est = indice_cupo_por_id_vehiculo(estacionamiento, id_buscar)
    if idx_est is not None:
        estacionamiento.pop(idx_est)

    for i, fila in enumerate(vehiculos):
        if fila[0] == id_buscar:
            vehiculos.pop(i)
            break
    print("Vehículo eliminado.")
    return vehiculos, estacionamiento


def listar_estacionamiento(estacionamiento):
    if not estacionamiento:
        print("No hay cupos ocupados registrados.")
        return
    print()
    print("Piso | Nro cupo | ID vehículo")
    print("-" * 35)
    for e in estacionamiento:
        print(f"{e[0]:4} | {e[1]:8} | {e[2]}")


def asignar_cupo(vehiculos, estacionamiento):
    id_v = entero_positivo_desde_cadena(input("ID de vehículo a estacionar: "))
    if id_v is None:
        print("ID inválido.")
        return estacionamiento
    v = buscar_vehiculo_por_id(vehiculos, id_v)
    if v is None:
        print("No existe un vehículo con ese ID.")
        return estacionamiento

    if indice_cupo_por_id_vehiculo(estacionamiento, id_v) is not None:
        print("Ese vehículo ya tiene un cupo asignado. Libérelo antes de reasignar.")
        return estacionamiento

    piso = piso_para_tipo(v[2])
    nro = primer_cupo_libre_en_piso(estacionamiento, piso)
    if nro is None:
        print(f"No hay cupos libres en el piso {piso} (máximo {CUPOS_POR_PISO} por piso).")
        return estacionamiento

    estacionamiento.append([piso, nro, id_v])
    print(
        f"Vehículo tipo «{v[2]}» → piso {piso}. "
        f"Cupo asignado automáticamente: lugar {nro} (vehículo ID {id_v})."
    )
    return estacionamiento


def liberar_cupo(estacionamiento):
    print("Modo: [1] por piso y número de cupo  [2] por ID de vehículo")
    modo = input("Seleccione: ").strip()
    idx = None
    if modo == "1":
        piso = entero_positivo_desde_cadena(input("Piso (1-3): "))
        nro = entero_positivo_desde_cadena(input(f"Número de cupo (1-{CUPOS_POR_PISO}): "))
        if piso is None or piso < 1 or piso > 3 or nro is None or nro < 1 or nro > CUPOS_POR_PISO:
            print("Datos inválidos.")
            return estacionamiento
        idx = indice_cupo_piso_y_numero(estacionamiento, piso, nro)
        if idx is None:
            print("No hay vehículo en ese cupo.")
            return estacionamiento
    elif modo == "2":
        id_v = entero_positivo_desde_cadena(input("ID de vehículo: "))
        if id_v is None:
            print("ID inválido.")
            return estacionamiento
        idx = indice_cupo_por_id_vehiculo(estacionamiento, id_v)
        if idx is None:
            print("Ese vehículo no tiene cupo asignado.")
            return estacionamiento
    else:
        print("Opción inválida.")
        return estacionamiento

    liberado = estacionamiento.pop(idx)
    print(f"Cupo liberado: piso {liberado[0]}, lugar {liberado[1]}, vehículo ID {liberado[2]}.")
    return estacionamiento


def consultar_cupo(estacionamiento, vehiculos):
    print()
    print("¿Cómo quiere consultar?")
    print("  [1] Ver si un lugar (piso + número de cupo) está ocupado o vacío.")
    print("  [2] Ver en qué piso y cupo está estacionado un vehículo (por su ID).")
    modo = input("Seleccione (1 o 2): ").strip()
    if modo == "1":
        piso = entero_positivo_desde_cadena(input("Piso (1-3): "))
        nro = entero_positivo_desde_cadena(input(f"Número de cupo (1-{CUPOS_POR_PISO}): "))
        if piso is None or piso < 1 or piso > 3 or nro is None or nro < 1 or nro > CUPOS_POR_PISO:
            print("Datos inválidos.")
            return
        idx = indice_cupo_piso_y_numero(estacionamiento, piso, nro)
        if idx is None:
            print()
            print(f"Piso {piso}, cupo {nro}: no hay ningún vehículo cargado en ese lugar.")
            print("(En la matriz de estacionamiento no figura ocupado; se puede asignar un vehículo ahí.)")
            return
        id_v = estacionamiento[idx][2]
        v = buscar_vehiculo_por_id(vehiculos, id_v)
        if v is None:
            print()
            print(
                f"Piso {piso}, cupo {nro}: ocupado según el estacionamiento (ID vehículo {id_v}), "
                "pero ese ID no está en la matriz de vehículos."
            )
            return
        print()
        print(f"Piso {piso}, cupo {nro}: OCUPADO.")
        print(
            f"  Vehículo ID {v[0]} | patente {v[1]} | tipo {v[2]} | titular usuario ID {v[3]}"
        )
    elif modo == "2":
        id_v = entero_positivo_desde_cadena(input("ID de vehículo: "))
        if id_v is None:
            print("ID inválido.")
            return
        idx = indice_cupo_por_id_vehiculo(estacionamiento, id_v)
        if idx is None:
            print()
            print(f"El vehículo ID {id_v} no tiene cupo asignado (no aparece en la matriz de estacionamiento).")
            return
        e = estacionamiento[idx]
        v = buscar_vehiculo_por_id(vehiculos, id_v)
        if v is None:
            print()
            print(
                f"Vehículo ID {id_v}: figura en piso {e[0]}, cupo {e[1]}, "
                "pero no hay fila con ese ID en la matriz de vehículos."
            )
            return
        print()
        print(
            f"Vehículo ID {id_v} ({v[1]}, {v[2]}): estacionado en piso {e[0]}, cupo {e[1]}."
        )
        print(f"  Titular del vehículo: usuario ID {v[3]}.")
    else:
        print("Opción inválida.")


# ----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
# ----------------------------------------------------------------------------------------------
def main():
    usuarios = [fila[:] for fila in MATRIZ_USUARIOS]
    vehiculos = [fila[:] for fila in MATRIZ_VEHICULOS]
    estacionamiento = [fila[:] for fila in MATRIZ_ESTACIONAMIENTO]

    while True:
        while True:
            opciones = 4
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de usuarios")
            print("[2] Gestión de vehículos")
            print("[3] Gestión de estacionamiento")
            print("[4] Listado general (todas las matrices)")
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
            exit()

        elif opcion == "1":
            while True:
                while True:
                    opciones = 5
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
                    if sub in [str(i) for i in range(0, opciones + 1)]:
                        break
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if sub == "0":
                    break
                elif sub == "1":
                    usuarios = alta_usuario(usuarios)
                elif sub == "2":
                    listar_usuarios(usuarios)
                elif sub == "3":
                    consultar_usuario(usuarios)
                elif sub == "4":
                    usuarios = modificar_usuario(usuarios)
                elif sub == "5":
                    usuarios = baja_usuario(usuarios)

                input("\nPresione ENTER para continuar.")

        elif opcion == "2":
            while True:
                while True:
                    opciones = 3
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
                    if sub in [str(i) for i in range(0, opciones + 1)]:
                        break
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if sub == "0":
                    break
                elif sub == "1":
                    vehiculos = alta_vehiculo(vehiculos, usuarios)
                elif sub == "2":
                    listar_vehiculos(vehiculos)
                elif sub == "3":
                    vehiculos, estacionamiento = baja_vehiculo(vehiculos, estacionamiento)

                input("\nPresione ENTER para continuar.")

        elif opcion == "3":
            while True:
                while True:
                    opciones = 4
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
                    if sub in [str(i) for i in range(0, opciones + 1)]:
                        break
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if sub == "0":
                    break
                elif sub == "1":
                    estacionamiento = asignar_cupo(vehiculos, estacionamiento)
                elif sub == "2":
                    listar_estacionamiento(estacionamiento)
                elif sub == "3":
                    estacionamiento = liberar_cupo(estacionamiento)
                elif sub == "4":
                    consultar_cupo(estacionamiento, vehiculos)

                input("\nPresione ENTER para continuar.")

        elif opcion == "4":
            print("\n--- USUARIOS ---")
            listar_usuarios(usuarios)
            print("\n--- VEHÍCULOS ---")
            listar_vehiculos(vehiculos)
            print("\n--- ESTACIONAMIENTO (ocupados) ---")
            listar_estacionamiento(estacionamiento)

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


main()
