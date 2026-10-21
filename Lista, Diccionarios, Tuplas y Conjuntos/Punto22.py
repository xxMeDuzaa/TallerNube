#Desarrollar un programa que permita registrar gastos diarios (fecha, categoría y monto). El sistema debe:
#● Permitir agregar nuevos gastos.
#● Mostrar el total gastado en el mes.
#● Mostrar el total por categoría.
#● Calcular el promedio diario de gasto.

from datetime import date, datetime  # date: solo fecha / datetime: fecha y hora (y conversión desde texto)

gastos = []  # Cada gasto: {"fecha": date, "categoria": str, "monto": float}


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
            # replace(",", ".") cambia la coma por punto para aceptar "1500,50"; float() convierte a decimal
            monto = float(input(mensaje).replace(",", "."))
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
            # strptime() convierte un texto en fecha según el formato indicado (%d día, %m mes, %Y año).
            # .date() se queda solo con la fecha, sin la hora.
            return datetime.strptime(texto, "%d/%m/%Y").date()
        except ValueError:  # strptime lanza ValueError si el texto no respeta el formato o la fecha no existe
            print("Fecha inválida. Use el formato dd/mm/aaaa.")


def pedir_mes():
    """Pide un mes en formato mm/aaaa y devuelve la tupla (mes, año)."""
    while True:
        texto = input("Mes a consultar (mm/aaaa, Enter = mes actual): ").strip()
        if not texto:
            hoy = date.today()
            return hoy.month, hoy.year  # Devolver dos valores separados por coma = devolver una tupla
        try:
            fecha = datetime.strptime(texto, "%m/%Y")
            return fecha.month, fecha.year
        except ValueError:
            print("Formato inválido. Use mm/aaaa (ej.: 10/2026).")


def gastos_del_mes():
    """Pide un mes y devuelve (mes, año, lista de gastos de ese mes)."""
    mes, anio = pedir_mes()  # Desempaquetado: cada valor de la tupla va a una variable
    # .month y .year son atributos de una fecha: devuelven el número de mes y el año
    del_mes = [g for g in gastos if g["fecha"].month == mes and g["fecha"].year == anio]
    if not del_mes:
        print(f"No hay gastos registrados en {mes:02d}/{anio}.")  # :02d muestra el mes con 2 dígitos (05)
    return mes, anio, del_mes


def agregar_gasto():
    fecha = pedir_fecha("Fecha del gasto")
    # capitalize() deja la primera letra en mayúscula y el resto en minúscula:
    # así "COMIDA", "comida" y "Comida" se guardan igual y se suman en la misma categoría
    categoria = pedir_texto("Categoría (ej.: comida, transporte, servicios): ").capitalize()
    monto = pedir_monto("Monto: $")
    gastos.append({"fecha": fecha, "categoria": categoria, "monto": monto})  # append() agrega al final
    # strftime() convierte una fecha a texto con el formato indicado
    print(f"Gasto registrado: {fecha.strftime('%d/%m/%Y')} - {categoria} - ${monto:,.2f}")


def total_del_mes():
    mes, anio, del_mes = gastos_del_mes()
    if del_mes:
        # sum() suma todos los valores que genera la expresión
        total = sum(g["monto"] for g in del_mes)
        print(f"Total gastado en {mes:02d}/{anio}: ${total:,.2f} ({len(del_mes)} gasto/s)")


def total_por_categoria():
    mes, anio, del_mes = gastos_del_mes()
    if not del_mes:
        return
    totales = {}  # Diccionario: categoría → total acumulado
    for gasto in del_mes:
        # get(clave, 0) devuelve el valor de la clave, o 0 si todavía no existe.
        # Así se puede acumular sin que dé KeyError la primera vez que aparece una categoría.
        totales[gasto["categoria"]] = totales.get(gasto["categoria"], 0) + gasto["monto"]

    print(f"Total por categoría en {mes:02d}/{anio}:")
    # items() devuelve los pares (clave, valor) del diccionario.
    # sorted(..., key=lambda x: x[1], reverse=True) los ordena por el valor (x[1]) de mayor a menor.
    for categoria, total in sorted(totales.items(), key=lambda x: x[1], reverse=True):
        print(f"  {categoria:<15} ${total:>12,.2f}")


def promedio_diario():
    mes, anio, del_mes = gastos_del_mes()
    if not del_mes:
        return
    # Comprensión de CONJUNTO (con llaves): un set no admite repetidos, entonces cada fecha
    # queda una sola vez aunque haya varios gastos el mismo día
    dias_con_gastos = {g["fecha"] for g in del_mes}
    total = sum(g["monto"] for g in del_mes)
    promedio = total / len(dias_con_gastos)
    print(f"Promedio diario en {mes:02d}/{anio}: ${promedio:,.2f} "
          f"(sobre {len(dias_con_gastos)} día/s con gastos)")


while True:
    print("\n=== GASTOS DIARIOS ===")
    print("1. Agregar gasto")
    print("2. Total gastado en el mes")
    print("3. Total por categoría")
    print("4. Promedio diario de gasto")
    print("5. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_gasto()
    elif opcion == "2":
        total_del_mes()
    elif opcion == "3":
        total_por_categoria()
    elif opcion == "4":
        promedio_diario()
    elif opcion == "5":
        break
    else:
        print("Opción no válida.")
