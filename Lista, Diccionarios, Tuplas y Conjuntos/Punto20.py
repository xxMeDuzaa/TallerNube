#Ingresar una lista de jugadores con nombre y puntaje. 
# Ordenar la lista de mayor a menor puntaje y mostrar el podio (los 3 primeros).

# MEJORA: el enunciado pide "ingresar", así que ahora los jugadores se cargan por teclado
jugadores = []

print("Carga de jugadores (escriba 'salir' en el nombre para terminar)")
while True:
    nombre = input("\nNombre del jugador: ").strip()  # strip() quita espacios al principio y al final
    if nombre.lower() == "salir":  # lower() pasa a minúsculas: acepta "Salir", "SALIR", etc.
        break
    if not nombre:
        print("El nombre no puede quedar vacío.")
        continue  # continue salta directamente a la siguiente vuelta del while

    while True:
        try:
            puntaje = int(input(f"Puntaje de {nombre}: "))  # int() convierte el texto a entero
            if puntaje >= 0:
                break
            print("El puntaje no puede ser negativo.")
        except ValueError:  # int() lanza ValueError si el texto no es un número
            print("Ingrese un número entero.")

    jugadores.append({"nombre": nombre, "puntaje": puntaje})  # append() agrega al final de la lista

if not jugadores:
    print("No se cargaron jugadores.")
else:
    # sorted() devuelve una lista NUEVA ordenada (la original no se modifica).
    # key=lambda j: j["puntaje"] indica que se ordene usando el puntaje de cada jugador.
    # reverse=True ordena de mayor a menor.
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["puntaje"], reverse=True)

    print("\nRanking completo:")
    # enumerate() devuelve (posición, elemento) en cada vuelta; start=1 hace que cuente desde 1
    for posicion, jugador in enumerate(jugadores_ordenados, start=1):
        print(f"{posicion}. {jugador['nombre']}: {jugador['puntaje']} puntos")

    print("\nPodio:")
    # [:3] es slicing: toma los elementos desde el inicio hasta la posición 3 (sin incluirla).
    # Si hay menos de 3 jugadores, devuelve los que haya sin dar error.
    for posicion, jugador in enumerate(jugadores_ordenados[:3], start=1):
        print(f"  Puesto {posicion}: {jugador['nombre']} ({jugador['puntaje']} puntos)")
