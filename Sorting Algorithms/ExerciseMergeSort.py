# Ejercicio de ordenamiento de paquetes de una bodega, utilizando el algortimo de ordenamiento Merge Sort

# Tengo una lista de paquetes con diferentes pesos, Tengo que ordenarlos de menor a mayor peso.

peso_paquetes = [[5,"kg"],[7,"kg"],[45,"kg"],[98,"kg"],[23,"kg"],[34,"kg"],[5,"kg"],[4,"kg"]]

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
        
    mitad = len(lista) // 2

    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    print(f"\n **Ordenando:**\n{formatear_paquetes(izquierda)}\n🔸 con\n{formatear_paquetes(derecha)}\n")
        
    return merge(izquierda, derecha)
    
def merge(izquierda, derecha):
    resultado = []
    i, j = 0, 0 

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i][0] < derecha[j][0]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado

def formatear_paquetes(lista):
    return "\n".join(f"📦 {peso} {unidad}" for peso, unidad in lista)

print("**Lista original:**\n" + formatear_paquetes(peso_paquetes) )
paquetes_ordenados = merge_sort(peso_paquetes)
print("\n**Lista ordenada:**\n" + formatear_paquetes(paquetes_ordenados))
