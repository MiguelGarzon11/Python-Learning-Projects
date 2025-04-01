# Ejercicios para entender Custom Functions 

# 1. Aplicar una función a cada elemento de una lista.
def map(funcion, iterable):
    resultado = []
    for elemento in iterable:
        resultado.append(funcion(elemento))
    return resultado

# 2. Filtar los elementos de una lista según una condición.
def filter(funcion, iterable):
    resultado = []
    for elemento in iterable:
        if funcion(elemento):
            resultado.append(elemento)
    return resultado 

# 3.  Aplicar una operación acumulativa sobre una lista.
def reduce(funcion, iterable, inicial=None):
    it = iter(iterable)

    if inicial is None:
        valor = next(it)
    else:
        valor = inicial
    
    for elemento in it:
        valor = funcion(valor, elemento)

    return valor

# 4. Unir dos listas en una lista de tuplas.
def zip(iterable1, iterable2):
    resultado = []
    for i in range(min(len(iterable1), len(iterable2))):
        resultado.append((iterable1[i], iterable2[i]))
    return resultado
