from rich import print
from rich.panel import Panel
from itertools import islice # Sirve para tomar solo una porción de un iterable (como los primeros 10 errores, por ejemplo).

try:
    with open("registros.log", "r", encoding="utf-8") as f:

        errores = (linea.strip() for linea in f if "ERROR" in linea)

        parsed = (
            (
                parts[0],
                parts[1],
                parts[2],
            )
            for linea in errores 
            for parts in [ linea.split(" ", 2)]
        )

        primeros_errores = islice(parsed, 10)

        for index, (fecha, nivel, mensaje) in enumerate(primeros_errores, 1):
            print(f"[{index}] {fecha} - [bold red]{nivel}[/bold red] - {mensaje}")

except FileNotFoundError:
    print("[bold red]El archivo registros.log no existe[/bold red]")

except Exception as e:
    print(f"[bold red]Error inesperado:[/bold red] {e}")
