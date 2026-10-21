#Cargar una lista de estudiantes, cada uno con 
# su nombre y una lista de notas. El sistema debe:
#● Calcular el promedio individual.
#● Indicar si aprueba (promedio ≥ 6).
#● Calcular el promedio general del curso.
#● Mostrar los 3 mejores promedios.

NOTA_APROBACION = 6


def promedio(numeros):
    """Devuelve el promedio de una lista de números."""
    return sum(numeros) / len(numeros)  # sum() suma todos los elementos; len() los cuenta


def pedir_notas(nombre):
    """Pide las notas en una sola línea, separadas por espacios, y devuelve una lista de floats."""
    while True:
        texto = input(f"Notas de {nombre} separadas por espacios (ej.: 7 8,5 6): ")
        try:
            # split() separa el texto por los espacios y devuelve una lista de strings: "7 8 6" → ["7", "8", "6"]
            # replace(",", ".") permite usar coma decimal (8,5 → 8.5)
            # la comprensión de lista convierte cada string a float
            notas = [float(n.replace(",", ".")) for n in texto.split()]
        except ValueError:
            print("Hay un valor que no es un número. Intente de nuevo.")
            continue
        if not notas:
            print("Ingrese al menos una nota.")
            continue
        # all() devuelve True solo si TODAS las notas cumplen la condición
        if not all(0 <= nota <= 10 for nota in notas):
            print("Todas las notas deben estar entre 0 y 10.")
            continue
        return notas


estudiantes = []

print("Carga de estudiantes (escriba 'salir' en el nombre para terminar)")
while True:
    nombre = input("\nNombre del estudiante: ").strip()  # strip() quita espacios al principio y al final
    if nombre.lower() == "salir":  # lower() pasa a minúsculas
        break
    if not nombre:
        print("El nombre no puede quedar vacío.")
        continue
    notas = pedir_notas(nombre)
    # Se guarda el promedio ya calculado para no repetir la cuenta después
    estudiantes.append({"nombre": nombre, "notas": notas, "promedio": promedio(notas)})  # append(): agrega al final

if not estudiantes:
    print("No se cargaron estudiantes.")
else:
    print(f"\n{'Estudiante':<18}{'Notas':<22}{'Promedio':>9}  Estado")
    print("-" * 62)
    for e in estudiantes:
        # join() une los textos de la lista usando ", " como separador.
        # :g muestra el número sin decimales innecesarios (8.0 → 8, 8.5 → 8.5)
        notas_texto = ", ".join(f"{n:g}" for n in e["notas"])
        estado = "Aprobado" if e["promedio"] >= NOTA_APROBACION else "Desaprobado"  # Operador ternario
        print(f"{e['nombre']:<18}{notas_texto:<22}{e['promedio']:>9.2f}  {estado}")

    # Promedio general del curso = promedio de los promedios individuales
    promedio_general = promedio([e["promedio"] for e in estudiantes])
    print(f"\nPromedio general del curso: {promedio_general:.2f}")

    print("\nMejores promedios:")
    # sorted() ordena por promedio de mayor a menor; [:3] toma los 3 primeros (o menos si no hay 3)
    mejores = sorted(estudiantes, key=lambda e: e["promedio"], reverse=True)[:3]
    # enumerate() devuelve (posición, elemento); start=1 empieza a contar desde 1
    for posicion, e in enumerate(mejores, start=1):
        print(f"  {posicion}. {e['nombre']}: {e['promedio']:.2f}")
