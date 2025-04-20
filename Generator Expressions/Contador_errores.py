from rich import print
from collections import Counter

try:
    with open("registros.log", "r", encoding="utf-8") as f:
        
        errores = (linea.strip() for linea in f if "ERROR" in linea)

        parsed = ((parts[0]) for linea in errores for parts in [linea.split(" ", 2)])

        conteo = Counter(parsed)

        for fecha in conteo:
            print(f"[bold red]{fecha}[/bold red]: {conteo[fecha]} errores")

except FileNotFoundError:
    print("[bold red]El archivo registros.log no existe[/bold red]")

except Exception as e:
    print(f"[bold red]Error inesperado:[/bold red] {e}")