from parking.utilidades import (
    buscar_usuario_por_id,
    cadena_a_entero,
    siguiente_id_usuario,
    normalizar_texto,
    validar_dni,
    validar_nombre_o_apellido,
)

def listar_usuarios(usuarios):
    if not usuarios:
        print("No hay usuarios cargados.")
        return
    print()
    print("ID | Nombre      | Apellido    | DNI")
    print("-" * 45)
    for u in usuarios:
        print(f"{u['id']:2} | {u['nombre']:11} | {u['apellido']:11} | {u['dni']}")


def alta_usuario(usuarios):
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    dni = input("DNI: ").strip()
    if not nombre or not apellido or not dni:
        print("Error: todos los campos son obligatorios.")
        return usuarios
    if not validar_nombre_o_apellido(nombre):
        print("Error: el nombre debe contener solo letras y tener entre 2 y 30 caracteres.")
        return usuarios
    if not validar_nombre_o_apellido(apellido):
        print("Error: el apellido debe contener solo letras y tener entre 2 y 30 caracteres.")
        return usuarios
    if not validar_dni(dni):
        print("Error: el DNI debe tener 7 u 8 números.")
        return usuarios
    nombre = normalizar_texto(nombre)
    apellido = normalizar_texto(apellido)
    dni = dni.strip()
    nuevo_id = siguiente_id_usuario(usuarios)
    usuarios.append({
        "id": nuevo_id,
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni
    })
    print(f"Usuario dado de alta. ID asignado: {nuevo_id}")
    return usuarios


def consultar_usuario(usuarios):
    try:
        id_buscar = cadena_a_entero(input("Ingrese ID de usuario: "))
        if id_buscar is None:
            print("ID inválido.")
            return
        u = buscar_usuario_por_id(usuarios, id_buscar)
        if u is None:
            print("No existe un usuario con ese ID.")
        else:
            print(f"ID: {u['id']} | {u['nombre']} {u['apellido']} | DNI: {u['dni']}")
    except Exception as exc:
        print(f"Error inesperado al consultar usuario: {exc}")]}")


def modificar_usuario(usuarios):
    id_buscar = cadena_a_entero(input("Ingrese ID de usuario a modificar: "))
    if id_buscar is None:
        print("ID inválido.")
        return usuarios
    u = buscar_usuario_por_id(usuarios, id_buscar)
    if u is None:
        print("No existe un usuario con ese ID.")
        return usuarios
    print("(Deje vacío para no cambiar el campo.)")
    nombre = input(f"Nombre [{u['nombre']}]: ").strip()
    apellido = input(f"Apellido [{u['apellido']}]: ").strip()
    dni = input(f"DNI [{u['dni']}]: ").strip()
    if nombre:
        if validar_nombre_o_apellido(nombre):
            u["nombre"] = normalizar_texto(nombre)
        else:
            print("Nombre inválido. No se modificó.")
    if apellido:
        if validar_nombre_o_apellido(apellido):
            u["apellido"] = normalizar_texto(apellido)
        else:
            print("Apellido inválido. No se modificó.")
    if dni:
        if validar_dni(dni):
            u["dni"] = dni.strip()
        else:
            print("DNI inválido. No se modificó.")
    print("Usuario actualizado.")
    return usuarios


def baja_usuario(usuarios):
    try:
        id_buscar = cadena_a_entero(input("Ingrese ID de usuario a eliminar: "))
        if id_buscar is None:
            print("ID inválido.")
            return usuarios
        for i, u in enumerate(usuarios):
            if u["id"] == id_buscar:
                confirmar = input(f"¿Eliminar a {u['nombre']} {u['apellido']}? (s/n): ").strip().lower()
                if confirmar == "s":
                    usuarios.pop(i)
                    print("Usuario eliminado.")
                else:
                    print("Operación cancelada.")
                return usuarios
        print("No existe un usuario con ese ID.")
    except Exception as exc:
        print(f"Error inesperado en la baja de usuario: {exc}")
    return usuarios
