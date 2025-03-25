# Ejercicio de Laberinto

# Imagina un laberinto representado como un grafo no dirigido. 
# Cada nodo es una sala y cada conexión representa un pasillo entre dos salas.

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

sala_usuario = input("Digite la sala de la cual quiere saber las salas conectadas:\n").strip().upper()
muestra_sala_conectada(sala_usuario)