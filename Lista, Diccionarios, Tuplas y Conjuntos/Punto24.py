#Permitir ingresar datos de varios empleados (nombre, sector, sueldo base, antigüedad). 
#Calcular el sueldo final según el siguiente criterio:
#● Antigüedad < 5 años → +5%.
#● Antigüedad entre 5 y 10 → +10%.
#● Antigüedad > 10 → +20%.
#● Mostrar un informe con el sueldo final de cada empleado y el promedio general.


def pedir_texto(mensaje):
    """Pide un dato por teclado y no permite que quede vacío."""
    while True:
        texto = input(mensaje).strip()  # strip() quita los espacios del principio y del final
        if texto:
            return texto
        print("Este dato no puede quedar vacío.")


def pedir_entero(mensaje, minimo=0):
    """Pide un número entero mayor o igual a 'minimo'."""
    while True:
        try:
            valor = int(input(mensaje))  # int() convierte el texto a entero
        except ValueError:
            print("Ingrese un número entero válido.")
            continue
        if valor >= minimo:
            return valor
        print(f"El valor debe ser mayor o igual a {minimo}.")


def pedir_monto(mensaje):
    """Pide un número decimal mayor a 0."""
    while True:
        try:
            # replace(",", ".") permite escribir "150000,50"; float() convierte el texto a decimal
            monto = float(input(mensaje).replace(",", "."))
        except ValueError:
            print("Ingrese un monto válido.")
            continue
        if monto > 0:
            return monto
        print("El monto debe ser mayor a 0.")


def porcentaje_aumento(antiguedad):
    """Devuelve el porcentaje de aumento (como decimal) según los años de antigüedad."""
    if antiguedad < 5:
        return 0.05
    elif antiguedad <= 10:  # Entre 5 y 10, ambos incluidos
        return 0.10
    else:  # Más de 10
        return 0.20


empleados = []

print("Carga de empleados (escriba 'salir' en el nombre para terminar)")
while True:
    nombre = input("\nNombre: ").strip()
    if nombre.lower() == "salir":  # lower() pasa a minúsculas: acepta "Salir", "SALIR", etc.
        break
    if not nombre:
        print("El nombre no puede quedar vacío.")
        continue
    sector = pedir_texto("Sector: ").upper()  # upper() pasa a mayúsculas: "it" → "IT", "ventas" → "VENTAS"
    sueldo_base = pedir_monto("Sueldo base: $")
    antiguedad = pedir_entero("Antigüedad (años): ")

    porcentaje = porcentaje_aumento(antiguedad)
    sueldo_final = sueldo_base * (1 + porcentaje)  # Ej.: 10% → sueldo_base * 1.10

    empleados.append({  # append() agrega el diccionario del empleado al final de la lista
        "nombre": nombre,
        "sector": sector,
        "sueldo_base": sueldo_base,
        "antiguedad": antiguedad,
        "porcentaje": porcentaje,
        "sueldo_final": sueldo_final,
    })

if not empleados:
    print("No se cargaron empleados.")
else:
    print("\n" + "=" * 72)  # "=" * 72 repite el carácter 72 veces para dibujar una línea
    print(f"{'INFORME DE SUELDOS':^72}")  # :^72 centra el texto en 72 caracteres
    print("=" * 72)
    # :<18 alinea a la izquierda en 18 lugares; :>13 a la derecha en 13
    print(f"{'Nombre':<18}{'Sector':<14}{'Antig.':>7}{'Base':>13}{'Aum.':>6}{'Final':>14}")
    print("-" * 72)
    for e in empleados:
        # :,.2f → separador de miles y 2 decimales / :.0% → muestra 0.1 como "10%"
        print(f"{e['nombre']:<18}{e['sector']:<14}{e['antiguedad']:>7}"
              f"{e['sueldo_base']:>13,.2f}{e['porcentaje']:>6.0%}{e['sueldo_final']:>14,.2f}")
    print("-" * 72)

    # sum() suma los sueldos finales y len() cuenta los empleados
    promedio = sum(e["sueldo_final"] for e in empleados) / len(empleados)
    print(f"Promedio general de sueldos finales: ${promedio:,.2f}")
