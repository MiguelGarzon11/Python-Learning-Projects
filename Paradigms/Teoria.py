# Son formas de pensar y estructurar el código. Cada paradigma 
# tiene sus reglas, ventajas y estilo.

# ===Paradigma Imperativo===

# “Paso a paso”. Le dices a la máquina qué hacer y cómo hacerlo.
# Ej: uso de for, if, variables y funciones comunes.

# suma = 0
# for i in range(5):
#     suma += i
# print(suma)

# ===Paradigma Declarativo===
# En lugar de decir cómo, describes qué quieres que pase.
# Python no es completamente declarativo, pero puedes ver este enfoque con librerías como pandas.

# En SQL: SELECT nombre FROM clientes WHERE edad > 18
# En Python (declarativo)
# mayores = [c["nombre"] for c in clientes if c["edad"] > 18]

# ===Paradigma Funcional===
# Usa funciones puras (sin efectos secundarios), evita variables mutables, usa map, filter, reduce, lambda.
# En Python puedes combinarlo con programación imperativa.

# numeros = [1, 2, 3, 4, 5]
# cuadrados = list(map(lambda x: x**2, numeros))

# ===Paradigma Orientado a Objetos (OOP)===
# Basado en objetos que representan entidades del mundo real. Muy usado en proyectos grandes.
# Incluye clases, atributos, métodos, herencia, encapsulamiento, polimorfismo, etc.

# class Persona:
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def saludar(self):
#         print(f"Hola, soy {self.nombre}")
