#Crear una lista de alumnos (nombre, DNI) y una lista de cursos (nombre del curso, cupo). 
# El usuario podrá inscribir alumnos en cursos si hay cupos disponibles. Al finalizar, mostrar:
#● Listado de alumnos por curso.
#● Cursos que aún tienen cupos.
#● Cantidad total de inscriptos.

# Datos de ejemplo. El DNI se guarda como texto porque no se usa para hacer cuentas.
alumnos = [
    {"nombre": "Ana Gómez", "dni": "40111222"},
    {"nombre": "Luis Pérez", "dni": "41222333"},
    {"nombre": "Sol Díaz", "dni": "42333444"},
]

# "inscriptos" es una lista con los DNI de los alumnos anotados en ese curso
cursos = [
    {"nombre": "Python", "cupo": 2, "inscriptos": []},
    {"nombre": "Bases de Datos", "cupo": 3, "inscriptos": []},
    {"nombre": "Redes", "cupo": 1, "inscriptos": []},
]


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


def buscar_alumno(dni):
    for alumno in alumnos:
        if alumno["dni"] == dni:
            return alumno
    return None


def buscar_curso(nombre):
    for curso in cursos:
        if curso["nombre"].lower() == nombre.lower():  # lower() compara sin distinguir mayúsculas
            return curso
    return None


def cupos_libres(curso):
    # len() cuenta cuántos DNI hay en la lista de inscriptos
    return curso["cupo"] - len(curso["inscriptos"])


def agregar_alumno():
    nombre = pedir_texto("Nombre y apellido: ").title()  # title() pone en mayúscula la inicial de cada palabra
    dni = pedir_texto("DNI (solo números): ")
    if not dni.isdigit():  # isdigit() devuelve True si el texto tiene solo dígitos
        print("El DNI debe contener solo números.")
        return
    if buscar_alumno(dni) is not None:
        print("Ya existe un alumno con ese DNI.")
        return
    alumnos.append({"nombre": nombre, "dni": dni})  # append() agrega al final de la lista
    print("Alumno agregado.")


def agregar_curso():
    nombre = pedir_texto("Nombre del curso: ")
    if buscar_curso(nombre) is not None:
        print("Ese curso ya existe.")
        return
    cupo = pedir_entero("Cupo: ", minimo=1)
    cursos.append({"nombre": nombre, "cupo": cupo, "inscriptos": []})
    print("Curso agregado.")


def inscribir():
    # Solo se ofrecen los cursos que todavía tienen lugar
    disponibles = [curso for curso in cursos if cupos_libres(curso) > 0]
    if not disponibles:
        print("No hay cursos con cupos disponibles.")
        return
    print("Cursos con cupo:")
    for curso in disponibles:
        print(f"  - {curso['nombre']} ({cupos_libres(curso)} lugar/es)")

    dni = pedir_texto("DNI del alumno: ")
    alumno = buscar_alumno(dni)
    if alumno is None:
        print("No existe un alumno con ese DNI (cárguelo primero con la opción 1).")
        return
    curso = buscar_curso(pedir_texto("Nombre del curso: "))
    if curso is None:
        print("No existe ese curso.")
        return
    if dni in curso["inscriptos"]:  # "in" verifica si el DNI ya está en la lista
        print(f"{alumno['nombre']} ya está inscripto/a en {curso['nombre']}.")
        return
    if cupos_libres(curso) == 0:
        print("El curso no tiene cupos disponibles.")
        return
    curso["inscriptos"].append(dni)  # Se agrega el DNI a la lista de inscriptos de ESE curso
    print(f"{alumno['nombre']} quedó inscripto/a en {curso['nombre']}.")


def informe_final():
    print("\n===== LISTADO DE ALUMNOS POR CURSO =====")
    for curso in cursos:
        print(f"\n{curso['nombre']} ({len(curso['inscriptos'])}/{curso['cupo']})")
        if not curso["inscriptos"]:
            print("  Sin inscriptos")
        for dni in curso["inscriptos"]:
            print(f"  - {buscar_alumno(dni)['nombre']} (DNI {dni})")

    print("\n===== CURSOS QUE AÚN TIENEN CUPOS =====")
    con_cupo = [curso for curso in cursos if cupos_libres(curso) > 0]
    if con_cupo:
        for curso in con_cupo:
            print(f"  - {curso['nombre']}: {cupos_libres(curso)} lugar/es libre/s")
    else:
        print("  Todos los cursos están completos.")

    # sum() suma la cantidad de inscriptos de cada curso
    total_inscripciones = sum(len(curso["inscriptos"]) for curso in cursos)
    # set(): conjunto sin repetidos. Si un alumno está en 2 cursos, su DNI se guarda una sola vez.
    alumnos_distintos = set()
    for curso in cursos:
        alumnos_distintos.update(curso["inscriptos"])  # update() agrega al set todos los elementos de la lista
    print(f"\nCantidad total de inscripciones: {total_inscripciones}")
    print(f"Alumnos distintos inscriptos: {len(alumnos_distintos)}")


while True:
    print("\n=== INSCRIPCIONES ===")
    print("1. Agregar alumno")
    print("2. Agregar curso")
    print("3. Inscribir alumno en un curso")
    print("4. Finalizar y mostrar informe")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_alumno()
    elif opcion == "2":
        agregar_curso()
    elif opcion == "3":
        inscribir()
    elif opcion == "4":
        informe_final()
        break
    else:
        print("Opción no válida.")
