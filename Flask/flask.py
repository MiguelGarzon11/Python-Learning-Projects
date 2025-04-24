# Flask es un microframework, lo que significa que es ligero y minimalista, proporcionando 
# solo las herramientas necesarias para comenzar a construir una aplicación web.

from flask import Flask

app = Flask(_name_) # Crea la aplicación Flask

@app.route("/") # Define la ruta para la página principal
def home():
    return "¡Hola, Mundo!"

if __name__="__main__":
    app.run(debug=True) # Corre la aplicación en modo de desarrollo (automáticamente recarga si haces cambios en el código)

# Rutas: Usamos @app.route() para definir qué funciones corresponden a qué URL.
# Plantillas: Flask usas Jinja2 como motor de plantillas. Pueden crear archivos HTML con variables que se rellenan dinámicamente.
# Bases de datos: Flask se íntegra fácilmente con bases de datos MySQL, PostgreSQL, o SQLite mediante extensiones como Flask-SQLAlchemy.

