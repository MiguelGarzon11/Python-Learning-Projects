# Ejercio Básico para entender Insert Sort 

# Cada valor se inserta en el lugar correcto comparandolo
# con los anteriores

def insertion_sort_palabras(lista):
    n = len(lista)
    for i in range(1, n):
        clave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = clave
        print(f"Paso {i}: {lista}")

    return lista

palabras = ["Pera", "Manzana", "Uva", "Banana"]
print("Lista original:", palabras)

lista_ordenada = insertion_sort_palabras(palabras)
print("Lista ordenada:", lista_ordenada)
 

def insertion_sort_numeros(lista):
    n = len(lista)
    contador = 0

    for i in range(1, n):
        clave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
            contador += 1

        lista[j + 1] = clave
        print(f"Paso {i}: {lista}")
    
    print(f"Número total de comparaciones: {contador}")
    return lista

lista = [2,34,6,7,7,89,8]
print("Lista original:", lista)

lista_ordenada = insertion_sort_numeros(lista)
print("Lista ordenada:", lista_ordenada)