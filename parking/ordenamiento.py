from parking.utilidades import cadena_a_entero

CAMPOS_USUARIOS = ("id", "nombre", "apellido", "dni")
CAMPOS_VEHICULOS = ("id", "patente", "tipo", "usuario", "tarifa")
CAMPOS_ESTACIONAMIENTO = ("piso", "cupo", "vehiculo")

ROTULOS_USUARIOS = {
    "id": "ID usuario",
    "nombre": "Nombre",
    "apellido": "Apellido",
    "dni": "DNI",
}
ROTULOS_VEHICULOS = {
    "id": "ID vehículo",
    "patente": "Patente",
    "tipo": "Tipo",
    "usuario": "ID usuario (titular)",
    "tarifa": "Tarifa mensual",
}
ROTULOS_ESTACIONAMIENTO = {
    "piso": "Piso",
    "cupo": "Nro cupo",
    "vehiculo": "ID vehículo",
}

ANCHO_COLUMNA_TABLA = 18


def _linea_con_ancho_fijo(valores, ancho):
    return " ".join(f"{str(v):<{ancho}}" for v in valores)


def ordenar_registros_por_campo(registros, campo):
    """Orden ascendente por el valor de una clave en cada diccionario."""
    registros.sort(key=lambda r: r[campo])
    return registros


def mostrar_registros_tabla(titulo, orden_campos, rotulos, registros):
    if not registros:
        print(f"\n{titulo}: (sin registros)")
        return
    print()
    print(titulo)
    encabezados = [rotulos[c] for c in orden_campos]
    w = ANCHO_COLUMNA_TABLA
    print(_linea_con_ancho_fijo(encabezados, w))
    print("-" * (len(encabezados) * w))
    for r in registros:
        fila = [r[c] for c in orden_campos]
        print(_linea_con_ancho_fijo(fila, w))


def flujo_ordenar_matriz(usuarios, vehiculos, estacionamiento):
    print()
    print("¿Qué listado desea ordenar?")
    print("[1] Usuarios")
    print("[2] Vehículos")
    print("[3] Estacionamiento")
    print("[0] Volver sin ordenar")
    op = input("Seleccione: ").strip()
    if op == "0":
        return
    if op == "1":
        registros = usuarios
        titulo = "Usuarios (ordenados)"
        orden_campos = CAMPOS_USUARIOS
        rotulos = ROTULOS_USUARIOS
    elif op == "2":
        registros = vehiculos
        titulo = "Vehículos (ordenados)"
        orden_campos = CAMPOS_VEHICULOS
        rotulos = ROTULOS_VEHICULOS
    elif op == "3":
        registros = estacionamiento
        titulo = "Estacionamiento (ordenado)"
        orden_campos = CAMPOS_ESTACIONAMIENTO
        rotulos = ROTULOS_ESTACIONAMIENTO
    else:
        print("Opción inválida.")
        return

    if not registros:
        print("No hay registros para ordenar.")
        return

    n = len(orden_campos)
    print()
    print(f"Ingrese el número de campo por el cual ordenar (1 a {n}), ascendente:")
    for i, campo in enumerate(orden_campos):
        print(f"  {i + 1} = {rotulos[campo]}")

    col_txt = input("Número de campo: ").strip()
    col = cadena_a_entero(col_txt)
    if col is None or col < 1 or col > n:
        print("Número inválido.")
        return

    campo = orden_campos[col - 1]
    try:
        ordenar_registros_por_campo(registros, campo)
    except KeyError:
        print("No se pudo ordenar: falta alguna clave en un registro.")
        return
    print(f"\nOrden aplicado por «{rotulos[campo]}» ({campo}), ascendente.")
    mostrar_registros_tabla(titulo, orden_campos, rotulos, registros)
