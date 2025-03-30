# Ejercicio de grafo conexiones de ciudades


def conexiones_ciudades(grafo):
    while True:
        ciudad = input("Ingrese el nombre de una ciudad: \n").strip()
        
        if ciudad == "salir":
            print("Saliendo del programa...")
            break
        
        if ciudad not in grafo:
            print(f"la ciudad {ciudad} no está en el grafo.")
            continue

        print(f"Ciudades concetadas con {ciudad}:") 
        for vecino, distancia in grafo[ciudad]:
            print(f"-> {vecino} ({distancia} km)")
    

grafo_ciudades = {
    "Bogota": [('Medellin', 500), ('Cali', 300)],
    "Medellin": [('Bogota', 500), ('Barranquilla', 400)],
    "Cali": [('Bogota', 300), ('Barranquilla', 250)],
    "Barranquilla": [('Medellin', 400), ('Cali', 250)]
}


conexiones_ciudades(grafo_ciudades)
