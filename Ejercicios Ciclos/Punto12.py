# Cargar una lista de productos y preguntar al usuario por un nombre. Indicar si está o no en la lista.
productos = ["manzana", "banana", "naranja", "pera", "uva"]
nombre_producto = input("Ingrese el nombre del producto que desea buscar: ")

if nombre_producto in productos:
    print(f"El producto '{nombre_producto}' está en la lista.")
else:
    print(f"El producto '{nombre_producto}' no está en la lista.")