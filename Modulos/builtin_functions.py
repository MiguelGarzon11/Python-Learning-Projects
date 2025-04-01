# Funciones builtin

from functools import reduce

# 1. Convertir temperaturas de Celsius a Fahrenheit usando map()

def celsius_a_fahrenheit(temp):
    return (temp * 9/5) + 32

def convertir_temperaturas(lista_temperaturas):
    return list(map(celsius_a_fahrenheit, lista_temperaturas ))

# 2. Filtar números pares usando filter()

def es_par(num):
    return num % 2 == 0

def obtener_pares(lista_numeros):
    return list(filter(es_par, lista_numeros))

# 3. Calcular el producto de una lista usando reduce()

def producto_lista(lista_numeros):
    return reduce(lambda x,y: x * y, lista_numeros)

# lambda es lo mismo que si hicieramos esto:
# def multiplicar(x, y):
#   return x * y 
# reduce aplica esta función acumulativamente a todos los elementos de la lista

# 4. Combinar dos listas en una lista de tuplas zip()

def combinar_listas(lista1, lista2):
    return list(zip(lista1, lista2)) # zip() toma elementos de ambas listas y los empareja en tuplas

# 5. Ordenar una lista de palabras por su longitud usando sorted()

def ordenar_por_longitud(lista_palabras):
    return sorted(lista_palabras, key=len) # sorted() ordena la lista usando len como clave de ordenación
