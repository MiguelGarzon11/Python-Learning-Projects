# Téoria para entender list comprehensions.
# Sintaxis
 
# [ expresión for elemento in iterable if condición ]

# expresión: lo que queremos hacer con cada elemento del iterable.
# for elemento in iterable: recorrer cada elemento del iterable.
# if condición: opcionalmente, podemos filtrar los elementos con una condición.


cuadrados = [x**2 for x in range(1, 6)] # Recorrer los números del 1 al 5 y Elevarlo al cuadrado.
print(cuadrados)

pares = [x for x in range(1, 11) if x % 2 == 0]
print(pares)

nombres = ["camila","miguel", "oliver", "margarita"]
nombres_mayus = [nombre.upper() for nombre in nombres]
print(nombres_mayus)

temperaturas_celcius = [0, 10, 20, 30, 40, 50]
fahrenheit = [(x * 9//5) + 32 for x in temperaturas_celcius]
print(fahrenheit)

palabras = ["manzana", "plátano", "cereza", "mango"]
longitud_palabras = [len(x) for x in palabras]
print(longitud_palabras)

palabrasF = ["manzana", "plátano", "cereza", "mango", "pera"]
filtrar_palabras = [x for x in palabrasF if len(x) > 5]
print(filtrar_palabras)