# Test de funciones builtin con Modulos

import builtin_functions as bf # Utilizo as para renombrar el modulo y utilizar un nombre más corto

# Conversión de temperaturas
temperaturas = [0, 25, 100]
print("Temperaturas convertidas:", bf.convertir_temperaturas(temperaturas))

# Función que filtra los números pares
numeros = [1,2,3,4,5,6,7,8]
print("Números pares:", bf.obtener_pares(numeros))

# Producto de una lista de números
numeros_producto = [1,2,3,4,5]
print("Producto de la lista:", bf.producto_lista(numeros_producto))

# Combinar dos listas
lista1 = ['a','b','c','d']
lista2 = [1,2,3,4]
print("Listas combinadas:", bf.combinar_listas(lista1, lista2))

# Ordenar palabras por longitud
palabras = ["Python", "Java", "C++", "Css"]
print("Palabras ordenadas:", bf.ordenar_por_longitud(palabras))



