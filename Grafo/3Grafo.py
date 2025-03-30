# Ejercicio de grafo red de computadoras

red_computadoras = {
    "PC1": ["PC2", "PC3"],
    "PC2": ["PC1", "PC4"],
    "PC3": ["PC1", "PC5"],
    "PC4": ["PC2", "PC5"],
    "PC5": ["PC3", "PC4"]
}

def buscar_camino(grafo, inicio, objetivo, visitados=None):
    if visitados is None:
        visitados = set()

    if inicio == objetivo:
        return True
    
    visitados.add(inicio)

    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            if buscar_camino(grafo, vecino, objetivo, visitados):
                return True
    return False

print(buscar_camino(red_computadoras, "PC1", "PC5"))
print(buscar_camino(red_computadoras, "PC7", "PC4"))
print(buscar_camino(red_computadoras, "PC1", "PC6"))