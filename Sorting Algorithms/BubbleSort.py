# Ejercicio de Básico para entender Algoritmos de ordenamiento con bubble Sort
# (Ordemiento de Burbuja)

def bubble_sort(numeros):
    n = len(numeros)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if numeros[j] > numeros[j+1]:
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
                swapped = True
        if not swapped:
            break
    return numeros

lista=[5, 3, 8, 4, 2]
print("Lista ordanada:", bubble_sort(lista))
