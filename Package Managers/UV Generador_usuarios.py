# UV es un gestor de entornos y dependencias ultrarrápido creado por Astral. Está diseñado como un reemplazo de pip, virtualenv, pip-tools, y pipenv.

# =========PASOS PARA CREAR UN ENTORNO VIRTUAL CON UV=============
# 1. uv --version -> Ver la versión instalada.
# 2. pip install uv -> Instalar uv.
# 3. uv venv .venv -> Esto crea una carpeta con el entorno virtual .venv
# 4. source .venv/bin/activate
# 5. uv pip install requests -> Instalar paquetes con uv
# 6. uv pip freeze > requirements.txt -> Crear un archivo requirements.txt
# 7. uv pip install -r requirements.txt -> Instalar las dependencias de manera automatica del proyecto.
# 8. deactivate -> Desactivar el entorno 
# 9. rm -rf .venv -> Borrar el entorno .venv
# 10. uv python -> Ver la versión de python instalada por uv.

import random
from rich.console import Console

console = Console()

adjetivos = ["rápido", "sabio", "valiente", "curioso", "feliz", "loco", "noble"]
sustantivos = ["león", "fénix", "dragón", "robot", "pirata", "explorador", "mago"]
# UV es un gestor de entornos y dependencias ultrarrápido creado por Astral. Está diseñado como un reemplazo de pip, virtualenv, pip-tools, y pipenv.

# =========PASOS PARA CREAR UN ENTORNO VIRTUAL CON UV=============
# 1. uv --version -> Ver la versión instalada.
# 2. pip install uv -> Instalar uv.
# 3. uv venv .venv -> Esto crea una carpeta con el entorno virtual .venv
# 4. source .venv/bin/activate
# 5. uv pip install requests -> Instalar paquetes con uv
# 6. uv pip freeze > requirements.txt -> Crear un archivo requirements.txt
# 7. uv pip install -r requirements.txt -> Instalar las dependencias de manera automatica del proyecto.
# 8. deactivate -> Desactivar el entorno 
# 9. rm -rf .venv -> Borrar el entorno .venv
# 10. uv python -> Ver la versión de python instalada por uv.

import random
from rich.console import Console

console = Console()

adjetivos = ["rápido", "sabio", "valiente", "curioso", "feliz", "loco", "noble"]
sustantivos = ["león", "fénix", "dragón", "robot", "pirata", "explorador", "mago"]

def generar_usuario():
    adjetivo = random.choice(adjetivos)
    sustantivo = random.choice(sustantivos)
    numero = random.randint(100, 999)
    return f"{adjetivo}_{sustantivo}_{numero}"

if __name__ == "__main__":
    console.print("[bold yellow] ¡Generador de nombres de usuario![/bold yellow]")
    nombre = generar_usuario()
    console.print(f"[bold green]Usuario generado:[/bold green] [italic]{nombre}[/italic]")

def generar_usuario():
    adjetivo = random.choice(adjetivos)
    sustantivo = random.choice(sustantivos)
    numero = random.randint(100, 999)
    return f"{adjetivo}_{sustantivo}_{numero}"

if __name__ == "__main__":
    console.print("[bold yellow] ¡Generador de nombres de usuario![/bold yellow]")
    nombre = generar_usuario()
    console.print(f"[bold green]Usuario generado:[/bold green] [italic]{nombre}[/italic]")
