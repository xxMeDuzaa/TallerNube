#Ingresar la base y la altura de un rectángulo, calcular el área y el perímetro.

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: ")) 

area = base * altura
perimetro = 2 * (base + altura)

print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")