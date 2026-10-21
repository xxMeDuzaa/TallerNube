#Registrar pacientes con sus datos personales y una lista de turnos 
# (fecha, médico, especialidad). Permitir:
#● Agregar nuevos pacientes.
#● Registrar un turno a un paciente existente.
#● Consultar todos los turnos por especialidad.
#● Mostrar el total de turnos por médico.

from datetime import date, datetime

# Cada paciente: {"dni", "nombre", "telefono", "turnos": [ {"fecha", "medico", "especialidad"}, ... ]}
# Es una estructura anidada: una lista de diccionarios, y cada diccionario tiene otra lista adentro.
pacientes = []


def pedir_texto(mensaje):
    """Pide un dato por teclado y no permite que quede vacío."""
    while True:
        texto = input(mensaje).strip()  # strip() quita los espacios del principio y del final
        if texto:
            return texto
        print("Este dato no puede quedar vacío.")


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


def buscar_paciente(dni):
    for paciente in pacientes:
        if paciente["dni"] == dni:
            return paciente
    return None


def agregar_paciente():
    dni = pedir_texto("DNI (solo números): ")
    if not dni.isdigit():  # isdigit() devuelve True si el texto tiene solo dígitos
        print("El DNI debe contener solo números.")
        return
    if buscar_paciente(dni) is not None:
        print("Ya existe un paciente con ese DNI.")
        return
    nombre = pedir_texto("Nombre y apellido: ").title()  # title(): "ana gómez" → "Ana Gómez"
    telefono = pedir_texto("Teléfono: ")
    # append() agrega el paciente al final de la lista; empieza sin turnos (lista vacía)
    pacientes.append({"dni": dni, "nombre": nombre, "telefono": telefono, "turnos": []})
    print("Paciente registrado.")


def registrar_turno():
    if not pacientes:
        print("Primero debe registrar al menos un paciente.")
        return
    paciente = buscar_paciente(pedir_texto("DNI del paciente: "))
    if paciente is None:
        print("No existe un paciente con ese DNI.")
        return
    fecha = pedir_fecha("Fecha del turno")
    if fecha < date.today():  # Las fechas se pueden comparar con < y >
        print("No se puede dar un turno en una fecha pasada.")
        return
    medico = pedir_texto("Médico: ").title()
    especialidad = pedir_texto("Especialidad: ").capitalize()  # capitalize(): primera letra en mayúscula
    # El turno se agrega a la lista de turnos DE ESE paciente
    paciente["turnos"].append({"fecha": fecha, "medico": medico, "especialidad": especialidad})
    print(f"Turno registrado para {paciente['nombre']} el {fecha.strftime('%d/%m/%Y')}.")


def turnos_por_especialidad():
    especialidad = pedir_texto("Especialidad a consultar: ").lower()  # lower(): compara sin mayúsculas
    encontrados = []
    for paciente in pacientes:  # Ciclo anidado: recorre pacientes y, dentro de cada uno, sus turnos
        for turno in paciente["turnos"]:
            if turno["especialidad"].lower() == especialidad:
                encontrados.append((turno, paciente))  # Tupla: guarda el turno junto con su paciente
    if not encontrados:
        print("No hay turnos para esa especialidad.")
        return
    print(f"Turnos de {especialidad.capitalize()}:")
    # sorted() ordena por fecha: t[0] es el turno dentro de la tupla (turno, paciente)
    for turno, paciente in sorted(encontrados, key=lambda t: t[0]["fecha"]):
        # strftime() convierte la fecha a texto con formato dd/mm/aaaa
        print(f"  {turno['fecha'].strftime('%d/%m/%Y')} | Dr/a. {turno['medico']} | "
              f"{paciente['nombre']} (DNI {paciente['dni']})")


def total_por_medico():
    totales = {}  # Diccionario: médico → cantidad de turnos
    for paciente in pacientes:
        for turno in paciente["turnos"]:
            # get(clave, 0) devuelve el valor actual o 0 si el médico todavía no está en el diccionario
            totales[turno["medico"]] = totales.get(turno["medico"], 0) + 1
    if not totales:
        print("No hay turnos registrados.")
        return
    print("Total de turnos por médico:")
    # items() devuelve los pares (médico, cantidad); se ordenan por cantidad de mayor a menor
    for medico, cantidad in sorted(totales.items(), key=lambda x: x[1], reverse=True):
        print(f"  Dr/a. {medico:<20} {cantidad} turno/s")


while True:
    print("\n=== TURNOS MÉDICOS ===")
    print("1. Agregar paciente")
    print("2. Registrar turno")
    print("3. Consultar turnos por especialidad")
    print("4. Total de turnos por médico")
    print("5. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_paciente()
    elif opcion == "2":
        registrar_turno()
    elif opcion == "3":
        turnos_por_especialidad()
    elif opcion == "4":
        total_por_medico()
    elif opcion == "5":
        break
    else:
        print("Opción no válida.")
