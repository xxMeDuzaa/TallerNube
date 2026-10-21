#Cargar una lista donde cada elemento sea un diccionario con nombre y nota. Mostrar los nombres de los alumnos aprobados.

alumnos = []

while True:
    nombre = input("Ingrese el nombre del alumno (o 'salir' para terminar): ").strip()
    if nombre.lower() == "salir":
        break
    while True:
        try:
            nota = float(input("Ingrese la nota del alumno: "))
            if 0 <= nota <= 10:
                break
            print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Ingrese un número válido.")
    alumnos.append({"nombre": nombre, "nota": nota})

aprobados = [a["nombre"] for a in alumnos if a["nota"] >= 6]
if aprobados:
    print("Alumnos aprobados:")
    for nombre in aprobados:
        print(nombre)
else:
    print("Ningún alumno aprobó.")
