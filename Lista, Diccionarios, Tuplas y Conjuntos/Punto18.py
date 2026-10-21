#Cargar una lista de diccionarios con producto, cantidad y precio unitario.
#Calcular el total de ventas (cantidad × precio_unitario).

# CORRECCIÓN: en la versión anterior el primer producto tenía la clave "precio_unitario  "
# (con espacios al final), y eso provocaba un KeyError al buscar "precio_unitario".
ventas = [
    {"producto": "Producto 1", "cantidad": 3, "precio_unitario": 10.0},
    {"producto": "Producto 2", "cantidad": 5, "precio_unitario": 20.0},
    {"producto": "Producto 3", "cantidad": 2, "precio_unitario": 15.0},
]

total_ventas = 0

# Encabezado de la tabla: ":<12" alinea a la izquierda en 12 caracteres y ":>10" a la derecha en 10
print(f"{'Producto':<12}{'Cant.':>6}{'P. unit.':>10}{'Subtotal':>11}")
for venta in ventas:
    subtotal = venta["cantidad"] * venta["precio_unitario"]
    total_ventas += subtotal  # += acumula: equivale a total_ventas = total_ventas + subtotal
    # ":.2f" muestra el número con 2 decimales
    print(f"{venta['producto']:<12}{venta['cantidad']:>6}{venta['precio_unitario']:>10.2f}{subtotal:>11.2f}")

print("-" * 39)  # "-" * 39 repite el guion 39 veces para dibujar una línea
print(f"Total de ventas: ${total_ventas:.2f}")

# Forma corta equivalente: sum() suma todos los valores que genera la expresión
# total_ventas = sum(v["cantidad"] * v["precio_unitario"] for v in ventas)
