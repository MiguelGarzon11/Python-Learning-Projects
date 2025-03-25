# Ejercicio de grafo Red social

red_social = {
    "Juan": ["Pedro", "Ana"],
    "Pedro": ["Juan", "Luis", "María"],
    "Ana": ["Juan", "María"],
    "Luis": ["Pedro"],
    "Miguel": ["Camila", "Maria"],
    "Camila": ["Miguel", "Maria"],
    "Maria": ["Miguel", "Camila", "Pedro", "Ana"]
}

red_social_lower = {nombre.lower(): amigos for nombre, amigos in red_social.items()}

def amigos_comun(red_social_lower):
    while True:
        persona1 = input("Digite la primera persona que quiere comparar los amigos en común (o 'salir' Para terminar):\n").lower()
        if persona1.lower() == "salir":
            break
        
        persona2 = input("Digite la segunda persona que quiere comparar los amigos en común (o 'salir' Para terminar):\n").lower()
        if persona2.lower() == "salir":
            break

        if persona1 not in red_social_lower or persona2 not in red_social_lower:
            print("Las personas no se encuentran en la red social. Intentelo de nuevo.")
            continue
        
        amigos1 = set(red_social_lower[persona1])
        amigos2 = set(red_social_lower[persona2])

        amigos_comunes = amigos1 & amigos2

        if amigos_comunes:
            print(f"Los amigos en común entre {persona1} y {persona2} son:\n" + "\n".join(amigos_comunes))
        
        else:
            print(f"{persona1} y {persona2} no tinen amigos en común.")

amigos_comun(red_social_lower)



# print("Los amigos de Pedro son:", red_social["Pedro"])
# print("los amigos de Luis son:", red_social["Luis"])