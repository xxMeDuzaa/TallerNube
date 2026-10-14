# Pedir las notas de 10 alumnos y contar cuántos aprobaron (nota mayor o igual a 6)
notas = []
for i in range(10):
    nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
    notas.append(nota)

aprobados = sum(1 for nota in notas if nota >= 6)
print(f"El número de alumnos aprobados es: {aprobados}")