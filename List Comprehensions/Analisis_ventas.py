from rich import print
from tabulate import tabulate
import colorama 

ventas = [
    {"cliente": "Ana", "producto": "Laptop", "total": 3500000, "estado": "completado"},
    {"cliente": "Luis", "producto": "Mouse", "total": 80000, "estado": "pendiente"},
    {"cliente": "Carlos", "producto": "Monitor", "total": 1200000, "estado": "completado"},
    {"cliente": "Lucía", "producto": "Teclado", "total": 150000, "estado": "completado"},
    {"cliente": "Sara", "producto": "Laptop", "total": 3400000, "estado": "cancelado"}
]

ventas_filtradas = [x for x in ventas if x["estado"] == "completado" and x["total"] >= 1000000]

# No es necesario en este caso pero asi se obtienen valores de diccionarios utilizando list comprehensions.

# datos = [list(fila.values()) for fila in ventas_filtradas] 
# encabezados = list(ventas_filtradas[0].keys())

print(tabulate(ventas_filtradas, headers="keys", tablefmt="fancy_grid"))
# "plain"   "github"    "fancy_grid"    "orgtbl"
# "simple"  "grid"  "pipe" (Markdown)   "jira"
# "html" (para web)

print(f"[bold green]Total de ventas filtradas:[/bold green]{len(ventas_filtradas)}\n")

c_especial = [x for x in ventas_filtradas if x["producto"] == "Laptop"]
if c_especial:
    print(f'[bold white]Cliente especial con laptop:[/bold white] [cyan]{c_especial[0]["cliente"]}[/cyan]')
else:
    print("[bold red]No hay clientes con Laptop[/bold red]")



