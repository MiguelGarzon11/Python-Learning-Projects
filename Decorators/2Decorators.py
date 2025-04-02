# Ejercicios Básicos para entender *args y **kwargs


# Entender *args

def suma(*numeros):
    resultado = sum(numeros)
    print(f"Suma de {numeros} es {resultado}")

suma(3,5)
suma(3,5,7,3)
suma(1,2,3,74,2)

# Entender **kwargs
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Miguel", edad=18)
mostrar_info(nombre="Camila", edad=18, apodo="Pollita", país="Colombia")

# Combinar *args y **kwargs
def combinar(*args, **kwargs):
    print("Argumentos posicionales:", args)
    print("Argumentos con nombre:", kwargs)

combinar(1,2,3,4, nombre="Miguel", edad=18)
 