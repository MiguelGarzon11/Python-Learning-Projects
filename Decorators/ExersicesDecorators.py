# Ejercicios Básicos para entender los Decoradores de Python

def decorador(func):
    def wrapper():
        print("Antes de llamar a la función")
        func()
        print("Despues de llamar a la función")
    return wrapper

@decorador
def saludo():
    print("Hola!")

saludo()

def decorador_argumentos(func):
    def wrapper(*args, **kwargs):
        print("Llamando a la función con los siguientes argumentos:", args)
        return func(*args, **kwargs)
    return wrapper

@decorador_argumentos 
def suma(a, b):
    return a + b

print(suma(5, 7))


# Ejemplo Básico para entender decoradores

def decorador(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a la función {func.__name__}")
        if args:
            print(f"Argumentos posicionales: {args}")
        if kwargs:
            print(f"Argumentos con nombre: {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"El resultado de {func.__name__}: {resultado}")
        print("Función ejecutada\n")
        return resultado
    return wrapper

@decorador
def suma(*numeros):
    return sum(numeros)

@decorador
def mostrar_info(nombre, edad):
    print(f"Nombre: {nombre}, Edad: {edad}")

suma(3,7,7,8,9)
mostrar_info(nombre="Miguel", edad=17)

