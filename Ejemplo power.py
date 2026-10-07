cantidad =int(input("Ingrese la cantidad de montoas a verificar: "))
print(cantidad)

for i in range(cantidad):
    monto = int(input("Ingrese el monto: "))
    if monto > 1500:
        descuento = monto * 0.20
    else:
        descuento = monto * 0.10
    total = monto - descuento
    print(f"El descuento es: {descuento}")
    print(f"El total es: {total}")
