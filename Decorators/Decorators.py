# Ejercicio de Registro de Tiempo en una tienda online

import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"La función '{func.__name__}' tardó {fin - inicio:.2f} segundos en ejecutarse.\n")
        return resultado
    return wrapper

@medir_tiempo
def procesar_pedido():
    print("Procesando pedido...")
    time.sleep(2)
    print("Pedido procesado correctamente.")

@medir_tiempo
def generar_reporte():
    print("Generando informe de ventas...")
    time.sleep(3)
    print("Informe generado con éxito.")

procesar_pedido()
generar_reporte()