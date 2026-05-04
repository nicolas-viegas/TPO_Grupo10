"""
Reportes y simulaciones sobre los registros (map, filter, etc.).

- map: transformar valores (ej. tarifa con descuento).
- filter: quedarse con filas que cumplen una condición.
"""

from parking import archivos
from parking.constantes import CUPOS_POR_PISO
from parking.utilidades import cadena_a_entero, division_segura, promedio_lista_numeros


def _tarifa_con_descuento(tarifa, porcentaje_descuento):
    """porcentaje_descuento: 0-100."""
    aplicar = lambda t, p: int(round(t * (1 - p / 100.0)))
    try:
        return aplicar(tarifa, porcentaje_descuento)
    except TypeError:
        return 0


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
    print(f"Simulación: tarifa mensual con {pct}% de descuento (no modifica los datos).")
    print("ID veh. | Patente   | Tarifa original | Con descuento")
    print("-" * 60)
    try:
        for fila in map(
            lambda v: (
                v["id"],
                v["patente"],
                v["tarifa"],
                _tarifa_con_descuento(v["tarifa"], pct),
            ),
            vehiculos,
        ):
            print(f"{fila[0]:7} | {fila[1]:9} | {fila[2]:15} | {fila[3]:13}")
    except (KeyError, TypeError) as exc:
        print(f"Error al procesar los datos de vehículos: {exc}")


def mostrar_vehiculos_por_tipo(vehiculos):
    print("Tipo: [1] moto  [2] auto  [3] camioneta")
    op = input("Seleccione: ").strip()
    tipos = {"1": "moto", "2": "auto", "3": "camioneta"}
    if op not in tipos:
        print("Opción inválida.")
        return
    tipo = tipos[op]
    filtrados = list(filter(lambda v: v["tipo"] == tipo, vehiculos))
    if not filtrados:
        print(f"No hay vehículos del tipo «{tipo}».")
        return
    print()
    print(f"Vehículos tipo «{tipo}» (filter): {len(filtrados)}")
    print("ID veh. | Patente   | ID usr | $ mensual")
    print("-" * 50)
    for v in filtrados:
        print(f"{v['id']:7} | {v['patente']:9} | {v['usuario']:6} | {v['tarifa']:9}")


def mostrar_ocupacion_por_piso(estacionamiento):
    """Resumen rápido: cupos ocupados y libres en cada piso (1 motos, 2 autos, 3 camionetas)."""
    print()
    print(f"Cupos por piso (máximo {CUPOS_POR_PISO} por piso):")
    print("-" * 45)
    for piso in (1, 2, 3):
        ocupados = sum(1 for e in estacionamiento if e["piso"] == piso)
        libres = CUPOS_POR_PISO - ocupados
        print(f"  Piso {piso}: {ocupados} ocupados, {libres} libres")

    total_plazas = 3 * CUPOS_POR_PISO
    ocupados_total = len(estacionamiento)
    ratio = division_segura(ocupados_total, total_plazas)
    if ratio is not None:
        print()
        print(
            f"  Ocupación global aproximada: {ratio * 100:.1f}% "
            f"({ocupados_total} cupos ocupados de {total_plazas})."
        )


def mostrar_promedio_tarifa_mensual(vehiculos):
    """Usa promedio_lista_numeros (manejo explícito de división por cero si la lista estuviera vacía)."""
    if not vehiculos:
        print("No hay vehículos.")
        return
    try:
        tarifas = [v["tarifa"] for v in vehiculos]
    except (KeyError, TypeError):
        print("No se pudieron leer las tarifas del listado de vehículos.")
        return
    promedio = promedio_lista_numeros(tarifas)
    if promedio is None:
        print("No se puede calcular el promedio (sin datos válidos).")
        return
    print()
    print(f"Promedio de tarifa mensual (todos los vehículos): ${promedio:.0f}")


def mostrar_cupos_en_piso(estacionamiento):
    p = cadena_a_entero(input("Piso a listar (1-3): "))
    if p is None or p < 1 or p > 3:
        print("Piso inválido.")
        return
    filas = list(filter(lambda e: e["piso"] == p, estacionamiento))
    print()
    if not filas:
        print(f"No hay cupos ocupados en el piso {p} (filter).")
        return
    print(f"Cupos ocupados en piso {p}: {len(filas)}")
    print("Nro cupo | ID vehículo")
    print("-" * 28)
    for e in sorted(filas, key=lambda x: x["cupo"]):
        print(f"{e['cupo']:8} | {e['vehiculo']}")


def menu_facturacion_y_lambdas(usuarios_list, vehiculos_list, estacionamiento_list):
    while True:
        print()
        print("---------------------------")
        print("FACTURACIÓN / REPORTES")
        print("---------------------------")
        print("[1] Simular tarifa mensual con descuento % (map)")
        print("[2] Listar vehículos por tipo (filter)")
        print("[3] Ocupación por piso (cupos usados y libres)")
        print("[4] Cupos ocupados en un piso (filter)")
        print("[5] Promedio de tarifa mensual (división segura)")
        print("[6] Exportar datos a archivo JSON")
        print("[7] Importar datos desde archivo JSON")
        print("---------------------------")
        print("[0] Volver al menú principal")
        print("---------------------------")
        print()

        sub = input("Seleccione una opción: ").strip()
        if sub == "0":
            break
        elif sub == "1":
            mostrar_tarifas_con_descuento(vehiculos_list)
        elif sub == "2":
            mostrar_vehiculos_por_tipo(vehiculos_list)
        elif sub == "3":
            mostrar_ocupacion_por_piso(estacionamiento_list)
        elif sub == "4":
            mostrar_cupos_en_piso(estacionamiento_list)
        elif sub == "5":
            mostrar_promedio_tarifa_mensual(vehiculos_list)
        elif sub == "6":
            ruta = input("Ruta del archivo JSON a crear (ej. backup.json): ").strip()
            if not ruta:
                print("Debe indicar una ruta.")
            elif archivos.exportar_matrices_json(
                ruta, usuarios_list, vehiculos_list, estacionamiento_list
            ):
                print("Exportación finalizada correctamente.")
        elif sub == "7":
            ruta = input("Ruta del archivo JSON a cargar: ").strip()
            if not ruta:
                print("Debe indicar una ruta.")
            else:
                datos = archivos.importar_matrices_json(ruta)
                if datos is not None:
                    u, v, e = datos
                    usuarios_list[:] = [dict(reg) for reg in u]
                    vehiculos_list[:] = [dict(reg) for reg in v]
                    estacionamiento_list[:] = [dict(reg) for reg in e]
                    print("Datos actualizados desde el archivo.")
        else:
            print("Opción inválida.")

        input("\nPresione ENTER para continuar.")
