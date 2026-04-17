from parking.constantes import (
    CUPOS_POR_PISO,
    PISO_AUTOS,
    PISO_CAMIONETAS,
    PISO_MOTOS,
    TARIFA_MENSUAL_AUTO,
    TARIFA_MENSUAL_CAMIONETA,
    TARIFA_MENSUAL_MOTO,
)


def cadena_a_entero(cadena):
    """Usa int(); si el texto no es un entero >= 0, devuelve None (evita ValueError en los menús)."""
    if cadena is None:
        return None
    t = cadena.strip()
    if not t:
        return None
    try:
        n = int(t)
    except ValueError:
        return None
    if n < 0:
        return None
    return n


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
