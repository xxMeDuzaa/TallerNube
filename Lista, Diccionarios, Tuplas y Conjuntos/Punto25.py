#Tener un catálogo de productos (nombre, precio, stock). 
# El usuario puede agregar productos al carrito indicando la cantidad. El programa debe:
#● Verificar que haya stock suficiente.
#● Descontar el stock al confirmar la compra.
#● Calcular el total a pagar.
#● Mostrar un ticket de compra detallado.

from datetime import datetime  # Para poner fecha y hora en el ticket

catalogo = [
    {"nombre": "Café", "precio": 2500.0, "stock": 10},
    {"nombre": "Medialuna", "precio": 900.0, "stock": 24},
    {"nombre": "Tostado", "precio": 4200.0, "stock": 5},
    {"nombre": "Jugo de naranja", "precio": 3000.0, "stock": 3},
]

# Cada ítem del carrito guarda una REFERENCIA al producto del catálogo y la cantidad elegida
carrito = []


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


def buscar_producto(nombre):
    for producto in catalogo:
        if producto["nombre"].lower() == nombre.lower():  # lower() compara sin distinguir mayúsculas
            return producto
    return None


def item_en_carrito(producto):
    """Devuelve el ítem del carrito que corresponde a ese producto, o None."""
    for item in carrito:
        if item["producto"] is producto:  # "is" verifica que sea exactamente el MISMO diccionario
            return item
    return None


def stock_disponible(producto):
    """Stock que todavía se puede agregar: el del catálogo menos lo que ya está en el carrito."""
    item = item_en_carrito(producto)
    reservado = item["cantidad"] if item else 0  # Operador ternario: valor_si_true if condición else valor_si_false
    return producto["stock"] - reservado


def total_carrito():
    # sum() suma el subtotal (precio × cantidad) de cada ítem
    return sum(item["producto"]["precio"] * item["cantidad"] for item in carrito)


def mostrar_catalogo():
    print(f"\n{'Producto':<18}{'Precio':>10}{'Stock':>7}")
    for producto in catalogo:
        print(f"{producto['nombre']:<18}{producto['precio']:>10,.2f}{stock_disponible(producto):>7}")


def agregar_al_carrito():
    producto = buscar_producto(pedir_texto("Producto: "))
    if producto is None:
        print("Ese producto no está en el catálogo.")
        return
    disponible = stock_disponible(producto)
    if disponible == 0:
        print("No hay stock disponible de ese producto.")
        return
    cantidad = pedir_entero(f"Cantidad (disponible: {disponible}): ", minimo=1)
    if cantidad > disponible:  # Verificación de stock suficiente
        print(f"Stock insuficiente. Solo quedan {disponible} unidad/es.")
        return
    item = item_en_carrito(producto)
    if item:  # Si el producto ya estaba en el carrito, se suma la cantidad
        item["cantidad"] += cantidad
    else:
        carrito.append({"producto": producto, "cantidad": cantidad})  # append() agrega al final
    print(f"Agregado: {cantidad} x {producto['nombre']}")


def mostrar_carrito():
    if not carrito:  # Una lista vacía se evalúa como False
        print("El carrito está vacío.")
        return
    print("\nCarrito:")
    for item in carrito:
        subtotal = item["producto"]["precio"] * item["cantidad"]
        print(f"  {item['cantidad']} x {item['producto']['nombre']:<18} ${subtotal:>10,.2f}")
    print(f"  Total a pagar: ${total_carrito():,.2f}")


def confirmar_compra():
    if not carrito:
        print("El carrito está vacío.")
        return
    # Se vuelve a verificar el stock antes de descontar, por seguridad
    for item in carrito:
        if item["cantidad"] > item["producto"]["stock"]:
            print(f"Stock insuficiente de {item['producto']['nombre']}. Compra cancelada.")
            return

    ancho = 44
    total = total_carrito()
    print("\n" + "=" * ancho)  # "=" * ancho repite el carácter para dibujar una línea
    print(f"{'TICKET DE COMPRA':^{ancho}}")  # :^ centra el texto
    # datetime.now() devuelve la fecha y hora actual; strftime() la convierte a texto con ese formato
    print(datetime.now().strftime("Fecha: %d/%m/%Y   Hora: %H:%M"))
    print("-" * ancho)
    print(f"{'Producto':<18}{'Cant.':>5}{'P. unit.':>10}{'Subtotal':>11}")
    for item in carrito:
        producto = item["producto"]
        subtotal = producto["precio"] * item["cantidad"]
        print(f"{producto['nombre']:<18}{item['cantidad']:>5}{producto['precio']:>10,.2f}{subtotal:>11,.2f}")
        producto["stock"] -= item["cantidad"]  # Descuenta el stock del catálogo (-= resta y asigna)
    print("-" * ancho)
    print(f"{'TOTAL A PAGAR:':<33}{total:>11,.2f}")
    print("=" * ancho)
    print("¡Gracias por su compra!")
    carrito.clear()  # clear() vacía la lista para poder empezar una compra nueva


while True:
    print("\n=== TIENDA ===")
    print("1. Ver catálogo")
    print("2. Agregar producto al carrito")
    print("3. Ver carrito")
    print("4. Confirmar compra")
    print("5. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        mostrar_catalogo()
    elif opcion == "2":
        agregar_al_carrito()
    elif opcion == "3":
        mostrar_carrito()
    elif opcion == "4":
        confirmar_compra()
    elif opcion == "5":
        if carrito:
            print("Se descartó el carrito sin confirmar.")
        break
    else:
        print("Opción no válida.")
