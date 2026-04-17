from parking.utilidades import (
    buscar_usuario_por_id,
    cadena_a_entero,
    siguiente_id_usuario,
)


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
    id_buscar = cadena_a_entero(input("Ingrese ID de usuario: "))
    if id_buscar is None:
        print("ID inválido.")
        return
    u = buscar_usuario_por_id(usuarios, id_buscar)
    if u is None:
        print("No existe un usuario con ese ID.")
    else:
        print(f"ID: {u[0]} | {u[1]} {u[2]} | DNI: {u[3]}")


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
    id_buscar = cadena_a_entero(input("Ingrese ID de usuario a eliminar: "))
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
