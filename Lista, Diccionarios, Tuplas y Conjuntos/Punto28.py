#Registrar pedidos de una cafetería donde cada pedido contiene: 
# número, cliente, lista de productos (nombre, cantidad, precio). El sistema debe:
#● Calcular el total de cada pedido.
#● Permitir buscar pedidos por cliente.
#● Mostrar el total facturado en el día.
#● Indicar el producto más vendido.

# Pedidos de ejemplo para poder probar. Cada pedido tiene una LISTA de productos (estructura anidada).
pedidos = [
    {"numero": 1, "cliente": "Ana", "productos": [
        {"nombre": "Café", "cantidad": 2, "precio": 2500.0},
        {"nombre": "Medialuna", "cantidad": 3, "precio": 900.0},
    ]},
    {"numero": 2, "cliente": "Luis", "productos": [
        {"nombre": "Tostado", "cantidad": 1, "precio": 4200.0},
        {"nombre": "Café", "cantidad": 1, "precio": 2500.0},
    ]},
]


def pedir_texto(mensaje):
    """Pide un dato por teclado y no permite que quede vacío."""
    while True:
        texto = input(mensaje).strip()  # strip() quita los espacios del principio y del final
        if texto:
            return texto
        print("Este dato no puede quedar vacío.")


def pedir_entero(mensaje, minimo=0):
    """Pide un número entero mayor o igual a 'minimo'."""
    while True:
        try:
            valor = int(input(mensaje))  # int() convierte el texto a entero
        except ValueError:
            print("Ingrese un número entero válido.")
            continue
        if valor >= minimo:
            return valor
        print(f"El valor debe ser mayor o igual a {minimo}.")


def pedir_monto(mensaje):
    """Pide un número decimal mayor a 0."""
    while True:
        try:
            monto = float(input(mensaje).replace(",", "."))  # replace(): acepta coma decimal; float(): a decimal
        except ValueError:
            print("Ingrese un monto válido.")
            continue
        if monto > 0:
            return monto
        print("El monto debe ser mayor a 0.")


def total_pedido(pedido):
    # sum() suma cantidad × precio de cada producto del pedido
    return sum(p["cantidad"] * p["precio"] for p in pedido["productos"])


def mostrar_pedido(pedido):
    print(f"\nPedido N° {pedido['numero']} - Cliente: {pedido['cliente']}")
    for p in pedido["productos"]:
        print(f"  {p['cantidad']} x {p['nombre']:<18} ${p['cantidad'] * p['precio']:>10,.2f}")
    print(f"  {'Total:':<22} ${total_pedido(pedido):>10,.2f}")


def registrar_pedido():
    # max(..., default=0) busca el número de pedido más alto; default evita el error si la lista está vacía
    numero = max((p["numero"] for p in pedidos), default=0) + 1
    cliente = pedir_texto("Cliente: ").title()  # title(): mayúscula al inicio de cada palabra
    productos = []
    print("Cargue los productos (deje el nombre vacío y presione Enter para terminar)")
    while True:
        nombre = input("  Producto: ").strip()
        if not nombre:
            if productos:  # Solo se puede terminar si hay al menos un producto
                break
            print("  El pedido debe tener al menos un producto.")
            continue
        cantidad = pedir_entero("  Cantidad: ", minimo=1)
        precio = pedir_monto("  Precio unitario: $")
        # capitalize() normaliza el nombre ("CAFÉ" y "café" → "Café") para poder sumar bien las ventas
        productos.append({"nombre": nombre.capitalize(), "cantidad": cantidad, "precio": precio})
    pedido = {"numero": numero, "cliente": cliente, "productos": productos}
    pedidos.append(pedido)  # append() agrega el pedido al final de la lista
    print(f"Pedido N° {numero} registrado.")
    mostrar_pedido(pedido)


def buscar_por_cliente():
    texto = pedir_texto("Nombre del cliente (o parte): ").lower()  # lower(): busca sin distinguir mayúsculas
    # "in" entre strings verifica si el texto buscado está contenido en el nombre del cliente
    encontrados = [p for p in pedidos if texto in p["cliente"].lower()]
    if not encontrados:
        print("No se encontraron pedidos para ese cliente.")
        return
    for pedido in encontrados:
        mostrar_pedido(pedido)


def total_facturado():
    if not pedidos:
        print("No hay pedidos registrados.")
        return
    for pedido in pedidos:
        print(f"  Pedido N° {pedido['numero']:<3} {pedido['cliente']:<15} ${total_pedido(pedido):>10,.2f}")
    total = sum(total_pedido(p) for p in pedidos)
    print(f"Pedidos del día: {len(pedidos)} | Total facturado: ${total:,.2f}")


def producto_mas_vendido():
    cantidades = {}  # Diccionario: nombre del producto → unidades vendidas
    for pedido in pedidos:
        for producto in pedido["productos"]:
            # get(clave, 0) devuelve el valor acumulado o 0 si el producto todavía no está
            cantidades[producto["nombre"]] = cantidades.get(producto["nombre"], 0) + producto["cantidad"]
    if not cantidades:
        print("No hay ventas registradas.")
        return
    # values() devuelve solo los valores del diccionario; max() busca el mayor
    maximo = max(cantidades.values())
    # Puede haber empate, por eso se buscan TODOS los productos con esa cantidad.
    # items() devuelve los pares (nombre, cantidad).
    mas_vendidos = [nombre for nombre, cantidad in cantidades.items() if cantidad == maximo]
    # join() une la lista de nombres en un solo texto separado por ", "
    print(f"Producto/s más vendido/s: {', '.join(mas_vendidos)} ({maximo} unidades)")


while True:
    print("\n=== CAFETERÍA ===")
    print("1. Registrar pedido")
    print("2. Ver total de cada pedido")
    print("3. Buscar pedidos por cliente")
    print("4. Total facturado en el día")
    print("5. Producto más vendido")
    print("6. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        registrar_pedido()
    elif opcion == "2":
        for pedido in pedidos:
            mostrar_pedido(pedido)
        if not pedidos:
            print("No hay pedidos registrados.")
    elif opcion == "3":
        buscar_por_cliente()
    elif opcion == "4":
        total_facturado()
    elif opcion == "5":
        producto_mas_vendido()
    elif opcion == "6":
        break
    else:
        print("Opción no válida.")
