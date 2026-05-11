# ----------------------------------------------------------------------------------------------
# CONSTANTES Y DATOS INICIALES (listas de diccionarios)
# ----------------------------------------------------------------------------------------------
import json

CUPOS_POR_PISO = 5
PISO_MOTOS = 1
PISO_AUTOS = 2
PISO_CAMIONETAS = 3

# Abono mensual en pesos: moto (menor cupo) < auto < camioneta (más espacio / categoría).
TARIFA_MENSUAL_MOTO = 42000
TARIFA_MENSUAL_AUTO = 68000
TARIFA_MENSUAL_CAMIONETA = 95000

# usuarios: id, nombre, apellido, dni
with open('usuarios.json', 'r', encoding='utf-8') as f:
    USUARIOS_INICIAL = json.load(f)

# vehículos: id, patente, tipo, usuario (id del titular), tarifa
with open('vehiculos.json', 'r', encoding='utf-8') as f:
    VEHICULOS_INICIAL = json.load(f)

# estacionamiento: piso, cupo (1..CUPOS_POR_PISO), vehiculo (id del vehículo)
with open('estacionamiento.json', 'r', encoding='utf-8') as f:
    ESTACIONAMIENTO_INICIAL = json.load(f)
