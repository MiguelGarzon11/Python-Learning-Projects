import requests # modulo request sirve para hacer peticiones HTTP como cuando un navegador visita un sitio web
from rich import print # Sobreescribe la función print para que se vea más estilizado en la terminal
from rich.panel import Panel # Panel es una libreria de rich que permite mostrar texto dentro de un recuadro bonito.

def verificar_usuario(user_id):
    url = f"https://dummyjson.com/users/{user_id}" # dummyjson es una API que proporciona datos simulados.
    try:
        respuesta = requests.get(url) # Se hace una petición GET a esa url.
        respuesta.raise_for_status() # Esta linea lanza un error automáticamente si la respuesta fue un fallo.
        datos = respuesta.json() # Convierte la respuesta en formato JSON(Diccionario de Python)

        nombre = f"{datos['firstName']} {datos['lastName']}"
        email = datos['email']
        activo = datos.get('activo', False)

        estado = "[green]Activo[/green]" if activo else "[red]Inactivo[/red]"

        print(Panel.fit( # Panel imprime el contenido en un cuadro bonito, con titulo y colores. fit() ajusta el tamaño del cuadro al contenido
            f"[bold cyan]Usuario:[/bold cyan] {nombre}\n"
            f"[bold]Email:[/bold] {email}\n"
            f"[bold]Estado:[/bold] {estado}",
            title = f"Verificación del Usuario #{user_id}",
            border_style="cyan"
        ))

        if not activo:
            print("[bold yellow]Este usuario no está activo. Conectar soporte.[/bold yellow]")
        
    except requests.exceptions.RequestException as e:
        print(f"[bold red]Error al consultar el usuario:[/bold red] {e}")
    
if __name__ == "__main__":
    verificar_usuario(5)
    verificar_usuario(6)
    verificar_usuario(7)
    verificar_usuario("y")