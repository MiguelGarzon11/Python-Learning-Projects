# Ejercicio de Organización de documentos de oficina con algoritmo de organización Quick Sort 


def quick_sort(lista):
    if len(lista) <= 1:
        return lista # La lista ya esta ordenada
    
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)

numero_paginas = [120, 15, 200, 45, 90, 30, 10, 75]

documentos_ordenados = quick_sort(numero_paginas)
print("Documentos ordenados por número de paginas:")
print("\n".join(map(str, documentos_ordenados)))




