# Test de Custom Functions.

import custom_functions as cf

# 1. Aplicar una función a cada elemento de una lista.
def cuadrado(n):
    return n * n

numeros = [1,2,3,4]
print("Lista elevada al cuadrado:", cf.map(cuadrado, numeros))

# 2. Filtrar elementos de una lista según una condición.
def es_par(n):
    return n % 2 == 0

numeros_filter = [1,2,3,4,5,6,7,8,9,0]
print("Números pares:", cf.filter(es_par, numeros_filter))

# 3. Reduce producto acumulativo de una lista
def multiplicar(x, y):
    return x * y

numeros_pro = [1,2,3,4]
print("Producto de los números:", cf.reduce(multiplicar, numeros_pro))

# 4. Unir dos listas en una lista de tuplas.
lista1 = ["a","b","c","d"]
lista2 = [1,2,3,4,5]
print("Listas combinadas:", cf.zip(lista1, lista2))

