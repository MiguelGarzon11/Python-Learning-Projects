# Dado un archivo de texto llamado "nombres.txt" que contiene una lista de nombres 
# (uno por línea realiza lo siguiente usando solo funciones puras, funciones de orden superior
# map, filter, reduce, lambda y sin usar bucles explícitos:

from rich import print
from functools import reduce

try:
    with open("nombre.txt", "r", encoding="utf-8") as n:

        nombres = (linea.strip() for linea in n)
        nombres_filtrados = list(filter(lambda x: len(x) > 4, nombres))
        print(f"[yellow]Los nombres que tienen más de 4 letras del archivo 'nombres.txt' son:\n[/yellow]{nombres_filtrados}")

        print(f"[bold white]El número de caracteres de todos los nombres filtrados es de:[/bold white]")
        print(reduce(lambda acumulador, nombre: acumulador + len(nombre), nombres_filtrados, 0))
        

except ValueError:
    print("\n[bold orange]ERROR: Valores incorrectos[/bold orange]\n")

except FileNotFoundError:
    print("\n[bold orange]ERROR: no se reconocio el archivo de nombres.txt[/bold orange]\n")
