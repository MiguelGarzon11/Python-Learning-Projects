# Ejercicio Básico para aprender Merge Sort (ordenamiento por mezcla)

def merge_sort(lista):
    if lista:
        if len(lista) <= 1:
            return lista
        
        mitad = len(lista) // 2

        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        izquierda = merge_sort(izquierda)
        derecha = merge_sort(derecha)

        print(f"Dividiendo: {izquierda} y {derecha}")

        return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i, j = 0, 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado

lista = [50,25,75,100]

print("Lista original", lista)
print("Lista ordenada", merge_sort(lista))


    