# ----------------------------------------------------------------------------------------------
# CONSTANTES Y MATRICES INICIALES (datos de ejemplo)
# ----------------------------------------------------------------------------------------------
CUPOS_POR_PISO = 5
PISO_MOTOS = 1
PISO_AUTOS = 2
PISO_CAMIONETAS = 3

# Abono mensual en pesos: moto (menor cupo) < auto < camioneta (más espacio / categoría).
TARIFA_MENSUAL_MOTO = 42000
TARIFA_MENSUAL_AUTO = 68000
TARIFA_MENSUAL_CAMIONETA = 95000

# usuarios: [id_usuario, nombre, apellido, dni]
MATRIZ_USUARIOS = [
    [1, "Ana", "García", "28111222"],
    [2, "Luis", "Rodríguez", "35111222"],
    [3, "María", "Fernández", "40111222"],
    [4, "Pedro", "López", "20999888"],
]

# vehículos: [id_vehiculo, patente, tipo, id_usuario, tarifa_mensual]
MATRIZ_VEHICULOS = [
    [1, "AB123CD", "moto", 1, TARIFA_MENSUAL_MOTO],
    [2, "XY987ZZ", "auto", 1, TARIFA_MENSUAL_AUTO],
    [3, "AA000BB", "camioneta", 2, TARIFA_MENSUAL_CAMIONETA],
    [4, "MOTO99", "moto", 3, TARIFA_MENSUAL_MOTO],
    [5, "CD456EF", "auto", 4, TARIFA_MENSUAL_AUTO],
]

# estacionamiento: [piso, nro_estacionamiento (1..CUPOS_POR_PISO), id_vehiculo]
MATRIZ_ESTACIONAMIENTO = [
    [1, 1, 1],
    [1, 2, 4],
    [2, 1, 2],
    [2, 3, 5],
    [3, 4, 3],
]
