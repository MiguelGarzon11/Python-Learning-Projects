#  Conda es un gestor de entornos como un gestor de paquetes, Lo más común es usarlo a través de Anaconda o Miniconda.

# Instala paquetes 
# Crea entornos virtuales aislados, pero a nivel del sistema.
# Tiene su propio repositorio de paquetes llamado Anaconda Cloud, Aunque tambien se puede instalar desde Pypi.

# =========PASOS PARA CREAR UN ENTORNO VIRTUAL CON CONDA=============

# 1. conda --version -> verificar que conda o Miniconda esta instalado.
# 2. conda create --name mi_entorno python=3.11 -> crear un entorno.
# 3. conda activate mi_entorno -> activar el entorno.
# 4. conda or pip install numpy -> Instalar paquetes.
# 5. conda deactivate -> Desactivar el entorno.
# 6. conda remove --name mi_entorno --all -> Borrar algún entorno.
# 7. conda env list -> ver todos mis entornos.

import secrets  # se usa para generar datos seguros aleatorios
import string # string.ascii_letters + string.digits # + string.punctuation
from rich.console import Console 

console = Console()

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits # + string.punctuation
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña

if __name__ == "__main__":
    console.print("[bold yellow] ¡Generador de Contraseñas Seguras![/bold yellow]")
    try:
        longitud = int(input("¿Qué longitud quieres para tu contraseña?\n"))
        contraseña = generar_contraseña(longitud)
        console.print(f"[bold green]Tu contraseña segura es: [/bold green] [italic]{contraseña}[/italic]")
    except ValueError:
        console.print("[bold red]Por favor ingresa un número valido.[/bold red]")