import numpy as np
from rich import print
from rich.panel import Panel

temperaturas = np.array([
    [18, 19, 20, 22, 24, 26, 28, 29, 30, 30, 28, 26, 24],  # Lunes
    [17, 18, 19, 21, 23, 25, 27, 28, 29, 29, 27, 25, 23],  # Martes
    [19, 20, 21, 23, 25, 27, 29, 30, 31, 31, 29, 27, 25],  # Miércoles
    [20, 21, 22, 24, 26, 28, 30, 31, 32, 32, 30, 28, 26],  # Jueves
    [18, 19, 21, 22, 24, 25, 27, 28, 29, 29, 27, 25, 24],  # Viernes
    [16, 17, 18, 20, 22, 24, 26, 27, 28, 28, 26, 24, 22],  # Sábado
    [15, 16, 17, 19, 21, 23, 25, 26, 27, 27, 25, 23, 21],  # Domingo
])

t_miercoles = temperaturas[2]
print("\n[bold cyan]Temperaturas registradas el miércoles[/bold cyan]")
for i, temperatura in enumerate(t_miercoles, start=6):
    if i < 12:
        print(f"[yellow]Temperatura registrada a las[/yellow] {i}:00 am: {temperatura}°")
    else:
        print(f"[red]Temperatura registrada a las[/red] {i}:00 pm: {temperatura}°")

t_12pm = temperaturas[:,6]
datos = ""
for i, temperatura in enumerate(t_12pm, start=1):
    salto= "\n" if i < len(t_12pm) else ""
    datos += f"Día {i} Temperatura: {temperatura}°{salto}"

print(Panel.fit(
    datos,
    title= f"[bold cyan]Temperaturas registradas todos los días a las 12[/bold cyan]",
    border_style="violet"
    ))


