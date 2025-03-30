# Ejercicio Básico para entender Quick Sort, ordena una lista eligiendo un pivote,
# dividiendo en menores y mayores, y aplicándose recursivamente a cada sublista.


def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + [pivote] + quick_sort(mayores)
    
numeros = [8,3,1,7,0,10,2]

ordenados = quick_sort(numeros)
print("Lista ordenada:", ordenados)

def quick_sort_nombres(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]

    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    return quick_sort_nombres(menores) + iguales + quick_sort_nombres(mayores)

nombres = ["Carlos", "Camila", "Maria", "Miguel", "luis", "Daniel"]

nombres_ordenados = quick_sort_nombres(nombres)
print("Lista de nombres ordenada:\n" + "\n".join(nombres_ordenados))