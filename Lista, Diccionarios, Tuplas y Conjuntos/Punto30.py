#Cargar los datos de ventas de una empresa: cada venta tiene 
# fecha, vendedor, producto y monto. El sistema debe:
#● Calcular el total vendido por vendedor.
#● Mostrar el producto más vendido.
#● Calcular el promedio de ventas del mes.
#● Mostrar los vendedores que superan el promedio.

from datetime import date, datetime

# Ventas de ejemplo para poder probar. date(año, mes, día) crea una fecha.
ventas = [
    {"fecha": date(2026, 10, 1), "vendedor": "Ana", "producto": "Notebook", "monto": 950000.0},
    {"fecha": date(2026, 10, 3), "vendedor": "Luis", "producto": "Mouse", "monto": 25000.0},
    {"fecha": date(2026, 10, 5), "vendedor": "Ana", "producto": "Monitor", "monto": 320000.0},
    {"fecha": date(2026, 10, 8), "vendedor": "Sol", "producto": "Notebook", "monto": 980000.0},
    {"fecha": date(2026, 10, 12), "vendedor": "Luis", "producto": "Teclado", "monto": 60000.0},
    {"fecha": date(2026, 10, 15), "vendedor": "Sol", "producto": "Mouse", "monto": 27000.0},
    {"fecha": date(2026, 10, 18), "vendedor": "Luis", "producto": "Mouse", "monto": 25000.0},
    {"fecha": date(2026, 9, 28), "vendedor": "Ana", "producto": "Teclado", "monto": 58000.0},
]


def pedir_texto(mensaje):
    """Pide un dato por teclado y no permite que quede vacío."""
    while True:
        texto = input(mensaje).strip()  # strip() quita los espacios del principio y del final
        if texto:
            return texto
        print("Este dato no puede quedar vacío.")


def pedir_monto(mensaje):
    """Pide un número decimal mayor a 0."""
    while True:
        try:
            monto = float(input(mensaje).replace(",", "."))  # replace(): acepta coma decimal; float(): a decimal
        except ValueError:
            print("Ingrese un monto válido.")
            continue
        if monto > 0:
            return monto
        print("El monto debe ser mayor a 0.")


def pedir_fecha(mensaje):
    """Pide una fecha en formato dd/mm/aaaa. Si se presiona Enter, usa la fecha de hoy."""
    while True:
        texto = input(f"{mensaje} (dd/mm/aaaa, Enter = hoy): ").strip()
        if not texto:
            return date.today()  # date.today() devuelve la fecha actual
        try:
            # strptime() convierte un texto en fecha según el formato; .date() descarta la hora
            return datetime.strptime(texto, "%d/%m/%Y").date()
        except ValueError:
            print("Fecha inválida. Use el formato dd/mm/aaaa.")


def pedir_mes():
    """Pide un mes en formato mm/aaaa y devuelve la tupla (mes, año)."""
    while True:
        texto = input("Mes a analizar (mm/aaaa, Enter = mes actual): ").strip()
        if not texto:
            hoy = date.today()
            return hoy.month, hoy.year
        try:
            fecha = datetime.strptime(texto, "%m/%Y")
            return fecha.month, fecha.year
        except ValueError:
            print("Formato inválido. Use mm/aaaa (ej.: 10/2026).")


def totales_por_vendedor(lista):
    """Devuelve un diccionario vendedor → total vendido."""
    totales = {}
    for venta in lista:
        # get(clave, 0) devuelve el total acumulado o 0 si el vendedor todavía no está en el diccionario
        totales[venta["vendedor"]] = totales.get(venta["vendedor"], 0) + venta["monto"]
    return totales


def agregar_venta():
    fecha = pedir_fecha("Fecha de la venta")
    vendedor = pedir_texto("Vendedor: ").title()  # title(): mayúscula al inicio de cada palabra
    producto = pedir_texto("Producto: ").capitalize()  # capitalize(): normaliza para poder agrupar
    monto = pedir_monto("Monto: $")
    ventas.append({"fecha": fecha, "vendedor": vendedor, "producto": producto, "monto": monto})  # append(): agrega al final
    print("Venta registrada.")


def mostrar_total_por_vendedor():
    totales = totales_por_vendedor(ventas)
    if not totales:
        print("No hay ventas registradas.")
        return
    print("Total vendido por vendedor:")
    # items() devuelve los pares (vendedor, total); se ordenan por total de mayor a menor
    for vendedor, total in sorted(totales.items(), key=lambda x: x[1], reverse=True):
        print(f"  {vendedor:<15} ${total:>14,.2f}")


def producto_mas_vendido():
    # Como cada venta no tiene cantidad, "más vendido" = el producto que aparece en más ventas
    conteo = {}
    for venta in ventas:
        conteo[venta["producto"]] = conteo.get(venta["producto"], 0) + 1
    if not conteo:
        print("No hay ventas registradas.")
        return
    maximo = max(conteo.values())  # values() devuelve solo los valores; max() el mayor
    # Puede haber empate: se muestran todos los productos con la cantidad máxima
    mas_vendidos = [producto for producto, cantidad in conteo.items() if cantidad == maximo]
    print(f"Producto/s más vendido/s: {', '.join(mas_vendidos)} ({maximo} venta/s)")  # join(): une con ", "


def promedio_y_vendedores_destacados():
    mes, anio = pedir_mes()
    # .month y .year devuelven el mes y el año de cada fecha
    del_mes = [v for v in ventas if v["fecha"].month == mes and v["fecha"].year == anio]
    if not del_mes:
        print(f"No hay ventas en {mes:02d}/{anio}.")  # :02d muestra el mes con 2 dígitos
        return

    total_mes = sum(v["monto"] for v in del_mes)  # sum() suma los montos
    promedio_por_venta = total_mes / len(del_mes)
    print(f"Ventas de {mes:02d}/{anio}: {len(del_mes)} | Total: ${total_mes:,.2f}")
    print(f"Promedio por venta: ${promedio_por_venta:,.2f}")

    # Para comparar vendedores se usa el promedio POR VENDEDOR (total del mes / cantidad de vendedores).
    # Comparar el total de un vendedor contra el monto de UNA venta promedio haría que casi todos lo superen.
    totales = totales_por_vendedor(del_mes)
    promedio_por_vendedor = total_mes / len(totales)
    print(f"Promedio por vendedor: ${promedio_por_vendedor:,.2f}")

    superan = [(vendedor, total) for vendedor, total in totales.items() if total > promedio_por_vendedor]
    if superan:
        print("Vendedores que superan el promedio:")
        for vendedor, total in sorted(superan, key=lambda x: x[1], reverse=True):
            print(f"  {vendedor:<15} ${total:>14,.2f}")
    else:
        print("Ningún vendedor supera el promedio (todos vendieron lo mismo).")


while True:
    print("\n=== VENTAS ===")
    print("1. Agregar venta")
    print("2. Total vendido por vendedor")
    print("3. Producto más vendido")
    print("4. Promedio del mes y vendedores que lo superan")
    print("5. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_venta()
    elif opcion == "2":
        mostrar_total_por_vendedor()
    elif opcion == "3":
        producto_mas_vendido()
    elif opcion == "4":
        promedio_y_vendedores_destacados()
    elif opcion == "5":
        break
    else:
        print("Opción no válida.")
