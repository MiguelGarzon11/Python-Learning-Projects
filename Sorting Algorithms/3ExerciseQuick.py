# Ejercicio Organización de Proyectos Empresariales con Quick Sort

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    mitad = len(lista) // 2
    pivote = lista[mitad][1]
    menores = [x for x in lista if x[1] < pivote]
    iguales = [x for x in lista if x[1] == pivote]
    mayores = [x for x in lista if x[1] > pivote]
    
    return quick_sort(menores) + iguales + quick_sort(mayores)

proyectos = [
    ("Lanzamiento App", "2025-07-15"),
    ("Revisión de Marketing", "2025-06-20"),
    ("Actualización Servidores", "2025-05-10"),
    ("Capacitación del Personal", "2025-08-05"),
]

proyectos_ordenados = quick_sort(proyectos)
print("Proyectos ordenados por fecha de entrega")
for nombre, fecha in proyectos_ordenados:
    print(f"Proyecto: {nombre}. Fecha de entrega: {fecha}")