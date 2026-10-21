# TallerNube — Guía de estudio de Python 🐍

Repositorio de ejercicios del taller, más un **resumen técnico del lenguaje** pensado para repasar antes de un parcial o como referencia rápida. Arranca por lo básico (lo que ya está en los ejercicios) y avanza hacia temas intermedios y avanzados: funciones, excepciones, archivos, programación orientada a objetos, iteradores, generadores, decoradores, módulos, tipado y buenas prácticas.

> Todos los ejemplos son para **Python 3.10+**. Podés probarlos en la consola interactiva (`python` o `py` en Windows) copiando y pegando.

---

## Índice

1. [Estructura del repositorio](#1-estructura-del-repositorio)
2. [Cómo ejecutar Python](#2-cómo-ejecutar-python)
3. [Qué es Python y cómo funciona](#3-qué-es-python-y-cómo-funciona)
4. [Sintaxis básica, variables y tipos](#4-sintaxis-básica-variables-y-tipos)
5. [Operadores](#5-operadores)
6. [Strings (cadenas) en profundidad](#6-strings-cadenas-en-profundidad)
7. [Entrada y salida](#7-entrada-y-salida)
8. [Condicionales y `match`](#8-condicionales-y-match)
9. [Ciclos](#9-ciclos)
10. [Estructuras de datos (repaso y más allá)](#10-estructuras-de-datos-repaso-y-más-allá)
11. [Comprensiones](#11-comprensiones)
12. [Funciones](#12-funciones)
13. [Alcance de variables (scope)](#13-alcance-de-variables-scope)
14. [Manejo de errores y excepciones](#14-manejo-de-errores-y-excepciones)
15. [Archivos](#15-archivos)
16. [Módulos, paquetes y entornos virtuales](#16-módulos-paquetes-y-entornos-virtuales)
17. [Programación orientada a objetos](#17-programación-orientada-a-objetos)
18. [Iteradores y generadores](#18-iteradores-y-generadores)
19. [Funciones de orden superior, `lambda` y decoradores](#19-funciones-de-orden-superior-lambda-y-decoradores)
20. [Context managers (`with`)](#20-context-managers-with)
21. [Type hints (anotaciones de tipo)](#21-type-hints-anotaciones-de-tipo)
22. [Biblioteca estándar: lo más útil](#22-biblioteca-estándar-lo-más-útil)
23. [Testing básico](#23-testing-básico)
24. [Estilo y buenas prácticas (PEP 8)](#24-estilo-y-buenas-prácticas-pep-8)
25. [Errores y trampas comunes](#25-errores-y-trampas-comunes)
26. [Machete final](#26-machete-final)

---

## 1. Estructura del repositorio

| Carpeta / archivo | Tema | Contenido |
|---|---|---|
| `Holamundo.py` | Primer programa | `print("Hola Mundo")` |
| `Secuencia_Condicionales/` | Secuencia, `input`, operaciones, `if/elif/else` | Puntos 1 a 7 (operaciones, promedio, conversión de temperatura, área, par/impar, mayoría de edad, calculadora) y un ejemplo de descuentos |
| `Ejercicios Ciclos/` | `for`, `range`, listas, `sum`/`max`/`min` | Puntos 8 a 13 (orden inverso, promedio, mayor/menor, aprobados, búsqueda, suma) |
| `Lista, Diccionarios, Tuplas y Conjuntos/` | Estructuras de datos, funciones, menús, fechas | Puntos 14 a 30 (detalle abajo) |

### Ejercicios de estructuras de datos (Puntos 14 a 30)

| Punto | Qué hace | Conceptos que practica |
|---|---|---|
| 14 | Carga números y los muestra sin repetir | `set()` para eliminar duplicados, `try/except` para cortar la carga |
| 15 | Alumnos (nombre y nota): muestra los aprobados | lista de diccionarios, validación de nota (0–10), comprensión de lista |
| 16 | Productos con stock menor a 5 | comprensión con condición, `len()`, constante `STOCK_MINIMO` |
| 17 | Agenda de contactos: agregar y buscar | menú con `while True`, funciones, búsqueda sin distinguir mayúsculas (`lower()`), validación de email con `in` |
| 18 | Total de ventas (cantidad × precio) | acumulador `+=`, tabla alineada con f-strings. **Se corrigió un `KeyError`**: una clave tenía espacios (`"precio_unitario  "`) |
| 19 | Estudiantes con más de 3 materias | lista dentro de un diccionario, `len()` de una lista anidada, `join()` |
| 20 | Ranking y podio de jugadores | carga por teclado, `sorted(key=lambda, reverse=True)`, slicing `[:3]`, `enumerate()` |
| 21 | Biblioteca: agregar, buscar, prestar, devolver, listar disponibles | búsqueda parcial con `in`, modificar un diccionario dentro de una lista, `date.today().year` |
| 22 | Gastos diarios: total del mes, por categoría, promedio diario | `datetime.strptime`/`strftime`, acumular en un diccionario con `get()`, `set` de fechas para contar días distintos |
| 23 | Inscripción de alumnos en cursos con cupo | listas anidadas (DNI inscriptos por curso), `isdigit()`, `set.update()` para contar alumnos distintos |
| 24 | Sueldos según antigüedad e informe | función con `if/elif/else` por rangos, formato `:,.2f` y `:.0%` |
| 25 | Catálogo y carrito de compras con ticket | verificar stock (incluyendo lo que ya está en el carrito), descontar stock, `clear()`, `datetime.now()` |
| 26 | Pacientes y turnos médicos | diccionario con lista adentro, ciclos anidados, tuplas `(turno, paciente)`, conteo por médico con `get()` |
| 27 | Notas por estudiante: promedios, aprobación y top 3 | `split()` para leer varias notas en una línea, `all()`, `join()`, promedio de promedios |
| 28 | Pedidos de una cafetería | `max(..., default=0)` para numerar, `values()`, manejo de empates en el producto más vendido |
| 29 | Lista de tareas (To-Do) | ids autoincrementales, orden por fecha, tareas vencidas, `lista[:] = ...` para eliminar elementos |
| 30 | Ventas por vendedor, promedio del mes y vendedores destacados | agrupar por mes (`.month`, `.year`), promedio por venta vs. promedio por vendedor |

> Los ejercicios con menú (17, 21–23, 25, 26, 28–30) traen **datos de ejemplo** cargados en algunos casos, para poder probarlos sin tipear todo.

### Patrones que se repiten en los ejercicios

**1. Menú con `while True`**

```python
while True:
    print("1. Agregar")
    print("2. Salir")
    opcion = input("Seleccione una opción: ").strip()
    if opcion == "1":
        agregar()
    elif opcion == "2":
        break                      # corta el ciclo y termina el programa
    else:
        print("Opción no válida.")
```

Las opciones se comparan como texto (`"1"`), así no hace falta convertir con `int()` y el programa no falla si el usuario escribe una letra.

**2. Pedir un dato hasta que sea válido**

```python
def pedir_entero(mensaje, minimo=0):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:          # el texto no era un número
            print("Ingrese un número entero válido.")
            continue                # vuelve a preguntar
        if valor >= minimo:
            return valor            # return también corta el while
        print(f"El valor debe ser mayor o igual a {minimo}.")
```

Cada ejercicio repite sus propias funciones `pedir_texto`, `pedir_entero`, `pedir_monto` y `pedir_fecha` para que se pueda leer y ejecutar solo. En un proyecto real irían en un módulo compartido (por ejemplo `utilidades.py`) que se importa desde cada archivo (ver [sección 16](#16-módulos-paquetes-y-entornos-virtuales)).

**3. Buscar en una lista de diccionarios y devolver `None` si no está**

```python
def buscar_alumno(dni):
    for alumno in alumnos:
        if alumno["dni"] == dni:
            return alumno           # devuelve el diccionario encontrado
    return None                     # recorrió todo y no lo encontró

alumno = buscar_alumno("40111222")
if alumno is None:
    print("No existe")
```

**4. Acumular o contar agrupando con un diccionario y `get()`**

```python
totales = {}
for venta in ventas:
    totales[venta["vendedor"]] = totales.get(venta["vendedor"], 0) + venta["monto"]
# get(clave, 0) devuelve 0 la primera vez, así no da KeyError
```

Para contar en vez de sumar, se suma `1` en lugar del monto. `collections.Counter` hace lo mismo en una línea (sección 10).

**5. Ordenar y quedarse con los primeros**

```python
top3 = sorted(estudiantes, key=lambda e: e["promedio"], reverse=True)[:3]
```

**6. Normalizar texto antes de comparar o guardar**

```python
nombre.strip()        # quita espacios sobrantes
nombre.lower()        # para comparar sin importar mayúsculas
nombre.title()        # "ana gómez" → "Ana Gómez" (nombres propios)
categoria.capitalize()  # "COMIDA" → "Comida" (para agrupar bien)
```

### Métodos y funciones usados (referencia rápida)

En el código de los ejercicios cada uno lleva un comentario que explica qué hace. Acá están todos juntos:

**Listas**

| Método / función | Qué hace | Ejemplo |
|---|---|---|
| `lista.append(x)` | agrega `x` al final | `alumnos.append({"nombre": "Ana"})` |
| `lista.clear()` | vacía la lista | `carrito.clear()` |
| `lista.reverse()` | invierte el orden en la misma lista | `nombres.reverse()` |
| `lista[:3]` | slicing: los 3 primeros (o los que haya) | `ordenados[:3]` |
| `lista[:] = nueva` | reemplaza el contenido manteniendo la misma lista | `tareas[:] = [t for t in tareas if ...]` |
| `len(lista)` | cantidad de elementos | `len(curso["inscriptos"])` |
| `sum(...)` | suma los valores | `sum(g["monto"] for g in gastos)` |
| `max(...)` / `min(...)` | mayor / menor; `default=` evita el error con lista vacía | `max(ids, default=0)` |
| `sorted(lista, key=..., reverse=True)` | devuelve una lista **nueva** ordenada | `sorted(jugadores, key=lambda j: j["puntaje"])` |
| `enumerate(lista, start=1)` | recorre devolviendo `(posición, elemento)` | `for i, j in enumerate(podio, start=1)` |
| `all(...)` / `any(...)` | ¿todos cumplen? / ¿alguno cumple? | `all(0 <= n <= 10 for n in notas)` |
| `x in lista` | ¿está `x` en la lista? | `dni in curso["inscriptos"]` |

**Diccionarios**

| Método | Qué hace | Ejemplo |
|---|---|---|
| `dic["clave"]` | lee un valor (`KeyError` si no existe) | `alumno["nota"]` |
| `dic["clave"] = valor` | agrega o modifica | `libro["estado"] = "prestado"` |
| `dic.get(clave, defecto)` | lee un valor o devuelve `defecto` si no existe | `totales.get(medico, 0)` |
| `dic.items()` | pares `(clave, valor)` para recorrer | `for medico, cant in totales.items()` |
| `dic.values()` | solo los valores | `max(cantidades.values())` |
| `dic.keys()` | solo las claves | `list(totales.keys())` |

**Conjuntos**

| Método | Qué hace | Ejemplo |
|---|---|---|
| `set(lista)` | crea un conjunto sin repetidos | `list(set(numeros))` |
| `{expr for x in ...}` | comprensión de conjunto | `{g["fecha"] for g in gastos}` |
| `conjunto.update(lista)` | agrega varios elementos | `alumnos_distintos.update(curso["inscriptos"])` |

**Strings**

| Método | Qué hace | Ejemplo |
|---|---|---|
| `strip()` | quita espacios al principio y al final | `"  Ana ".strip()` → `"Ana"` |
| `lower()` / `upper()` | minúsculas / mayúsculas | `"SALIR".lower()` → `"salir"` |
| `title()` | mayúscula al inicio de cada palabra | `"ana gómez".title()` → `"Ana Gómez"` |
| `capitalize()` | primera letra mayúscula, resto minúscula | `"COMIDA".capitalize()` → `"Comida"` |
| `split()` | separa en una lista | `"7 8 6".split()` → `["7", "8", "6"]` |
| `", ".join(lista)` | une una lista de textos con un separador | `", ".join(["a", "b"])` → `"a, b"` |
| `replace(a, b)` | reemplaza texto | `"8,5".replace(",", ".")` → `"8.5"` |
| `isdigit()` | ¿tiene solo dígitos? | `"40111222".isdigit()` → `True` |
| `"x" in texto` | ¿un texto está contenido en otro? | `"bor" in "borges"` → `True` |

**Fechas (`from datetime import date, datetime`)**

| Función / atributo | Qué hace | Ejemplo |
|---|---|---|
| `date.today()` | fecha de hoy | `date.today().year` → año actual |
| `datetime.now()` | fecha y hora actual | ticket del Punto 25 |
| `datetime.strptime(texto, formato)` | texto → fecha | `datetime.strptime("21/10/2026", "%d/%m/%Y").date()` |
| `fecha.strftime(formato)` | fecha → texto | `fecha.strftime("%d/%m/%Y")` |
| `fecha.month`, `fecha.year` | mes y año de una fecha | filtrar los gastos de un mes |
| `fecha1 < fecha2` | las fechas se comparan directamente | turnos en fechas pasadas, tareas vencidas |

**Formato en f-strings**

| Formato | Resultado |
|---|---|
| `f"{x:.2f}"` | 2 decimales |
| `f"{x:,.2f}"` | separador de miles y 2 decimales (`1,500.50`) |
| `f"{0.1:.0%}"` | porcentaje (`10%`) |
| `f"{mes:02d}"` | entero con 2 dígitos (`05`) |
| `f"{texto:<18}"` / `:>10` / `:^44` | alinear a la izquierda / derecha / centro en ese ancho |
| `f"{8.0:g}"` | sin decimales innecesarios (`8`) |

---

## 2. Cómo ejecutar Python

```bash
python --version          # verificar instalación (en Windows también: py --version)
python Holamundo.py       # ejecutar un archivo
python                    # abrir la consola interactiva (REPL); salir con exit()
python -m pip install X   # instalar un paquete
```

Si el nombre del archivo o la carpeta tiene espacios, usá comillas:

```bash
python "Ejercicios Ciclos/Punto10.py"
```

---

## 3. Qué es Python y cómo funciona

- **Interpretado**: el código fuente se compila a *bytecode* (`.pyc`, en `__pycache__/`) y lo ejecuta la máquina virtual de CPython línea por línea. No hay paso de compilación manual.
- **Tipado dinámico**: el tipo lo tiene el **valor**, no la variable. Una variable puede apuntar a un `int` y después a un `str`.
- **Tipado fuerte**: no convierte tipos implícitamente de forma "mágica". `"3" + 4` da error (en JavaScript daría `"34"`).
- **Todo es un objeto**: números, funciones, clases, módulos… todo tiene un tipo (`type(x)`), una identidad (`id(x)`) y un valor.
- **Las variables son referencias (etiquetas)**: `a = [1, 2]; b = a` no copia la lista, ambas variables apuntan al mismo objeto.
- **La indentación es sintaxis**: los bloques se definen con sangría (4 espacios por convención), no con llaves.
- **Multiparadigma**: imperativo, orientado a objetos y funcional.

### Mutables vs. inmutables (concepto clave)

| Inmutables | Mutables |
|---|---|
| `int`, `float`, `bool`, `str`, `tuple`, `frozenset`, `None` | `list`, `dict`, `set`, objetos de clases propias |

Un objeto inmutable no puede modificarse: cualquier "cambio" crea un objeto nuevo.

```python
s = "hola"
s.upper()        # devuelve "HOLA", pero s sigue siendo "hola"
s = s.upper()    # ahora s apunta a un string nuevo

lista = [1, 2]
otra = lista
otra.append(3)
print(lista)     # [1, 2, 3]  ← ¡se modificó el mismo objeto!
```

---

## 4. Sintaxis básica, variables y tipos

```python
# Esto es un comentario de una línea
"""Esto es un docstring / string multilínea,
se usa para documentar módulos, funciones y clases."""

nombre = "María"         # str
edad = 25                # int (precisión ilimitada: 2**1000 funciona)
altura = 1.65            # float (punto flotante de doble precisión)
activo = True            # bool (True / False, con mayúscula)
nada = None              # ausencia de valor
complejo = 3 + 2j        # complex

a, b, c = 1, 2, 3        # asignación múltiple
a, b = b, a              # intercambio sin variable auxiliar
x = y = 0                # mismo valor a varias variables
MAX_INTENTOS = 3         # constante por convención (Python no las fuerza)
```

### Conversión de tipos (casting)

```python
int("42")        # 42
int(3.99)        # 3  (trunca, no redondea)
float("3.5")     # 3.5
str(10)          # "10"
bool(0), bool("")  , bool([])   # False, False, False  → valores "falsy"
bool(5), bool("a") , bool([0])  # True, True, True
list("abc")      # ['a', 'b', 'c']
round(2.675, 2)  # 2.67 (¡ojo con los float! ver sección 25)
```

**Valores falsy**: `False`, `None`, `0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`. Todo lo demás es *truthy*. Por eso se puede escribir `if lista:` en vez de `if len(lista) > 0:`.

### Inspección

```python
type(edad)              # <class 'int'>
isinstance(edad, int)   # True (preferible a comparar type())
id(edad)                # identidad del objeto en memoria
dir(str)                # lista de atributos/métodos
help(str.split)         # documentación
```

---

## 5. Operadores

### Aritméticos

| Operador | Significado | Ejemplo | Resultado |
|---|---|---|---|
| `+` `-` `*` | suma, resta, producto | `7 * 2` | `14` |
| `/` | división real (siempre float) | `7 / 2` | `3.5` |
| `//` | división entera (piso) | `7 // 2` | `3` |
| `%` | módulo (resto) | `7 % 2` | `1` |
| `**` | potencia | `2 ** 10` | `1024` |

`%` es la herramienta para "par o impar" (`n % 2 == 0`, como en `Punto5.py`) y para saber si un número es divisible por otro.

**Asignación compuesta**: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` (ej.: `total_notas += nota` en `Punto2.py`). Python **no** tiene `++` ni `--`.

### Comparación y lógicos

```python
==  !=  <  >  <=  >=        # comparación (devuelven bool)
1 < x < 10                  # comparaciones encadenadas (muy pythónico)
and  or  not                # lógicos, con evaluación de cortocircuito
```

`and`/`or` devuelven **uno de los operandos**, no necesariamente un bool:

```python
nombre = input() or "Anónimo"   # si el usuario no escribe nada, usa "Anónimo"
```

### Identidad y pertenencia

```python
x is None          # identidad: ¿es el MISMO objeto?
x == y             # igualdad: ¿tienen el mismo VALOR?
"pera" in productos        # pertenencia (ver Punto12.py)
"kiwi" not in productos
```

Regla: usá `is` **solo** para comparar con `None`, `True` o `False`.

### Operador morsa `:=` (3.8+)

Asigna y devuelve el valor dentro de una expresión:

```python
while (texto := input("Comando: ")) != "salir":
    print(f"Ejecutando {texto}")
```

### Ternario

```python
estado = "aprobado" if promedio >= 6 else "desaprobado"
```

---

## 6. Strings (cadenas) en profundidad

```python
s = "Python"
s[0]        # 'P'      índice desde 0
s[-1]       # 'n'      índices negativos cuentan desde el final
s[0:3]      # 'Pyt'    slicing [inicio:fin) — fin no incluido
s[::2]      # 'Pto'    paso de 2
s[::-1]     # 'nohtyP' invertir
len(s)      # 6
"th" in s   # True
s * 2       # 'PythonPython'
```

### Métodos más usados

```python
"  hola  ".strip()               # 'hola' (también lstrip / rstrip)
"Hola".upper(), "Hola".lower()   # 'HOLA', 'hola'
"hola mundo".title()             # 'Hola Mundo'
"a,b,c".split(",")               # ['a', 'b', 'c']   ← Punto8.py
", ".join(["a", "b", "c"])       # 'a, b, c'
"banana".replace("a", "o")       # 'bonono'
"banana".count("a")              # 3
"banana".find("n")               # 2 (-1 si no está)
"archivo.py".endswith(".py")     # True
"123".isdigit()                  # True — útil para validar input
"Hola".startswith("H")           # True
```

> En `Punto8.py`, `"Ana, Luis".split(",")` deja un espacio adelante en `" Luis"`. Solución: `[n.strip() for n in texto.split(",")]`.

### Formateo con f-strings (la forma moderna)

```python
nombre, prom = "Ana", 7.456
f"{nombre} tiene {prom:.2f}"     # 'Ana tiene 7.46'
f"{1234567:,}"                   # '1,234,567'
f"{0.25:.0%}"                    # '25%'
f"{'izq':<10}|{'der':>10}|{'centro':^10}"   # alineación y ancho
f"{prom = }"                     # 'prom = 7.456' (útil para depurar)
```

Strings especiales:

```python
r"C:\Users\maria"     # raw string: no interpreta \ como escape
"Línea 1\nLínea 2\tTab"   # \n salto de línea, \t tabulación
"""Multi
línea"""
```

---

## 7. Entrada y salida

```python
dato = input("Mensaje: ")          # SIEMPRE devuelve str
edad = int(input("Edad: "))        # hay que convertir
a, b = map(int, input("Dos números: ").split())   # leer varios en una línea

print("a", "b", "c")               # a b c
print("a", "b", sep="-")           # a-b
print("sin salto", end="")         # no agrega \n al final
```

Si el usuario escribe algo no numérico, `int(input())` lanza `ValueError`. Ver [validación con `try/except`](#14-manejo-de-errores-y-excepciones).

---

## 8. Condicionales y `match`

```python
if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
```

- `elif` evita anidar `if` dentro de `else`.
- Un bloque vacío se escribe con `pass`.

### `match` / `case` (3.10+) — *structural pattern matching*

Es más potente que un `switch` de otros lenguajes. La calculadora de `Punto7.py` quedaría:

```python
match operacion:
    case "+":
        resultado = num1 + num2
    case "-":
        resultado = num1 - num2
    case "*":
        resultado = num1 * num2
    case "/" if num2 != 0:          # guarda (condición extra)
        resultado = num1 / num2
    case "/":
        resultado = "No se puede dividir por cero"
    case _:                          # comodín = "default"
        resultado = "Operación inválida"
```

También puede desestructurar datos:

```python
match punto:
    case (0, 0):          print("Origen")
    case (x, 0):          print(f"Sobre el eje X en {x}")
    case (x, y):          print(f"Punto en ({x}, {y})")

match pedido:
    case {"tipo": "envio", "direccion": dir}:
        print(f"Enviar a {dir}")
```

---

## 9. Ciclos

### `for` — recorre cualquier iterable

```python
for i in range(5):            # 0, 1, 2, 3, 4
for i in range(1, 4):         # 1, 2, 3
for i in range(10, 0, -2):    # 10, 8, 6, 4, 2
for letra in "hola":          # recorre caracteres
for producto in productos:    # recorre una lista
```

### `while` — repite mientras la condición sea verdadera

```python
intentos = 0
while intentos < 3:
    intentos += 1
```

### Control de flujo

```python
for n in numeros:
    if n < 0:
        continue      # salta a la siguiente vuelta
    if n == 0:
        break         # corta el ciclo
else:
    print("Terminó sin break")   # el else de un ciclo se ejecuta si NO hubo break
```

El `for ... else` es ideal para búsquedas:

```python
for p in productos:
    if p == buscado:
        print("Encontrado")
        break
else:
    print("No encontrado")
```

### Funciones auxiliares para iterar

```python
for i, nombre in enumerate(nombres, start=1):   # índice + valor
    print(i, nombre)

for nombre, nota in zip(nombres, notas):        # recorre en paralelo
    print(nombre, nota)

for x in reversed(lista): ...                   # en orden inverso, sin modificar
for x in sorted(lista, reverse=True): ...       # ordenado, sin modificar
```

### Funciones de agregación

```python
sum(numeros), max(numeros), min(numeros), len(numeros)
any(n > 10 for n in numeros)     # ¿alguno cumple?
all(n >= 6 for n in notas)       # ¿todos cumplen?
```

`Punto11.py` usa `sum(1 for nota in notas if nota >= 6)` para contar: es una **expresión generadora** (sección 18).

### Patrón "pedir hasta que sea válido"

```python
while True:
    texto = input("Ingrese un número: ")
    if texto.isdigit():
        numero = int(texto)
        break
    print("Inválido, intente de nuevo.")
```

---

## 10. Estructuras de datos (repaso y más allá)

### Resumen comparativo

| Tipo | Literal | Ordenada | Mutable | Duplicados | Acceso | Uso típico |
|---|---|---|---|---|---|---|
| `list` | `[1, 2]` | ✅ | ✅ | ✅ | por índice | colección que cambia |
| `tuple` | `(1, 2)` | ✅ | ❌ | ✅ | por índice | registro fijo, clave de dict |
| `dict` | `{"a": 1}` | ✅ (por inserción) | ✅ | claves únicas | por clave | mapeo clave → valor |
| `set` | `{1, 2}` | ❌ | ✅ | ❌ | pertenencia | eliminar duplicados, operaciones de conjuntos |
| `frozenset` | `frozenset({1})` | ❌ | ❌ | ❌ | pertenencia | set usable como clave |

### Listas

```python
l = [3, 1, 2]
l.append(4)          # agrega al final
l.insert(0, 9)       # inserta en posición
l.extend([5, 6])     # agrega varios
l.remove(9)          # elimina por valor (primera aparición)
l.pop()              # elimina y devuelve el último (o pop(i))
l.sort()             # ordena IN PLACE (devuelve None)
sorted(l)            # devuelve una lista NUEVA ordenada
l.reverse()          # invierte in place (Punto8.py)
l.index(2), l.count(2)
l[1:3] = [7, 8]      # reemplazo por slicing
del l[0]
copia = l.copy()     # o l[:]  o list(l) — copia superficial
```

### Tuplas y desempaquetado

```python
punto = (3, 4)
x, y = punto
primero, *resto = [1, 2, 3, 4]    # primero=1, resto=[2, 3, 4]
uno = (1,)                         # tupla de un elemento: ¡lleva coma!

def min_max(nums):
    return min(nums), max(nums)    # devolver varios valores = devolver una tupla
menor, mayor = min_max([4, 1, 9])
```

**Named tuples**: tuplas con nombres de campo.

```python
from collections import namedtuple
Alumno = namedtuple("Alumno", ["nombre", "nota"])
a = Alumno("Ana", 8)
a.nombre, a.nota
```

### Diccionarios

```python
alumno = {"nombre": "Ana", "nota": 8}
alumno["nota"]                  # 8 (KeyError si no existe)
alumno.get("edad", 0)           # 0 — valor por defecto, sin error
alumno["edad"] = 20             # agrega o modifica
alumno.setdefault("cursos", []).append("Python")
del alumno["edad"]
alumno.pop("nota", None)

for clave, valor in alumno.items(): ...
alumno.keys(), alumno.values()
alumno |= {"pais": "AR"}        # unir diccionarios (3.9+)
```

Las claves deben ser **hashables** (inmutables): `str`, `int`, `tuple`… nunca una lista.

### Conjuntos

```python
a, b = {1, 2, 3}, {2, 3, 4}
a | b     # unión          {1, 2, 3, 4}
a & b     # intersección   {2, 3}
a - b     # diferencia     {1}
a ^ b     # dif. simétrica {1, 4}
set([1, 1, 2])   # {1, 2} — quitar duplicados
vacio = set()    # ¡{} es un dict vacío, no un set!
```

La búsqueda `x in conjunto` es **O(1)** promedio; en una lista es **O(n)**. Para buscar muchas veces en una colección grande, convertila a `set`.

### Más allá: el módulo `collections`

```python
from collections import Counter, defaultdict, deque, OrderedDict

Counter("banana")                  # Counter({'a': 3, 'n': 2, 'b': 1})
Counter(notas).most_common(3)      # las 3 notas más repetidas

grupos = defaultdict(list)         # crea la lista automáticamente
for nombre, curso in inscripciones:
    grupos[curso].append(nombre)

cola = deque([1, 2, 3])            # cola de doble extremo, eficiente en ambos lados
cola.appendleft(0); cola.popleft()
```

### Pilas y colas

- **Pila (LIFO)**: una `list` con `append()` y `pop()`.
- **Cola (FIFO)**: `deque` con `append()` y `popleft()` (en una lista, `pop(0)` es lento).
- **Cola de prioridad**: módulo `heapq`.

### Copia superficial vs. profunda

```python
import copy
matriz = [[1, 2], [3, 4]]
sup = matriz.copy()            # copia la lista externa, comparte las internas
prof = copy.deepcopy(matriz)   # copia todo, recursivamente
sup[0][0] = 99                 # ¡también cambia matriz!
```

---

## 11. Comprensiones

Forma concisa de construir colecciones a partir de otras. Sintaxis: `[expresión for elemento in iterable if condición]`.

```python
cuadrados = [n ** 2 for n in range(10)]
pares     = [n for n in numeros if n % 2 == 0]
etiquetas = ["par" if n % 2 == 0 else "impar" for n in numeros]   # if/else va ANTES del for
nombres   = [n.strip() for n in "Ana, Luis, Sol".split(",")]

notas_por_alumno = {nombre: nota for nombre, nota in zip(nombres, notas)}   # dict
iniciales = {nombre[0] for nombre in nombres}                              # set
aplanada  = [x for fila in matriz for x in fila]                           # anidada
```

Los ejercicios de ciclos se pueden reescribir así:

```python
numeros = [int(input("Número: ")) for _ in range(8)]   # Punto10: cargar 8 números
```

(`_` es la convención para una variable que no se usa.)

Si la comprensión no entra cómoda en una línea o tiene muchas condiciones, usá un `for` normal: la legibilidad manda.

---

## 12. Funciones

```python
def calcular_promedio(notas):
    """Devuelve el promedio de una lista de notas."""   # docstring
    if not notas:
        return 0
    return sum(notas) / len(notas)
```

- Sin `return` (o `return` solo), la función devuelve `None`.
- Las funciones son **objetos**: se pueden guardar en variables, pasar como argumento y devolver.

### Tipos de parámetros

```python
def saludar(nombre, saludo="Hola"):          # parámetro con valor por defecto
    return f"{saludo}, {nombre}"

saludar("Ana")                    # posicional
saludar(saludo="Buenas", nombre="Ana")   # por nombre (keyword)

def sumar_todo(*args):            # cantidad variable de posicionales → tupla
    return sum(args)
sumar_todo(1, 2, 3)

def mostrar(**kwargs):            # cantidad variable de nombrados → dict
    for k, v in kwargs.items():
        print(k, v)
mostrar(nombre="Ana", edad=20)

def f(a, b, /, c, *, d):          # / → a y b solo posicionales; * → d solo por nombre
    ...

valores = [1, 2, 3]
sumar_todo(*valores)              # desempaquetar al llamar
config = {"nombre": "Ana"}
saludar(**config)
```

Orden de los parámetros: `normales, /, normales, *args, solo-keyword, **kwargs`.

### ⚠️ Valor por defecto mutable

```python
def agregar(item, lista=[]):      # MAL: la lista se crea UNA vez y se comparte
    lista.append(item)
    return lista

def agregar(item, lista=None):    # BIEN
    if lista is None:
        lista = []
    lista.append(item)
    return lista
```

### Paso de argumentos

Python pasa **referencias a objetos** ("pass by object reference"). Si la función modifica un objeto mutable recibido (`lista.append`), el cambio se ve afuera; si reasigna el parámetro (`lista = [...]`), no.

### Recursividad

```python
def factorial(n):
    if n <= 1:            # caso base
        return 1
    return n * factorial(n - 1)   # caso recursivo
```

El límite de recursión por defecto es ~1000 llamadas (`sys.getrecursionlimit()`). Para problemas grandes conviene una versión iterativa.

### Refactor de un ejercicio con funciones

```python
# Secuencia_Condicionales/Punto3.py como función reutilizable
def celsius_a_fahrenheit(c: float) -> float:
    return c * 1.8 + 32

if __name__ == "__main__":
    temp = float(input("Temperatura en °C: "))
    print(f"{celsius_a_fahrenheit(temp):.1f} °F")
```

`if __name__ == "__main__":` hace que ese bloque se ejecute solo cuando corrés el archivo directamente, y no cuando lo importás desde otro (sección 16).

---

## 13. Alcance de variables (scope)

Regla **LEGB**: Python busca un nombre en este orden:

1. **L**ocal — dentro de la función actual
2. **E**nclosing — funciones que contienen a la actual
3. **G**lobal — nivel del módulo (archivo)
4. **B**uilt-in — nombres predefinidos (`print`, `len`…)

```python
contador = 0
def incrementar():
    global contador          # para REASIGNAR una global (usar con moderación)
    contador += 1

def externa():
    total = 0
    def interna():
        nonlocal total       # para reasignar una variable de la función contenedora
        total += 1
    interna()
    return total
```

**Closure**: una función interna que "recuerda" variables de la externa aunque esta ya haya terminado.

```python
def multiplicador(factor):
    def multiplicar(x):
        return x * factor
    return multiplicar

doble = multiplicador(2)
doble(5)    # 10
```

> No pises nombres built-in: `list = [1, 2]` o `sum = 0` rompen `list()` y `sum()` en ese archivo.

---

## 14. Manejo de errores y excepciones

```python
try:
    num = int(input("Número: "))
    resultado = 10 / num
except ValueError:
    print("No es un número válido")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except (TypeError, KeyError) as e:     # varias a la vez, con acceso al error
    print(f"Error: {e}")
else:
    print("Se ejecuta si NO hubo excepción:", resultado)
finally:
    print("Se ejecuta SIEMPRE (cerrar recursos, etc.)")
```

### Excepciones comunes

| Excepción | Cuándo ocurre |
|---|---|
| `ValueError` | valor con tipo correcto pero inválido: `int("hola")` |
| `TypeError` | operación con tipos incompatibles: `"a" + 1` |
| `ZeroDivisionError` | `x / 0` (le puede pasar a `Punto1.py` y `Punto7.py`) |
| `IndexError` | índice fuera de rango: `[1, 2][5]` |
| `KeyError` | clave inexistente en un dict |
| `NameError` | variable no definida (en `Punto7.py`, si la operación es inválida, `resultado` nunca se define) |
| `AttributeError` | atributo/método inexistente |
| `FileNotFoundError` | archivo inexistente |

### Lanzar y crear excepciones

```python
def retirar(saldo, monto):
    if monto > saldo:
        raise ValueError("Saldo insuficiente")
    return saldo - monto

class SaldoInsuficienteError(Exception):     # excepción propia
    """Se lanza cuando no alcanza el saldo."""
```

### Buenas prácticas

- Capturá excepciones **específicas**. Evitá `except:` a secas o `except Exception:` sin motivo: esconden errores reales.
- Poné en el `try` solo el código que puede fallar.
- Filosofía de Python: **EAFP** ("es más fácil pedir perdón que permiso"): intentar y capturar, en lugar de chequear todo antes.
- `assert condicion, "mensaje"` sirve para verificaciones internas durante el desarrollo, no para validar datos del usuario.

---

## 15. Archivos

Siempre con `with`: cierra el archivo automáticamente aunque haya un error.

```python
# Escribir ('w' sobrescribe, 'a' agrega al final)
with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("Ana,8\n")
    f.writelines(["Luis,6\n", "Sol,9\n"])

# Leer
with open("notas.txt", encoding="utf-8") as f:
    contenido = f.read()           # todo como un string
with open("notas.txt", encoding="utf-8") as f:
    for linea in f:                # línea por línea (eficiente en memoria)
        nombre, nota = linea.strip().split(",")
```

Modos: `r` lectura (por defecto), `w` escritura, `a` agregar, `x` crear (falla si existe), `b` binario (`rb`, `wb`), `+` lectura y escritura.

> En Windows especificá siempre `encoding="utf-8"` para no tener problemas con tildes y ñ.

### CSV y JSON

```python
import csv, json

with open("alumnos.csv", newline="", encoding="utf-8") as f:
    for fila in csv.DictReader(f):
        print(fila["nombre"], fila["nota"])

datos = {"curso": "Python", "alumnos": ["Ana", "Luis"]}
with open("datos.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)
with open("datos.json", encoding="utf-8") as f:
    datos = json.load(f)

json.dumps(datos)   # dict → str
json.loads(texto)   # str → dict
```

### Rutas con `pathlib`

```python
from pathlib import Path
carpeta = Path("Ejercicios Ciclos")
for archivo in carpeta.glob("*.py"):
    print(archivo.name, archivo.stat().st_size)
Path("salida").mkdir(exist_ok=True)
texto = Path("Holamundo.py").read_text(encoding="utf-8")
```

---

## 16. Módulos, paquetes y entornos virtuales

- **Módulo**: cualquier archivo `.py`.
- **Paquete**: carpeta con módulos (y opcionalmente un `__init__.py`).

```python
import math                       # importar módulo completo
math.sqrt(16)
from math import pi, sqrt         # importar nombres específicos
import datetime as dt             # alias
from utilidades import promedio   # módulo propio (utilidades.py en la misma carpeta)
```

Evitá `from modulo import *`: no se sabe de dónde viene cada nombre.

> Los nombres de carpeta con espacios o comas (como `Lista, Diccionarios, Tuplas y Conjuntos`) no pueden importarse como paquetes. Para código reutilizable usá `snake_case`: `estructuras_de_datos/`.

### `__name__`

Cada módulo tiene la variable `__name__`. Vale `"__main__"` cuando el archivo se ejecuta directamente y el nombre del módulo cuando se importa. De ahí el patrón:

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

### Entornos virtuales y `pip`

Un entorno virtual aísla las dependencias de cada proyecto.

```bash
python -m venv .venv                 # crear
.venv\Scripts\activate               # activar en Windows
source .venv/bin/activate            # activar en Linux/macOS
pip install requests                 # instalar paquete
pip freeze > requirements.txt        # guardar dependencias
pip install -r requirements.txt      # reinstalarlas en otra máquina
deactivate                           # salir
```

Agregá `.venv/` y `__pycache__/` al `.gitignore`.

---

## 17. Programación orientada a objetos

### Clases y objetos

```python
class Alumno:
    institucion = "UADER"                 # atributo de CLASE (compartido)

    def __init__(self, nombre, notas=None):   # constructor / inicializador
        self.nombre = nombre              # atributo de INSTANCIA
        self.notas = notas or []

    def agregar_nota(self, nota):         # método de instancia
        if not 0 <= nota <= 10:
            raise ValueError("Nota fuera de rango")
        self.notas.append(nota)

    def promedio(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def esta_aprobado(self):
        return self.promedio() >= 6

ana = Alumno("Ana")
ana.agregar_nota(8)
ana.esta_aprobado()     # True
```

`self` es la referencia al objeto actual; Python lo pasa automáticamente.

### Los 4 pilares

**Encapsulamiento** — Python no tiene `private` real; se usan convenciones:

```python
class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo          # _ → "interno, no tocar desde afuera"
        self.__pin = 1234            # __ → name mangling (_Cuenta__pin)

    @property                        # getter: se usa como atributo
    def saldo(self):
        return self._saldo

    @saldo.setter                    # setter con validación
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor

c = Cuenta(100)
c.saldo = 50      # pasa por el setter
```

**Herencia**:

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def presentarse(self):
        return f"Soy {self.nombre}"

class Docente(Persona):
    def __init__(self, nombre, materia):
        super().__init__(nombre)          # llama al constructor del padre
        self.materia = materia
    def presentarse(self):                # sobrescritura (override)
        return f"{super().presentarse()} y doy {self.materia}"

isinstance(Docente("Juan", "BD"), Persona)   # True
issubclass(Docente, Persona)                 # True
```

Python admite herencia múltiple (`class C(A, B)`); el orden de búsqueda de métodos se ve con `C.__mro__`.

**Polimorfismo** — objetos distintos responden al mismo mensaje. En Python rige el *duck typing*: "si camina como pato y hace cuac, es un pato"; no importa la clase, importa que tenga el método.

```python
for p in [Persona("Ana"), Docente("Juan", "Python")]:
    print(p.presentarse())
```

**Abstracción** — clases abstractas que no se pueden instanciar:

```python
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self): ...

class Rectangulo(Figura):            # Punto4.py como objeto
    def __init__(self, base, altura):
        self.base, self.altura = base, altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2 * (self.base + self.altura)
```

### Métodos de clase y estáticos

```python
class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def desde_fahrenheit(cls, f):        # constructor alternativo, recibe la clase
        return cls((f - 32) / 1.8)

    @staticmethod
    def es_valida(c):                    # función utilitaria, no recibe self ni cls
        return c >= -273.15
```

### Métodos mágicos (dunder)

Permiten que tus objetos se integren con la sintaxis del lenguaje.

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):                  # representación para el programador
        return f"Vector({self.x}, {self.y})"
    def __str__(self):                   # lo que muestra print()
        return f"({self.x}, {self.y})"
    def __add__(self, otro):             # v1 + v2
        return Vector(self.x + otro.x, self.y + otro.y)
    def __eq__(self, otro):              # v1 == v2
        return (self.x, self.y) == (otro.x, otro.y)
    def __len__(self):                   # len(v)
        return 2
```

Otros: `__lt__` (`<`, permite `sorted`), `__getitem__` (`obj[i]`), `__iter__` (`for x in obj`), `__contains__` (`in`), `__call__` (`obj()`), `__hash__`.

### `dataclasses`: clases de datos sin repetir código

```python
from dataclasses import dataclass, field

@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int = 0
    etiquetas: list[str] = field(default_factory=list)

p = Producto("Mate", 5000)
print(p)          # Producto(nombre='Mate', precio=5000, stock=0, etiquetas=[])
```

Genera automáticamente `__init__`, `__repr__` y `__eq__`. Con `@dataclass(frozen=True)` el objeto es inmutable.

### Composición vs. herencia

Preferí **composición** ("tiene un") cuando la relación no es claramente "es un": un `Carrito` *tiene* `Producto`s, no *es* un producto.

---

## 18. Iteradores y generadores

**Iterable**: algo que se puede recorrer con `for` (implementa `__iter__`). **Iterador**: objeto que entrega el siguiente valor con `next()` y lanza `StopIteration` al terminar.

```python
it = iter([1, 2, 3])
next(it)   # 1
next(it)   # 2
```

### Generadores: `yield`

Una función con `yield` produce valores **de a uno y bajo demanda** (evaluación perezosa), sin guardar todo en memoria.

```python
def contar_hasta(n):
    i = 1
    while i <= n:
        yield i            # pausa la función y devuelve i
        i += 1

for x in contar_hasta(3):
    print(x)               # 1 2 3

def leer_numeros(ruta):    # procesar un archivo enorme línea por línea
    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            yield int(linea)
```

### Expresiones generadoras

Como una comprensión de lista pero con paréntesis: no crean la lista.

```python
total = sum(n ** 2 for n in range(1_000_000))     # no ocupa memoria para el millón
aprobados = sum(1 for nota in notas if nota >= 6)  # Punto11.py
```

### `itertools`

```python
import itertools as it
it.count(1)                        # 1, 2, 3, ... infinito
it.cycle("AB")                     # A, B, A, B, ...
it.chain([1, 2], [3])              # 1, 2, 3
it.combinations([1, 2, 3], 2)      # (1,2) (1,3) (2,3)
it.permutations("abc", 2)
it.product([0, 1], repeat=2)       # (0,0) (0,1) (1,0) (1,1)
it.groupby(sorted(datos, key=f), key=f)
it.islice(generador, 5)            # los primeros 5
```

---

## 19. Funciones de orden superior, `lambda` y decoradores

### `lambda`: funciones anónimas de una expresión

```python
cuadrado = lambda x: x ** 2
alumnos = [("Ana", 8), ("Luis", 6), ("Sol", 9)]
sorted(alumnos, key=lambda a: a[1], reverse=True)   # ordenar por nota
max(alumnos, key=lambda a: a[1])                    # ('Sol', 9)
```

### `map`, `filter`, `reduce`

```python
list(map(int, ["1", "2", "3"]))              # [1, 2, 3]
list(filter(lambda n: n % 2 == 0, numeros))  # pares
from functools import reduce
reduce(lambda acc, n: acc * n, [1, 2, 3, 4]) # 24
```

En la práctica, las comprensiones suelen ser más legibles que `map`/`filter` con `lambda`.

### Decoradores

Un decorador es una función que recibe una función y devuelve otra que la "envuelve", agregando comportamiento sin modificar su código.

```python
import time
from functools import wraps

def medir_tiempo(func):
    @wraps(func)                       # conserva nombre y docstring originales
    def envoltura(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} tardó {time.perf_counter() - inicio:.4f}s")
        return resultado
    return envoltura

@medir_tiempo                          # equivale a: procesar = medir_tiempo(procesar)
def procesar(n):
    return sum(range(n))
```

Decorador con parámetros (tres niveles):

```python
def repetir(veces):
    def decorador(func):
        @wraps(func)
        def envoltura(*args, **kwargs):
            for _ in range(veces):
                func(*args, **kwargs)
        return envoltura
    return decorador

@repetir(3)
def saludar():
    print("Hola")
```

Decoradores built-in útiles: `@property`, `@classmethod`, `@staticmethod`, `@dataclass`, `@functools.lru_cache` (memoriza resultados):

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(100)   # instantáneo gracias al cache
```

---

## 20. Context managers (`with`)

Garantizan que un recurso se libere (archivo, conexión, lock), incluso si ocurre una excepción.

```python
class Conexion:
    def __enter__(self):
        print("Abriendo conexión")
        return self
    def __exit__(self, tipo, valor, traceback):
        print("Cerrando conexión")
        return False          # False → no silencia la excepción

with Conexion() as c:
    ...
```

Versión corta con `contextlib`:

```python
from contextlib import contextmanager

@contextmanager
def cronometro():
    import time
    inicio = time.perf_counter()
    yield
    print(f"{time.perf_counter() - inicio:.3f}s")

with cronometro():
    sum(range(10_000_000))
```

---

## 21. Type hints (anotaciones de tipo)

Python no las verifica en tiempo de ejecución, pero documentan el código, mejoran el autocompletado del editor y permiten chequear con herramientas como **mypy**.

```python
def promedio(notas: list[float]) -> float:
    return sum(notas) / len(notas)

edad: int = 20
alumnos: dict[str, list[float]] = {}
coordenada: tuple[int, int] = (0, 0)

def buscar(nombre: str) -> str | None:      # puede devolver str o None (3.10+)
    ...

from typing import Callable, Iterable, Any
def aplicar(f: Callable[[int], int], datos: Iterable[int]) -> list[int]:
    return [f(x) for x in datos]
```

```bash
pip install mypy
mypy mi_archivo.py
```

---

## 22. Biblioteca estándar: lo más útil

Python viene "con baterías incluidas":

| Módulo | Para qué | Ejemplo |
|---|---|---|
| `math` | funciones matemáticas | `math.sqrt(2)`, `math.pi`, `math.ceil(2.1)`, `math.floor(2.9)` |
| `random` | aleatorios | `random.randint(1, 6)`, `random.choice(l)`, `random.shuffle(l)` |
| `statistics` | estadística | `statistics.mean(l)`, `median`, `mode`, `stdev` |
| `datetime` | fechas y horas | `datetime.date.today()`, `datetime.timedelta(days=7)` |
| `time` | tiempo, pausas | `time.sleep(1)`, `time.perf_counter()` |
| `os` / `sys` | sistema operativo, intérprete | `os.getcwd()`, `os.environ`, `sys.argv`, `sys.exit()` |
| `pathlib` | rutas de archivos | `Path("a") / "b.txt"` |
| `json` / `csv` | formatos de datos | ver sección 15 |
| `re` | expresiones regulares | `re.findall(r"\d+", texto)` |
| `collections` | estructuras extra | `Counter`, `defaultdict`, `deque` |
| `itertools` / `functools` | iteración y funciones | ver secciones 18 y 19 |
| `decimal` / `fractions` | precisión exacta | `Decimal("0.1") + Decimal("0.2")` |
| `sqlite3` | base de datos SQL embebida | `sqlite3.connect("app.db")` |
| `logging` | registros (mejor que `print` en apps) | `logging.info("Inicio")` |
| `argparse` | argumentos de línea de comandos | scripts con `--opciones` |
| `unittest` | tests | ver sección 23 |

### Fechas

```python
from datetime import datetime, timedelta
ahora = datetime.now()
ahora.strftime("%d/%m/%Y %H:%M")              # fecha → texto
datetime.strptime("21/10/2026", "%d/%m/%Y")   # texto → fecha
vencimiento = ahora + timedelta(days=30)
```

### Expresiones regulares

```python
import re
re.fullmatch(r"[\w.]+@[\w.]+\.\w+", email)    # validar formato de email (simplificado)
re.findall(r"\d+", "tengo 3 gatos y 12 peces")  # ['3', '12']
re.sub(r"\s+", " ", "mucho    espacio")         # 'mucho espacio'
```

### SQLite (enlaza con Bases de Datos)

```python
import sqlite3
con = sqlite3.connect("escuela.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS alumno (id INTEGER PRIMARY KEY, nombre TEXT, nota REAL)")
cur.execute("INSERT INTO alumno (nombre, nota) VALUES (?, ?)", ("Ana", 8))   # ? evita inyección SQL
con.commit()
for fila in cur.execute("SELECT nombre, nota FROM alumno WHERE nota >= ?", (6,)):
    print(fila)
con.close()
```

---

## 23. Testing básico

### Con `assert` + `pytest` (lo más simple)

```python
# test_conversiones.py
from conversiones import celsius_a_fahrenheit

def test_punto_congelamiento():
    assert celsius_a_fahrenheit(0) == 32

def test_ebullicion():
    assert celsius_a_fahrenheit(100) == 212
```

```bash
pip install pytest
pytest            # busca archivos test_*.py y funciones test_*
```

### Con `unittest` (incluido en Python)

```python
import unittest

class TestPromedio(unittest.TestCase):
    def test_promedio(self):
        self.assertAlmostEqual(promedio([6, 7, 8]), 7)
    def test_lista_vacia(self):
        with self.assertRaises(ZeroDivisionError):
            promedio([])

if __name__ == "__main__":
    unittest.main()
```

---

## 24. Estilo y buenas prácticas (PEP 8)

**PEP 8** es la guía de estilo oficial.

- Indentación de **4 espacios** (no tabs).
- Nombres:
  - variables y funciones → `snake_case` (`calcular_promedio`, `cant_numeros`)
  - clases → `PascalCase` (`Alumno`, `CuentaBancaria`)
  - constantes → `MAYUSCULAS` (`NOTA_MINIMA = 6`)
  - "privados" → `_prefijo`
- Espacios alrededor de operadores: `suma = num1 + num2` (no `suma=num1+num2`).
- Líneas de hasta ~79–99 caracteres.
- Dos líneas en blanco entre funciones/clases de nivel superior; una entre métodos.
- Imports al principio del archivo: estándar → terceros → propios.
- Nombres descriptivos; evitar "números mágicos" (`if promedio >= NOTA_APROBACION` en vez de `>= 6`).
- Docstrings en funciones y clases públicas.

Herramientas que lo hacen por vos:

```bash
pip install ruff black
ruff check .     # detecta errores y problemas de estilo
black .          # formatea automáticamente
```

**El Zen de Python** — ejecutá `import this`. Algunas líneas clave:
*"Bello es mejor que feo. Explícito es mejor que implícito. Simple es mejor que complejo. La legibilidad cuenta. Los errores nunca deberían pasar silenciosamente."*

---

## 25. Errores y trampas comunes

| Trampa | Ejemplo | Solución |
|---|---|---|
| Olvidar que `input` devuelve `str` | `input() + 1` → `TypeError` | convertir con `int()`/`float()` |
| Precisión de `float` | `0.1 + 0.2 == 0.3` → `False` | `math.isclose(a, b)` o `Decimal` para dinero |
| `round` "banquero" | `round(2.5)` → `2`, `round(3.5)` → `4` | redondea al par más cercano; usar `Decimal` si importa |
| `=` vs `==` | `if x = 5:` → `SyntaxError` | `==` para comparar |
| `is` vs `==` | `a is b` con strings o números | usar `==`; `is` solo con `None` |
| Default mutable | `def f(l=[])` | `def f(l=None)` |
| Copia por referencia | `b = a` con listas | `a.copy()` / `copy.deepcopy(a)` |
| Modificar una lista mientras se recorre | `for x in l: l.remove(x)` | recorrer una copia o usar comprensión |
| `sort()` devuelve `None` | `l = l.sort()` | `l.sort()` solo, o `l = sorted(l)` |
| Matriz con `*` | `[[0] * 3] * 3` comparte filas | `[[0] * 3 for _ in range(3)]` |
| Variable posiblemente no definida | `resultado` en `Punto7.py` si la operación no existe | agregar `else` / `case _` |
| División por cero | `num1 / num2` en `Punto1.py` | validar o `try/except ZeroDivisionError` |
| Pisar built-ins | `list = [...]`, `sum = 0` | usar otros nombres |
| `except:` vacío | oculta todos los errores | capturar la excepción específica |
| Clave de diccionario mal escrita | `"precio_unitario  "` (con espacios) en el Punto 18 original → `KeyError` | revisar las claves; usar `get()` si la clave puede faltar |
| Tupla de un elemento | `(5)` es un `int` | `(5,)` |
| `{}` vacío | es un `dict`, no un `set` | `set()` |

---

## 26. Machete final

```python
# Tipos y conversión
int() float() str() bool() list() tuple() dict() set() type() isinstance()

# Built-ins que conviene conocer
print() input() len() range() enumerate() zip() sorted() reversed()
sum() min() max() abs() round() any() all() map() filter() open() help() dir()

# Estructura típica de un script
"""Descripción del programa."""
import math

NOTA_APROBACION = 6

def es_aprobado(nota: float) -> bool:
    return nota >= NOTA_APROBACION

def main() -> None:
    try:
        nota = float(input("Nota: "))
    except ValueError:
        print("Ingresá un número.")
        return
    print("Aprobado" if es_aprobado(nota) else "Desaprobado")

if __name__ == "__main__":
    main()
```

### Complejidad de operaciones frecuentes

| Operación | `list` | `dict` / `set` |
|---|---|---|
| acceso por índice / clave | O(1) | O(1) |
| `x in coleccion` | O(n) | O(1) |
| agregar al final / insertar | O(1) / O(n) | O(1) |
| eliminar | O(n) | O(1) |
| ordenar (`sorted`) | O(n log n) | — |

---

### Recursos para seguir

- [Documentación oficial de Python (en español)](https://docs.python.org/es/3/)
- [Tutorial oficial](https://docs.python.org/es/3/tutorial/)
- [PEP 8 — Guía de estilo](https://peps.python.org/pep-0008/)
- [Python Tutor](https://pythontutor.com/) — visualiza paso a paso cómo se ejecuta tu código y cómo se comportan las referencias en memoria

---

📄 Licencia: ver [LICENSE](LICENSE).
