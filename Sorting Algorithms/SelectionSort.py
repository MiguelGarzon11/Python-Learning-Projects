# Ejercicio Básico para entender Selection Sort

# Selection Sort busca el elemento más pequeñó o más grande 
# de la lista y lo ubica en el lugar correcto

def selection_sort(lista):
    n = len(lista)
    comparaciones= 0

    for i in range(n):
        menor = i
        for j in range(i+1,n):
            comparaciones += 1
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
        print(f"Paso: {i+1}: {lista}")
    return lista, comparaciones

lista = [5,6,8,9,3,4]
print("Lista original:", lista)

lista_ordenada, total_comparaciones = selection_sort(lista)
print("Lista ordenada:", lista_ordenada)
print(f"Número total de comparaciones: {total_comparaciones}\n\n\n")

def selection_sort_decendente(lista2):
    n = len(lista2)
    comparaciones = 0

    for i in range(n):
        mayor = i
        for j in range(i+1, n):
            comparaciones += 1
            if lista2[j] > lista2[mayor]:
                mayor = j
        lista2[i], lista2[mayor] = lista2[mayor], lista2[i]
        print(f"Paso: {i+1}: {lista2}")
    return lista2, comparaciones

lista2 = [2,5,6,8,43,3,45,6]
print("Lista original:", lista2)

lista_ordenada2, total_comparaciones2 = selection_sort_decendente(lista2)
print("Lista ordenada:", lista_ordenada2)
print(f"Número total de comparaciones: {total_comparaciones2}")



