# Ejercicio para practicar Requests dentro de un entorno virtual UV.

import requests
from rich.console import Console

console = Console()

sitio_web = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org",
    "https://www.este-no-existe.com"
]

def verificar_estado(url):
    try:
        respuesta = requests.get(url, timeout=5)
        if respuesta.status_code == 200:
            console.print(f"{url} [bold green]está online.[/bold green]")
        else:
            console.print(f"{url} [bold wine]respondió con código[/bold wine] [italic]{respuesta.status_code}.[/italic]")
    except requests.exceptions.RequestException as error:
        console.print(f"[bold red]Error al conectar con[/bold red] [italic]{url}[/italic][bold red]:[/bold red] [bold orange]{error}[/bold orange]")

if __name__ == "__main__":
    console.print("[bold blue]Verificando estado de sitios web...[/bold blue]\n")
    for sitio in sitio_web:
        verificar_estado(sitio)
