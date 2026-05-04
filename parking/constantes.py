# ----------------------------------------------------------------------------------------------
# CONSTANTES Y DATOS INICIALES (listas de diccionarios)
# ----------------------------------------------------------------------------------------------
CUPOS_POR_PISO = 5
PISO_MOTOS = 1
PISO_AUTOS = 2
PISO_CAMIONETAS = 3

# Abono mensual en pesos: moto (menor cupo) < auto < camioneta (más espacio / categoría).
TARIFA_MENSUAL_MOTO = 42000
TARIFA_MENSUAL_AUTO = 68000
TARIFA_MENSUAL_CAMIONETA = 95000

# usuarios: id, nombre, apellido, dni
USUARIOS_INICIAL = [
    {"id": 1, "nombre": "Ana", "apellido": "García", "dni": "28111222"},
    {"id": 2, "nombre": "Luis", "apellido": "Rodríguez", "dni": "35111222"},
    {"id": 3, "nombre": "María", "apellido": "Fernández", "dni": "40111222"},
    {"id": 4, "nombre": "Pedro", "apellido": "López", "dni": "20999888"},
]

# vehículos: id, patente, tipo, usuario (id del titular), tarifa
VEHICULOS_INICIAL = [
    {"id": 1, "patente": "AB123CD", "tipo": "moto", "usuario": 1, "tarifa": TARIFA_MENSUAL_MOTO},
    {"id": 2, "patente": "XY987ZZ", "tipo": "auto", "usuario": 1, "tarifa": TARIFA_MENSUAL_AUTO},
    {"id": 3, "patente": "AA000BB", "tipo": "camioneta", "usuario": 2, "tarifa": TARIFA_MENSUAL_CAMIONETA},
    {"id": 4, "patente": "MOTO99", "tipo": "moto", "usuario": 3, "tarifa": TARIFA_MENSUAL_MOTO},
    {"id": 5, "patente": "CD456EF", "tipo": "auto", "usuario": 4, "tarifa": TARIFA_MENSUAL_AUTO},
]

# estacionamiento: piso, cupo (1..CUPOS_POR_PISO), vehiculo (id del vehículo)
ESTACIONAMIENTO_INICIAL = [
    {"piso": 1, "cupo": 1, "vehiculo": 1},
    {"piso": 1, "cupo": 2, "vehiculo": 4},
    {"piso": 2, "cupo": 1, "vehiculo": 2},
    {"piso": 2, "cupo": 3, "vehiculo": 5},
    {"piso": 3, "cupo": 4, "vehiculo": 3},
]
