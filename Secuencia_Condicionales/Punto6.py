#Ingresar la edad de una persona y decir si puede entrar a un evento (solo mayores de 18 años).

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Puede entrar al evento.")
else:
    print("No puede entrar al evento.")