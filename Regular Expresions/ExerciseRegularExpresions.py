# Ejercicio filtrado y valoración de datos de contacto

import re

texto ="""
Nombre: Juan Pérez, Email: juan.perez@gmail.com, Teléfono: +57-3201234567
Nombre: Maria Gómez, Correo: maria.gomez@empresa.com, Tel: 601-4567890
Pedro Ramírez - pedro99@correo.net - 315-9876543
Carlos - correo: carlos123@dominio, tel: 300999888
"""

# 1. Expresión regular para extraer ** Correos Electrónicos **
patron_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
correos = re.findall(patron_email, texto)

# 2. Expresión regular para extraer **Números de Teléfono** (soporta formato internacional y local)
patron_telefono = r"(\+?\d{1,3}-?\d{3,}-?\d{4,})"
telefonos = re.findall(patron_telefono, texto)

# 3. Expresión regular para extraer **Nombres de los Empleados**
patron_nombres = r"Nombre:\s*([\w\sáéíóúÁÉÍÓÚñÑ]+)|([\w\sáéíóúÁÉÍÓÚñÑ]+)\s*-\s*\w+@"
matches_nombres = re.findall(patron_nombres, texto)
nombres = [match[0] if match[0] else match[1] for match in matches_nombres]

print("Correos electrónicos encontrados:")
print(correos)

print("\nNúmeros de teléfono encontrados:")
print(telefonos)

print("\nNombres de empleados encontrados:")
print(nombres)