#Crear un programa que permita registrar libros (título, autor, año y estado: disponible o prestado). El usuario debe poder:
#● Agregar nuevos libros.
#● Buscar libros por título o autor.
#● Prestar un libro (cambiar su estado).
#● Mostrar todos los libros disponibles.

from datetime import (
    date,  # date sirve para trabajar con fechas; acá se usa para saber el año actual
)

ANIO_ACTUAL = date.today().year 

# Cada libro es un diccionario. Se cargan algunos de ejemplo para poder probar el programa.
libros = [
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "anio": 1963, "estado": "disponible"},
    {"titulo": "Ficciones", "autor": "Jorge Luis Borges", "anio": 1944, "estado": "disponible"},
    {"titulo": "El túnel", "autor": "Ernesto Sabato", "anio": 1948, "estado": "prestado"},
]


def pedir_texto(mensaje):
    """Pide un dato por teclado y no permite que quede vacío."""
    while True:
        texto = input(mensaje).strip()  # strip() quita los espacios del principio y del final
        if texto:
            return texto
        print("Este dato no puede quedar vacío.")


def pedir_anio():
    """Pide un año válido (entero entre 1 y el año actual)."""
    while True:
        try:
            anio = int(input("Año de publicación: "))  # int() convierte el texto a entero
        except ValueError:  # Si el texto no es un número, int() lanza ValueError
            print("Ingrese un año válido (solo números).")
            continue
        if 1 <= anio <= ANIO_ACTUAL:  # Comparación encadenada: anio >= 1 y anio <= ANIO_ACTUAL
            return anio
        print(f"El año debe estar entre 1 y {ANIO_ACTUAL}.")


def mostrar_libro(libro):
    print(f"  - {libro['titulo']} | {libro['autor']} | {libro['anio']} | {libro['estado']}")


def buscar_por_titulo(titulo):
    """Devuelve el libro con ese título exacto (sin distinguir mayúsculas) o None."""
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():  # lower() pasa a minúsculas para comparar
            return libro
    return None


def agregar_libro():
    titulo = pedir_texto("Título: ")
    if buscar_por_titulo(titulo) is not None:
        print("Ese libro ya está registrado.")
        return
    autor = pedir_texto("Autor: ")
    anio = pedir_anio()
    # append() agrega el nuevo libro al final de la lista. Todo libro nuevo empieza disponible.
    libros.append({"titulo": titulo, "autor": autor, "anio": anio, "estado": "disponible"})
    print("Libro agregado.")


def buscar_libros():
    texto = pedir_texto("Ingrese parte del título o del autor: ").lower()
    # "in" entre dos strings verifica si uno está CONTENIDO en el otro: "bor" in "jorge luis borges" → True.
    # Así se encuentran coincidencias parciales, en el título o en el autor.
    resultados = [
        libro for libro in libros
        if texto in libro["titulo"].lower() or texto in libro["autor"].lower()
    ]
    if resultados:
        print(f"Se encontraron {len(resultados)} libro/s:")  # len() cuenta los elementos de la lista
        for libro in resultados:
            mostrar_libro(libro)
    else:
        print("No se encontraron libros.")


def cambiar_estado(nuevo_estado):
    """Presta o devuelve un libro, según el estado que reciba ("prestado" o "disponible")."""
    titulo = pedir_texto("Título exacto del libro: ")
    libro = buscar_por_titulo(titulo)
    if libro is None:
        print("No existe un libro con ese título.")
        return
    if libro["estado"] == nuevo_estado:
        print(f"El libro ya está {nuevo_estado}.")
        return
    # Al modificar este diccionario se modifica el que está dentro de la lista: es el MISMO objeto
    libro["estado"] = nuevo_estado
    print(f"'{libro['titulo']}' ahora está {nuevo_estado}.")


def mostrar_disponibles():
    disponibles = [libro for libro in libros if libro["estado"] == "disponible"]
    if not disponibles:
        print("No hay libros disponibles.")
        return
    print("Libros disponibles:")
    # sorted() devuelve una copia ordenada; key indica que se ordene por título
    for libro in sorted(disponibles, key=lambda l: l["titulo"]):
        mostrar_libro(libro)


while True:
    print("\n=== BIBLIOTECA ===")
    print("1. Agregar libro")
    print("2. Buscar libro por título o autor")
    print("3. Prestar libro")
    print("4. Devolver libro (extra)")
    print("5. Mostrar libros disponibles")
    print("6. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        buscar_libros()
    elif opcion == "3":
        cambiar_estado("prestado")
    elif opcion == "4":
        cambiar_estado("disponible")
    elif opcion == "5":
        mostrar_disponibles()
    elif opcion == "6":
        break
    else:
        print("Opción no válida.")
