# Ejercicio de grafo Rutas Ciudades

def encontrar_ruta(grafo, origen, destino, visitadas=None, ruta=None):
    if visitadas is None:
        visitadas = set()
    if ruta is None:
        ruta = []
    
    ruta.append(origen)
    visitadas.add(origen)

    if origen == destino:
        return ruta
    
    for vecino, _ in grafo.get(origen, []):
        if vecino not in visitadas:
            resultado = encontrar_ruta(grafo, vecino, destino, visitadas, ruta)
            if resultado:
                return resultado
    
    ruta.pop()
    return None

grafo_ciudades = {
    "Bogota": [('Medellin', 500), ('Cali', 300)],
    "Medellin": [('Bogota', 500), ('Barranquilla', 400)],
    "Cali": [('Bogota', 300), ('Barranquilla', 250)],
    "Barranquilla": [('Medellin', 400), ('Cali', 250)]
}

origen = input("Ingrese la ciudad de origen: \n").strip().capitalize()
destino = input("Ingrese la ciudad de destino: \n").strip().capitalize()

ruta_encontrada = encontrar_ruta(grafo_ciudades, origen, destino)

if ruta_encontrada:
    print(f"Ruta encontrada de {origen} a {destino}: {' ->'.join(ruta_encontrada)}")
else: 
    print(f"No hay ruta disponible entre {origen} y {destino}.")