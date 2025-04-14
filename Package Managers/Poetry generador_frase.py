# Poetry es un gestor de dependencias y entornos virtuales para python.
# Gestionar dependencias (igual que requirements.txt, pero más potente y organizado).
# Crear y publicar paquetes de Python fácilmente.
# Manejar entornos virtuales automáticamente.
# Fijar versiones exactas de dependencias en un archivo llamado poetry.lock.

# ===Archivos Principales===
# pyproject.toml -> Aqui se declara todo: nombre del proyecto, dependencias, versión, scripts.
# poetry.lock -> Guarda versiones exactas para garantizar que el entorno sea 100% reproducible.

# =========PASOS PARA CREAR UN ENTORNO VIRTUAL CON UV=============
# 1. Poetry new mi_proyecto -> Crear un nuevo proyecto
# 2. cd mi_proyecto; poetry add flask requests numpy -> Agregar dependencias.
# 3. poetry install -> Si alguien te comparte un proyecto con pyproject.toml y poetry.lock esto instala todas las dependecias.
# 4. poetry run python main.py -> Ejecutar comandos del entorno virtual
# 5. poetry env activate -> Activar el entorno.
# 6. deactivate -> Desactivar el entorno
# 7. poetry env remove <nombre-del-entorno> -> Eliminar un entorno.



from rich.console import Console
import random

console = Console()

sujetos = ["El gato", "Una inteligencia artificial", "Un dragón", "Mi vecino", "La computadora"]
verbos = ["come", "programa", "persigue", "canta", "sueña"]
complementos = ["una pizza", "un algoritmo", "estrellas", "poesía", "códigos secretos"]

def generar_frase():
    sujeto = random.choice(sujetos)
    verbo = random.choice(verbos)
    complemento = random.choice(complementos)
    return f"{sujeto} {verbo} {complemento}"

if __name__ == "__main__":
    console.print("[bold cyan] Generador de frases aleatorias [/bold cyan]\n")
    frase = generar_frase()
    console.print(f"[green]Frase generada:[/green] [italic]{frase}[/italic]")

