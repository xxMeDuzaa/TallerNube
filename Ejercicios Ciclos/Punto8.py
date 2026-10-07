#Solicitar al usuario ingresar 5 nombres y luego imprimirlos en orden inverso.

nombres = input("Ingrese 5 nombres separados por comas: ").split(",")
nombres.reverse()
for nombre in nombres:
    print(nombre)