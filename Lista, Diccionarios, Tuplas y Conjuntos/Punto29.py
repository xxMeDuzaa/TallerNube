#Administrador de tareas (To-Do List): Permitir al usuario crear tareas con:
#título, descripción, fecha límite y estado (pendiente o completada).
#Funcionalidades:
#● Agregar nuevas tareas.
#● Marcar tareas como completadas.
#● Mostrar las tareas pendientes ordenadas por fecha.
#● Eliminar tareas finalizadas.

from datetime import date, datetime

# Cada tarea: {"id", "titulo", "descripcion", "fecha_limite": date, "estado": "pendiente"/"completada"}
# El "id" es un número único que permite elegir una tarea sin escribir el título completo.
tareas = []


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


def listar(lista):
    """Muestra una lista de tareas, marcando las pendientes que ya vencieron."""
    hoy = date.today()
    for t in lista:
        vencida = t["estado"] == "pendiente" and t["fecha_limite"] < hoy  # Las fechas se comparan con < y >
        aviso = "  (VENCIDA)" if vencida else ""  # Operador ternario
        # strftime() convierte la fecha a texto con formato dd/mm/aaaa
        print(f"  [{t['id']}] {t['fecha_limite'].strftime('%d/%m/%Y')} - {t['titulo']}{aviso}")
        if t["descripcion"]:
            print(f"        {t['descripcion']}")


def agregar_tarea():
    # max(..., default=0) busca el id más alto; default evita el error con la lista vacía
    nuevo_id = max((t["id"] for t in tareas), default=0) + 1
    titulo = pedir_texto("Título: ")
    descripcion = input("Descripción (opcional): ").strip()
    fecha_limite = pedir_fecha("Fecha límite")
    tareas.append({  # append() agrega la tarea al final de la lista
        "id": nuevo_id,
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha_limite": fecha_limite,
        "estado": "pendiente",
    })
    print(f"Tarea [{nuevo_id}] agregada.")


def marcar_completada():
    pendientes = [t for t in tareas if t["estado"] == "pendiente"]
    if not pendientes:
        print("No hay tareas pendientes.")
        return
    listar(pendientes)
    id_tarea = pedir_entero("ID de la tarea a completar: ", minimo=1)
    for t in pendientes:
        if t["id"] == id_tarea:
            t["estado"] = "completada"  # Modifica el diccionario que está dentro de la lista 'tareas'
            print(f"Tarea '{t['titulo']}' marcada como completada.")
            return
    print("No hay una tarea pendiente con ese ID.")


def mostrar_pendientes():
    pendientes = [t for t in tareas if t["estado"] == "pendiente"]
    if not pendientes:
        print("No hay tareas pendientes.")
        return
    print("Tareas pendientes (de la más próxima a la más lejana):")
    # sorted() ordena por fecha límite: los objetos date se comparan directamente
    listar(sorted(pendientes, key=lambda t: t["fecha_limite"]))


def eliminar_finalizadas():
    cantidad = sum(1 for t in tareas if t["estado"] == "completada")  # Cuenta las completadas
    if cantidad == 0:
        print("No hay tareas finalizadas para eliminar.")
        return
    # tareas[:] = ... reemplaza el CONTENIDO de la lista por las tareas no completadas.
    # Se usa [:] para modificar la misma lista global; sin [:] se crearía una variable local nueva.
    tareas[:] = [t for t in tareas if t["estado"] != "completada"]
    print(f"Se eliminaron {cantidad} tarea/s finalizada/s.")


while True:
    print("\n=== TO-DO LIST ===")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas pendientes")
    print("4. Eliminar tareas finalizadas")
    print("5. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        marcar_completada()
    elif opcion == "3":
        mostrar_pendientes()
    elif opcion == "4":
        eliminar_finalizadas()
    elif opcion == "5":
        break
    else:
        print("Opción no válida.")
