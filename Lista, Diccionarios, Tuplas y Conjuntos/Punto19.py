#Cada estudiante tiene un nombre y una lista de materias. 
# Mostrar los alumnos que cursan más de 3 materias.

MINIMO_MATERIAS = 3

# Cada estudiante es un diccionario, y su clave "materias" guarda una LISTA (estructura anidada)
estudiantes = [
    {"nombre": "Estudiante 1", "materias": ["Matemáticas", "Física", "Química"]},
    {"nombre": "Estudiante 2", "materias": ["Historia", "Geografía", "Lengua", "Inglés"]},
    {"nombre": "Estudiante 3", "materias": ["Biología", "Matemáticas"]},
    {"nombre": "Estudiante 4", "materias": ["Arte", "Música", "Educación Física", "Tecnología", "Informática"]},
]

# Comprensión de lista: guarda los estudiantes cuya lista de materias tiene más de 3 elementos.
# len() devuelve la cantidad de elementos de la lista de materias.
estudiantes_con_mas_materias = [
    estudiante for estudiante in estudiantes if len(estudiante["materias"]) > MINIMO_MATERIAS
]

if estudiantes_con_mas_materias:  # Una lista con elementos se evalúa como True
    print(f"Estudiantes que cursan más de {MINIMO_MATERIAS} materias:")
    for estudiante in estudiantes_con_mas_materias:
        # join() une los elementos de la lista en un solo texto, usando ", " como separador
        materias = ", ".join(estudiante["materias"])
        print(f" - {estudiante['nombre']} ({len(estudiante['materias'])}): {materias}")
else:
    print(f"Ningún estudiante cursa más de {MINIMO_MATERIAS} materias.")
