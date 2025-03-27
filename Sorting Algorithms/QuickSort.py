# Ejercicio Básico para entender Quick Sort, ordena una lista eligiendo un pivote,
# dividiendo en menores y mayores, y aplicándose recursivamente a cada sublista.


def quick_sort(lista, pivote):
    if len(lista) <= 1:
        return lista
    
    pivote = numeros[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + [pivote] + quick_sort(mayores)
    
numeros = [8,3,1,7,0,10,2]

ordenados = quick_sort(numeros)
print("Lista ordenada:", quick_sort(ordenados))