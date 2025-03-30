# Sistema de ranking Top 5 para un videojuego

import heapq 

ranking = []  # heap

def agregar_jugadores(nombre, puntaje):
    heapq.heappush(ranking, (puntaje, nombre))
    print(f"{nombre} con {puntaje} puntos ha sido añadido al ranking.\n")

def mostrar_top_jugadores(n=5):
    print("\n T O P  J U G A D O R E S \n")
    top_jugadores = heapq.nlargest(n, ranking)
    for i, (puntaje, nombre) in enumerate(top_jugadores, start=1):
        print(f"{i}. {nombre} - {puntaje} puntos.\n")

def actualizar_datos():
    nombre_buscar = input("Digite el nombre del jugador que desea actualizar:\n\n")

    for i, (puntaje, nombre) in enumerate(ranking):
        if nombre == nombre_buscar:
            nuevo_puntaje = int(input("Digite el nuevo puntaje:\n"))
            del ranking[i]
            heapq.heapify(ranking)
            heapq.heappush(ranking, (nuevo_puntaje, nombre_buscar))
            print(f"El puntaje de {nombre_buscar} anteriormente de {puntaje} puntos ha sido actualizado con exito a {nuevo_puntaje} puntos.\n")
            return
        print("\nJugador no encontrado.\n")

while True:
    print("\nBienvenido al Menú de visualización\n")
    print("1. Agregar jugadores.")
    print("2. Mostrar Top 5 jugadores.")
    print("3. Actualizar datos.")
    print("4. Salir\n")

    opcion = int(input("Digite un número del (1-4)\n\n"))

    try:
        if opcion == 1:
            nombre = input("Digite el nombre del jugador.\n") # Se pide el nombre del jugador
            puntaje = int(input("\nDigite el puntaje del jugador.\n")) # Se pide el puntaje del jugador
            agregar_jugadores(nombre, puntaje)
        elif opcion == 2:
            mostrar_top_jugadores()
        elif opcion == 3:
            actualizar_datos()
        else:
            print("Opcion incorrecta.\n")
    except ValueError:
        print("ERROR: Dato invalido\n")