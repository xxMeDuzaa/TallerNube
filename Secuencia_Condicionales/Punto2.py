#Solicitar tres notas y mostrar el promedio e indicar si el alumno está aprobado o desaprobado.

#print("Ingrese tres notas:")
#nota1=float(input("Nota 1: "))
#nota2=float(input("Nota 2: "))
#nota3=float(input("Nota 3: "))

#promedio=(nota1+nota2+nota3)/3
#print("El promedio es: ")

#if promedio >= 6:
#    print(f"{promedio:.2f} El alumno está aprobado.")
#else:
#    print(f"{promedio:.2f} El alumno está desaprobado.")

# -----------------------------------------

total_notas = 0
contador = 0

for  i in range(1, 4):
    nota = float(input(f"Ingrese la nota {i}: "))  
    total_notas += nota
    contador += 1

promedio = total_notas / contador
if promedio >= 6:
    print(f"{promedio:.2f} El alumno está aprobado.")
else:
    print(f"{promedio:.2f} El alumno está desaprobado.")