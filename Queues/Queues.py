# Simular una cola donde se atienden clientes en orden de llegada y si cuenta con 
# membresia de exclusividad VIP (Queue).

from collections import deque

cola = deque()
cola_vip = deque()

def agregar_cliente(nombre, membresia):
    if membresia == 0:
        cola.append(nombre)
        print(f"{nombre} ¡ Se añadio correctamente a la cola de atención !\n")
    elif membresia == 1:
        cola_vip.append(nombre)
        print(f"{nombre} ¡ Se añadio correctamente a la fila preferencial VIP !\n")

def atender_clientes():
    if not cola_vip:
        if cola:    
            print(f"Se esta atendiendo a: {cola.popleft()}\n")
        else:
            print("No hay clientes que atender")
    else:
        print(f"Se esta atendiendo a {cola_vip.popleft()}\n")
    

while True:
    
    print(f"¡ Hola Bienvenido al Menú Principal !")
    print("1. Agregar Cliente.")
    print("2. Mostrar fila de espera.")
    print("3. Mostrar fila preferencial.")
    print("4. Atención en turno.")
    print("5. Salir")

    try:
    
        opcion = int(input("Digite un número del (1-5):\n\n"))
        
        if opcion == 1: 
            nombre = input("Digite su nombre por favor:\n")
            membresia = int(input("Digite (1) si tiene la membresia vip, (0) si no cuenta con membresia vip:\n"))
            
            if membresia == 1:
                agregar_cliente(nombre, membresia)
            elif membresia == 0:
                agregar_cliente(nombre, membresia)
            else:
                print("\n¡ Error: Digite valores validos !\n")
            continue
        
        elif opcion == 2:
            print("La fila de espera es:\n")
            if cola:
                print("\n".join(f"{i}. {cliente}" for i, cliente in enumerate(cola, start=1)))
            else:
                print("No hay clientes en la fila de espera.")
        
        elif opcion == 3:
            print("La fila de espera preferencial es: \n")
            if cola_vip:
                print("\n".join(f"{i}. {cliente}" for i, cliente in enumerate(cola_vip, start=1)))
            else:
                print("No hay clientes en la fila preferencial.\n")
        elif opcion == 4:
            atender_clientes()

        elif opcion == 5:
            print("¡ Gracias por usar el programa. Saliendo...!\n")
            break
        else:
            print("\n¡ Digite valores validos !\n")
        
    except ValueError:
        print("¡ Error: Digite valores validos !")