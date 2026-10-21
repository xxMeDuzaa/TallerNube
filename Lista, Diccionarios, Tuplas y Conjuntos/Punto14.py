#Ingresar una lista con números repetidos y mostrar la misma lista sin repeticiones.

numeros = []

while True:
    try:
        numero = int(input("Ingrese un número (o escriba 'salir' para terminar): "))
        numeros.append(numero)
    except ValueError:
        break

# Eliminar repeticiones
numeros_sin_repeticiones = list(set(numeros)) #set elimina los elementos repetidos y luego se convierte de nuevo a lista

print("Lista sin repeticiones:", numeros_sin_repeticiones)