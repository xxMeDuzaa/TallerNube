#Leer una lista de 8 números enteros y mostrar el mayor y el menor.
numeros = []
cantNumeros = 8

for i in range(cantNumeros):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

mayor = max(numeros)
menor = min(numeros)

print("El mayor es:", mayor)
print("El menor es:", menor)