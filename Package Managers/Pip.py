# pip (Package Installer for Python)


# Instalar paquetes desde Pypi
# Desinstalarlos
# Listar todos los paquetes que tienes instalados
# Guardar dependencias en un archivo (requirements.txt)
# Instalarlas desde ese archivo

# pip install nombre_paquete    -> Instalar un paquete
# pip uninstall nombre_paquete  -> Desinstalar un paquete
# pip list  -> Ver qué paquetes tienes instalados
# pip show nombre_paquete   -> Ver la info de un paquete (versión, ubicación, etc.)
# pip freeze    -> Lista todos los paquetes + versión (ideal para exportar)
# pip install -r requirements.txt   -> Instala desde un archivo de dependencias

import requests

def obtener_clima(ciudad):
    url = f"https://wttr.in/{ciudad}?format=3"
    response = requests.get(url)    # Petición GET solicita información a la URL que construimos.
    if response.status_code == 200: # El código 200 significa que todo salió bien, si no, puede haber errores como 404 (no encontrado).
        print(response.text)
    else:
        print("No se pudo obtener el clima. Intenta de nuevo.")

if __name__ == "__main__":
    ciudad = input("Ingresa el nombre de una ciudad:\n")
    obtener_clima(ciudad)

