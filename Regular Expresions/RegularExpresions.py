# Ejercicios para entender Regular Expresions (Regex).

# . → Representa cualquier carácter

# \d → Representa un dígito (0-9)

# \w → Representa un carácter alfanumérico (letras y números)

# \s → Representa un espacio en blanco

# * → Cero o más repeticiones del carácter anterior

# + → Una o más repeticiones

# ? → Cero o una repetición

# {n} → Exactamente n repeticiones

# [] → Agrupa caracteres específicos ([aeiou] busca vocales)

# ^ → Indica inicio de una línea

# $ → Indica fin de una línea

import re

# texto = "Cumplimos 624 días juntos con mi pollita y Mi novia no quiere venir a verme y me\n " \
# "siento muy triste porque la extraño mucho y me hace muchisima falta"
# patron = r"\d+" # Encuentra todos los números
# resultado = re.findall(patron, texto)
# print(resultado, texto)

texto = "Hola estoy estudiando Regular Expresions de Python"
patron = r"\b[A-Z]\w*"
resultado = re.findall(patron, texto)
print(resultado)

texto = "Tengo 2 perros, 3 gatos y 15 peces en mi casa."
patron = r"\d+"  # Encuentra uno o más dígitos consecutivos
resultado = re.findall(patron, texto)

print(resultado)