# Teoria para entender Generator Expressions.

# Son como las list comprehensions, pero no crean toda la lista en memoria de inmediato. 
# En su lugar, generan los elementos uno por uno a medida que se necesitan. 
# Esto los hace mucho más eficientes en términos de memoria.

# ===Sintaxis===
# generador = (x * 2 for x in range(1000000))
# Se usa paréntesis ( ) en vez de corchetes [ ]

# Es ideal para datos muy grandes.

# Si se tiene millones de temperaturas. Si usas una list comprehension, ocupas mucha RAM.
# Con un generator expression, solo se calcula cuando lo necesitas, como con next() o un for.

# List Comprehension
# 🔹 Se escribe con corchetes: # [ ]
# 🔹 Crea toda la lista de una vez
# 🔹 Ocupa más memoria
# 🔹 Se usa cuando necesito todos los datos ya

# Generator Expression
# 🔹 Se escribe con paréntesis: # ( )
# 🔹 Crea los datos uno por uno, solo cuando los uso
# 🔹 Ahorra memoria
# 🔹 Se usa cuando no necesito todos los datos al mismo tiempo

# Ejericicio 1
generador = (x for x in range(50) if x % 2 == 0)
print(list(generador))

# Ejercicio 2
precios_usd = [10, 15, 20, 25, 30, 12, 40]
generadorcop = list(x * 4000 for x in precios_usd if x >= 20)
for cop in generadorcop:
    print(f"$ {cop:,.0f} pesos".replace(".",","))

# Ejercicio 3
tamanos_bytes = [512, 2048, 8192, 16384, 64]
generadorby = list(x // 1024 for x in tamanos_bytes if x >= 1024)
for valor in generadorby:
    print(f"Archivo de {valor} KB")