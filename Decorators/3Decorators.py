from datetime import datetime

# 1. Ejercicio crear una funcion que acepte *args y **kwargs

def registrar_venta(*args, **kwargs):
    print("Productos vendidos:")
    for i, producto in enumerate(args, start=1):
        print(f"{i}. {producto}")
    print("Información del comprador:",)
    for clave, valor in kwargs.items():
        print(f"-{clave}: {valor}")

registrar_venta("Laptop","Mouse","Monitor","Teclado", nombre="Miguel", ciudad="Bogotá", correo="miguelangelgarb@gmail.com")

# 2. Ejercicio crear un decorador utilizando *args y **kwargs
def verificar_edad(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("edad", 0) >= 18:
            return func(*args, **kwargs)
        else:
            print(f"¡{args[0]} No tienes permiso para realizar esta función!")
    return wrapper

@verificar_edad
def comprar_alcohol(nombre, edad):
    print(f"{nombre} ha comprado alcohol.")

@verificar_edad

def paracaidas(nombre, edad):
    print(f"{nombre} se puede lanzar de paracaidas.")


comprar_alcohol("Miguel", edad=18)
comprar_alcohol("Camila", edad=17)
paracaidas("Miguel", edad=18)
paracaidas("Camila",edad=17)

# 3. Ejercicio crear decorador utilizando *args y **kwargs

def registrar_intentos(func):

    def envoltura(*args, **kwargs):
        # Decorador que registra los intentos de inicio de sesión en un archivo.
        usuario = args[0]
        resultado = func(*args, **kwargs)
        estado = "Éxito" if resultado else "Fallo"

        with open("registrar_intentos.txt", "a") as archivo:
            archivo.write(f"{datetime.now()} - Usuario: {usuario} - Estado: {estado}\n")
        return resultado
    return envoltura

@registrar_intentos
def iniciar_sesion(usuario, contraseña):
    # función que simula un inicio de sesión.
    usuario_registrados = {"admin": "0407", "Camila": "777"}
    return usuario_registrados.get(usuario) == contraseña

print(iniciar_sesion("admin", "0407"))
print(iniciar_sesion("Camila", "777"))
print(iniciar_sesion("Miguel", "2442"))