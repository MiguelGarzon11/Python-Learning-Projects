# Ejercicio de Quick Sort, Organización de turnos de un hospital

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]
    mayores = [x for x in lista if x > pivote]
    iguales = [x for x in lista if x == pivote]
    menores = [x for x in lista if x < pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)

numero_turnos = [7,2,9,1,5,8,3,6,4,10]

turnos_organizados = quick_sort(numero_turnos)

print("Turnos organizados:")
for turno in turnos_organizados:
    print(f"Paciente con prioridad {turno}")

