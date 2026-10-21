#Permitir ingresar varios contactos con nombre, teléfono y email. 
# Buscar un contacto por nombre y mostrar sus datos.

contactos = []  # Lista vacía donde se guarda un diccionario por cada contacto


def pedir_texto(mensaje):
    """Pide un dato por teclado y no permite que quede vacío."""
    while True:
        texto = input(mensaje).strip()  # strip() quita los espacios del principio y del final
        if texto:  # Un string vacío ("") se evalúa como False
            return texto
        print("Este dato no puede quedar vacío.")


def buscar_por_nombre(nombre):
    """Devuelve el contacto con ese nombre o None si no existe."""
    for contacto in contactos:
        # lower() pasa el texto a minúsculas: así "Ana" y "ana" se consideran iguales
        if contacto["nombre"].lower() == nombre.lower():
            return contacto
    return None


def agregar_contacto():
    nombre = pedir_texto("Ingrese el nombre del contacto: ")
    if buscar_por_nombre(nombre) is not None:
        print("Ya existe un contacto con ese nombre.")
        return
    telefono = pedir_texto("Ingrese el teléfono del contacto: ")
    email = pedir_texto("Ingrese el email del contacto: ")
    # "in" verifica si un texto está contenido dentro de otro (validación simple de email)
    while "@" not in email or "." not in email:
        print("Email inválido (debe contener '@' y '.').")
        email = pedir_texto("Ingrese el email del contacto: ")
    # append() agrega el diccionario al final de la lista
    contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
    print("Contacto agregado.")


def buscar_contacto():
    if not contactos:  # Una lista vacía se evalúa como False
        print("Todavía no hay contactos cargados.")
        return
    nombre = pedir_texto("Ingrese el nombre del contacto a buscar: ")
    contacto = buscar_por_nombre(nombre)
    if contacto is None:
        print("Contacto no encontrado.")
    else:
        print(f"Nombre: {contacto['nombre']}")
        print(f"Teléfono: {contacto['telefono']}")
        print(f"Email: {contacto['email']}")


while True:
    print("\n1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        break
    else:
        print("Opción no válida.")
