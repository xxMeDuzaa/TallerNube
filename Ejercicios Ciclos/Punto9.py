#Ingresar una lista de 10 números y mostrar el promedio.
nota = 0
cantNotas = 10

for i in range(cantNotas):
    nota += float(input(f"Ingrese el número {i + 1}: "))
    
print("El promedio es:", nota / cantNotas)
