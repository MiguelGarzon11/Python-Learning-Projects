# Programa que calcula la suma de los números pares entre 1 y 100 o a y n usando solo estructuras clasicas
# bucles for, condicionales if, y variables.

from rich import print

try:
    print("[bold yellow]Digite el primer número del rango:[/bold yellow]\n")
    a = int(input())
    print("[bold yellow]Digite el segundo número del rango:[/bold yellow]\n")
    b = int(input())
        
    # rango = [x for x in range(a, b) if x % 2 == 0] Paradigma declarativo
    pares = []
    
    for x in range(a, b):
        if x % 2 == 0:
            pares.append(x)


    print(f"[bold white]\nLos números pares dentro del rango de[/bold white] {a} [bold white]y[/bold white] {b} [bold white]son:[/bold white]\n{pares}")

    suma = sum(pares)
    print(f"[bold white]La suma de los números pares en el rango especificado es de:[/bold white]\n{suma}")

except ValueError:
    print("[bold red]ERROR: No se proporciono valores validos.[/bold red]\n")
