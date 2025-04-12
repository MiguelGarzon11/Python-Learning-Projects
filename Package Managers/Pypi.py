# PyPI Conocer qué es, cómo bucar paquetes, cómo leer su documentación
# https://pypi.org Repositorio oficial de paquetes de python

import requests

r = requests.get("https://api.github.com")

if r.status_code == 200:
    data = r.jason()
    print("Conexión exitosa a la API de Github")
    print("Información general:")
    print(f"- API Version: {data['current_user_url']}")

else:
    print("Hubo un problema al conectarse:", r.status_code)
