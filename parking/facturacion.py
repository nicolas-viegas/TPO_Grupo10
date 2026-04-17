"""
Reportes y simulaciones sobre las matrices (map, filter, etc.).

- map: transformar valores (ej. tarifa con descuento).
- filter: quedarse con filas que cumplen una condición.
"""

from parking.constantes import CUPOS_POR_PISO
from parking.utilidades import cadena_a_entero


def _tarifa_con_descuento(tarifa, porcentaje_descuento):
    """porcentaje_descuento: 0-100."""
    aplicar = lambda t, p: int(round(t * (1 - p / 100.0)))
    return aplicar(tarifa, porcentaje_descuento)


def mostrar_tarifas_con_descuento(vehiculos):
    if not vehiculos:
        print("No hay vehículos.")
        return
    pct_txt = input("Porcentaje de descuento a simular (0-100): ").strip()
    pct = cadena_a_entero(pct_txt)
    if pct is None or pct < 0 or pct > 100:
        print("Porcentaje inválido.")
        return
    print()
    print(f"Simulación: tarifa mensual con {pct}% de descuento (no modifica la matriz).")
    print("ID veh. | Patente   | Tarifa original | Con descuento")
    print("-" * 60)
    for fila in map(
        lambda v: (
            v[0],
            v[1],
            v[4],
            _tarifa_con_descuento(v[4], pct),
        ),
        vehiculos,
    ):
        print(f"{fila[0]:7} | {fila[1]:9} | {fila[2]:15} | {fila[3]:13}")


def mostrar_vehiculos_por_tipo(vehiculos):
    print("Tipo: [1] moto  [2] auto  [3] camioneta")
    op = input("Seleccione: ").strip()
    tipos = {"1": "moto", "2": "auto", "3": "camioneta"}
    if op not in tipos:
        print("Opción inválida.")
        return
    tipo = tipos[op]
    filtrados = list(filter(lambda v: v[2] == tipo, vehiculos))
    if not filtrados:
        print(f"No hay vehículos del tipo «{tipo}».")
        return
    print()
    print(f"Vehículos tipo «{tipo}» (filter): {len(filtrados)}")
    print("ID veh. | Patente   | ID usr | $ mensual")
    print("-" * 50)
    for v in filtrados:
        print(f"{v[0]:7} | {v[1]:9} | {v[3]:6} | {v[4]:9}")


def mostrar_ocupacion_por_piso(estacionamiento):
    """Resumen rápido: cupos ocupados y libres en cada piso (1 motos, 2 autos, 3 camionetas)."""
    print()
    print(f"Cupos por piso (máximo {CUPOS_POR_PISO} por piso):")
    print("-" * 45)
    for piso in (1, 2, 3):
        ocupados = sum(1 for e in estacionamiento if e[0] == piso)
        libres = CUPOS_POR_PISO - ocupados
        print(f"  Piso {piso}: {ocupados} ocupados, {libres} libres")


def mostrar_cupos_en_piso(estacionamiento):
    p = cadena_a_entero(input("Piso a listar (1-3): "))
    if p is None or p < 1 or p > 3:
        print("Piso inválido.")
        return
    filas = list(filter(lambda e: e[0] == p, estacionamiento))
    print()
    if not filas:
        print(f"No hay cupos ocupados en el piso {p} (filter).")
        return
    print(f"Cupos ocupados en piso {p}: {len(filas)}")
    print("Nro cupo | ID vehículo")
    print("-" * 28)
    for e in sorted(filas, key=lambda x: x[1]):
        print(f"{e[1]:8} | {e[2]}")


def menu_facturacion_y_lambdas(vehiculos, estacionamiento):
    while True:
        print()
        print("---------------------------")
        print("FACTURACIÓN / REPORTES")
        print("---------------------------")
        print("[1] Simular tarifa mensual con descuento % (map)")
        print("[2] Listar vehículos por tipo (filter)")
        print("[3] Ocupación por piso (cupos usados y libres)")
        print("[4] Cupos ocupados en un piso (filter)")
        print("---------------------------")
        print("[0] Volver al menú principal")
        print("---------------------------")
        print()

        sub = input("Seleccione una opción: ").strip()
        if sub == "0":
            break
        elif sub == "1":
            mostrar_tarifas_con_descuento(vehiculos)
        elif sub == "2":
            mostrar_vehiculos_por_tipo(vehiculos)
        elif sub == "3":
            mostrar_ocupacion_por_piso(estacionamiento)
        elif sub == "4":
            mostrar_cupos_en_piso(estacionamiento)
        else:
            print("Opción inválida.")

        input("\nPresione ENTER para continuar.")
