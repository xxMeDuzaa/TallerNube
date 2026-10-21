#Crear una lista de productos, cada uno con nombre, precio y stock. 
# Mostrar el total de productos con stock menor a 5.

STOCK_MINIMO = 5  # Constante (en mayúsculas por convención): límite para considerar "stock bajo"

# Lista de diccionarios: cada producto es un diccionario con las claves nombre, precio y stock
productos = [
    {"nombre": "Yerba", "precio": 3500.0, "stock": 3},
    {"nombre": "Azúcar", "precio": 1200.0, "stock": 7},
    {"nombre": "Café", "precio": 6800.0, "stock": 2},
    {"nombre": "Galletitas", "precio": 1500.0, "stock": 1},
    {"nombre": "Leche", "precio": 1300.0, "stock": 12},
]

# Comprensión de lista: arma una lista NUEVA solo con los productos que cumplen la condición
productos_bajo_stock = [producto for producto in productos if producto["stock"] < STOCK_MINIMO]

# len() devuelve la cantidad de elementos de una lista
print(f"Total de productos con stock menor a {STOCK_MINIMO}: {len(productos_bajo_stock)}")

# Además del total, se muestra cuáles son (útil para saber qué reponer)
for producto in productos_bajo_stock:
    print(f" - {producto['nombre']}: {producto['stock']} unidad/es")
