from parking.constantes import CUPOS_POR_PISO
from parking.utilidades import (
    buscar_vehiculo_por_id,
    cadena_a_entero,
    indice_cupo_piso_y_numero,
    indice_cupo_por_id_vehiculo,
    piso_para_tipo,
    primer_cupo_libre_en_piso,
)


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
    id_v = cadena_a_entero(input("ID de vehículo a estacionar: "))
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
        piso = cadena_a_entero(input("Piso (1-3): "))
        nro = cadena_a_entero(input(f"Número de cupo (1-{CUPOS_POR_PISO}): "))
        if piso is None or piso < 1 or piso > 3 or nro is None or nro < 1 or nro > CUPOS_POR_PISO:
            print("Datos inválidos.")
            return estacionamiento
        idx = indice_cupo_piso_y_numero(estacionamiento, piso, nro)
        if idx is None:
            print("No hay vehículo en ese cupo.")
            return estacionamiento
    elif modo == "2":
        id_v = cadena_a_entero(input("ID de vehículo: "))
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
        piso = cadena_a_entero(input("Piso (1-3): "))
        nro = cadena_a_entero(input(f"Número de cupo (1-{CUPOS_POR_PISO}): "))
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
        id_v = cadena_a_entero(input("ID de vehículo: "))
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
