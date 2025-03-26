# Ejercicio de Laberinto

# Imagina un laberinto representado como un grafo no dirigido. 
# Cada nodo es una sala y cada conexión representa un pasillo entre dos salas.

from collections import deque

laberinto = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

def muestra_sala_conectada(sala):
    if sala not in laberinto:
        print("Esa sala no exite en el laberinto")
        return
    
    conexiones = laberinto[sala]
    print(f"Las salas conectadas a {sala} son: {', '.join(conexiones)}")

# sala_usuario = input("Digite la sala de la cual quiere saber las salas conectadas:\n").strip().upper()
# muestra_sala_conectada(sala_usuario)

def buscar_camino(laberinto, inicio, fin):
    if inicio not in laberinto or fin not in laberinto:
        return "Una o ambas salas no existen en el laberinto."
    
    cola = deque([[inicio]])
    visitados = set()

    while cola:
        camino = cola.popleft()
        sala_actual = camino[-1]

        if sala_actual == fin:
            return f"Camino encontrado: {'->'.join(camino)}"
        if sala_actual not in visitados:
            visitados.add(sala_actual)

            for sala_vecina in laberinto[sala_actual]:
                if sala_vecina not in visitados:
                    nueva_ruta = camino + [sala_vecina]
                    cola.append(nueva_ruta)
    
    return "No hay camino entre las salas."

inicio = input("Ingrese la sala de inicio:\n").strip().upper()
fin = input("Ingrese la sala de destino:\n").strip().upper()

print(buscar_camino(laberinto, inicio, fin))

