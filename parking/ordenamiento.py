from parking.utilidades import cadena_a_entero

ENCABEZADOS_USUARIOS = ["ID usuario", "Nombre", "Apellido", "DNI"]
ENCABEZADOS_VEHICULOS = ["ID vehículo", "Patente", "Tipo", "ID usuario", "Tarifa mensual"]
ENCABEZADOS_ESTACIONAMIENTO = ["Piso", "Nro cupo", "ID vehículo"]

# Mismo ancho para todas las columnas (f"{valor:18}" aprox.; subí el número si hace falta)
ANCHO_COLUMNA_TABLA = 18


def _linea_con_ancho_fijo(celdas, n_columnas, ancho):
    return " ".join(f"{str(celdas[i]):<{ancho}}" for i in range(n_columnas))


def ordenar_matriz_por_columna(matriz, indice_columna):
    """
    Ordena las filas de la matriz en forma ascendente según la columna indicada.
    Usa list.sort con key (por valor de esa columna en cada fila).
    """
    matriz.sort(key=lambda fila: fila[indice_columna])
    return matriz


def mostrar_matriz_con_encabezados(titulo, encabezados, matriz):
    if not matriz:
        print(f"\n{titulo}: (sin filas)")
        return
    print()
    print(titulo)
    n = len(encabezados)
    w = ANCHO_COLUMNA_TABLA
    print(_linea_con_ancho_fijo(encabezados, n, w))
    print("-" * (n * w))
    for fila in matriz:
        celdas = [fila[i] if i < len(fila) else "" for i in range(n)]
        print(_linea_con_ancho_fijo(celdas, n, w))


def flujo_ordenar_matriz(usuarios, vehiculos, estacionamiento):
    print()
    print("¿Qué matriz desea ordenar?")
    print("[1] Usuarios")
    print("[2] Vehículos")
    print("[3] Estacionamiento")
    print("[0] Volver sin ordenar")
    op = input("Seleccione: ").strip()
    if op == "0":
        return
    if op == "1":
        matriz, titulo, encabezados = usuarios, "Matriz de usuarios (ordenada)", ENCABEZADOS_USUARIOS
    elif op == "2":
        matriz, titulo, encabezados = vehiculos, "Matriz de vehículos (ordenada)", ENCABEZADOS_VEHICULOS
    elif op == "3":
        matriz, titulo, encabezados = (
            estacionamiento,
            "Matriz de estacionamiento (ordenada)",
            ENCABEZADOS_ESTACIONAMIENTO,
        )
    else:
        print("Opción inválida.")
        return

    if not matriz:
        print("La matriz está vacía; no hay nada que ordenar.")
        return

    num_columnas = len(matriz[0])
    print()
    print(f"Ingrese el número de columna por la cual ordenar (1 a {num_columnas}), ascendente:")
    for i in range(num_columnas):
        print(f"  {i + 1} = {encabezados[i]}")

    col_txt = input("Número de columna: ").strip()
    col = cadena_a_entero(col_txt)
    if col is None or col < 1 or col > num_columnas:
        print("Número de columna inválido.")
        return

    indice = col - 1
    ordenar_matriz_por_columna(matriz, indice)
    print(f"\nOrden aplicado por columna {col} («{encabezados[indice]}»), ascendente.")
    mostrar_matriz_con_encabezados(titulo, encabezados, matriz)
