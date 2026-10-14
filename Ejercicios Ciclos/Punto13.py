# Cargar una lista con 5 números y mostrar la suma total.
numeros = []
for i in range(5):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

suma = sum(numeros)
print("La suma total es:", suma)