from parking.utilidades import (
    buscar_usuario_por_id,
    buscar_vehiculo_por_id,
    buscar_vehiculo_por_patente,
    cadena_a_entero,
    indice_cupo_por_id_vehiculo,
    siguiente_id_vehiculo,
    tarifa_mensual_por_tipo,
)


def listar_vehiculos(vehiculos):
    if not vehiculos:
        print("No hay vehículos cargados.")
        return
    print()
    print("ID veh. | Patente   | Tipo      | ID usr | $ mensual")
    print("-" * 55)
    for v in vehiculos:
        tarifa = v.get("tarifa", "-")
        print(
            f"{v['id']:7} | {v['patente']:9} | {v['tipo']:9} | "
            f"{v['usuario']:6} | {tarifa!s:>9}"
        )


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

    id_usuario = cadena_a_entero(input("ID de usuario (titular): "))
    if id_usuario is None:
        print("Error: ID de usuario inválido.")
        return vehiculos
    if buscar_usuario_por_id(usuarios, id_usuario) is None:
        print("Error: no existe un usuario con ese ID.")
        return vehiculos

    tarifa = tarifa_mensual_por_tipo(tipo)
    nuevo_id = siguiente_id_vehiculo(vehiculos)
    vehiculos.append(
        {
            "id": nuevo_id,
            "patente": patente,
            "tipo": tipo,
            "usuario": id_usuario,
            "tarifa": tarifa,
        }
    )
    print(f"Vehículo dado de alta. ID: {nuevo_id}. Tarifa mensual: ${tarifa}")
    return vehiculos


def baja_vehiculo(vehiculos, estacionamiento):
    id_buscar = cadena_a_entero(input("Ingrese ID de vehículo a eliminar: "))
    if id_buscar is None:
        print("ID inválido.")
        return vehiculos, estacionamiento
    v = buscar_vehiculo_por_id(vehiculos, id_buscar)
    if v is None:
        print("No existe un vehículo con ese ID.")
        return vehiculos, estacionamiento

    confirmar = input(f"¿Eliminar vehículo {v['patente']} ({v['tipo']})? (s/n): ").strip().lower()
    if confirmar != "s":
        print("Operación cancelada.")
        return vehiculos, estacionamiento

    idx_est = indice_cupo_por_id_vehiculo(estacionamiento, id_buscar)
    if idx_est is not None:
        estacionamiento.pop(idx_est)

    for i, fila in enumerate(vehiculos):
        if fila["id"] == id_buscar:
            vehiculos.pop(i)
            break
    print("Vehículo eliminado.")
    return vehiculos, estacionamiento
