from parking.utilidades import (
    buscar_usuario_por_id,
    buscar_vehiculo_por_patente,
    cadena_a_entero,
    siguiente_id_vehiculo,
    tarifa_mensual_por_tipo,
    validar_patente,
    formatear_patente,
)


def listar_vehiculos(vehiculos, usuarios):
    if not vehiculos:
        print("No hay vehículos cargados.")
        return
    print()
    # Ajustamos el ancho para que entre el nombre del titular
    print("ID veh. | Patente   | Tipo      | Titular (ID - Nombre)          | $ mensual")
    print("-" * 80)
    for v in vehiculos:
        tarifa = v.get("tarifa", "-")

        u = buscar_usuario_por_id(usuarios, v["usuario"])
        if u is not None:
            nombre_titular = f"{u['id']} - {u['nombre']} {u['apellido']}"
        else:
            nombre_titular = f"{v['usuario']} - (Desconocido)"
            
        # para que la tabla no se descuadre lo cortamos
        nombre_titular = nombre_titular[:28]
        
        print(
            f"{v['id']:7} | {v['patente']:9} | {v['tipo']:9} | "
            f"{nombre_titular:30} | {tarifa!s:>9}"
        )


def alta_vehiculo(vehiculos, usuarios):
    patente = input("Patente: ").strip().upper()
    if not patente:
        print("Error: la patente es obligatoria.")
        return vehiculos
    if not validar_patente(patente):
        print("Error: patente inválida. Use formato AB123CD o ABC123.")
        return vehiculos
    patente = formatear_patente(patente).replace("-", "")
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


def buscar_vehiculo_por_id(vehiculos, id_vehiculo):
    i = 0
    encontrado = None
    while i < len(vehiculos) and encontrado is None:
        if vehiculos[i]["id"] == id_vehiculo:
            encontrado = vehiculos[i]
        i += 1
    return encontrado

def modificar_vehiculo(vehiculos, usuarios):
    id_buscar = cadena_a_entero(input("Ingrese ID de vehículo a modificar: "))
    if id_buscar is None:
        print("ID inválido.")
        return vehiculos    
    
    v = buscar_vehiculo_por_id(vehiculos, id_buscar)
    if v is None:
        print("No existe un vehículo con ese ID.")
        return vehiculos
    
    patente = input(f"Patente [{v['patente']}]: ").strip().upper()
    if patente and patente != v['patente']:
        if buscar_vehiculo_por_patente(vehiculos, patente) is not None:
            print("Error: ya existe otro vehículo con esa patente.")
        else:
            v["patente"] = patente
            print("Patente actualizada.")

    print(f"Tipo actual: {v['tipo']}. [1] moto  [2] auto  [3] camioneta")
    ingresar_tipo = input("Seleccione nuevo tipo (o deje vacío): ").strip()
    if ingresar_tipo in ["1", "2", "3"]:
        tipos = {"1": "moto", "2": "auto", "3": "camioneta"}
        v["tipo"] = tipos[ingresar_tipo]
        v["tarifa"] = tarifa_mensual_por_tipo(v["tipo"])
        print("Tipo y tarifa actualizados.")

    id_usr_txt = input(f"ID de nuevo titular [{v['usuario']}]: ").strip()
    if id_usr_txt:
        try:
            nuevo_id_usr = int(id_usr_txt)
            if buscar_usuario_por_id(usuarios, nuevo_id_usr) is not None:
                v["usuario"] = nuevo_id_usr
                print("Titular actualizado.")
            else:
                print("Error: El ID de usuario no existe.")
        except ValueError:
            print("Error: El ID de usuario debe ser un número entero válido.")
    return vehiculos


def consultar_vehiculos_de_usuario(vehiculos, usuarios):
    id_usuario = cadena_a_entero(input("Ingrese ID de usuario para ver sus vehículos: "))
    if id_usuario is None:
        print("ID inválido.")
        return
    
    u = buscar_usuario_por_id(usuarios, id_usuario)
    if u is None:
        print("No existe un usuario con ese ID.")
        return
    
    print(f"\nVehículos registrados a nombre de: {u['nombre']} {u['apellido']} (ID: {u['id']})")
    print("-" * 60)
    
    encontrados = 0
    # Usamos búsqueda secuencial pura (while) como pide la cátedra
    i = 0
    while i < len(vehiculos):
        v = vehiculos[i]
        if v["usuario"] == id_usuario:
            print(f" - ID Vehículo: {v['id']:3} | Patente: {v['patente']:9} | Tipo: {v['tipo']}")
            encontrados += 1
        i += 1
        
    if encontrados == 0:
        print("Este usuario no tiene vehículos registrados.")