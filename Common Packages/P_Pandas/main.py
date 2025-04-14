# Teoría Pandas.

# Pandas es una librería de Python especializada en análisis de dato. Es super poderosa cuando 
# necesitas organizar, transformar, analizar o visualizar datos estrucutrados, como los que vienen
# en archivos .csv, Excel o bases de datos.

# =======¿Para qué sirve?========
# Leer y escribir archivos de datos (CSV, Excel, JSON, etc.)
# Manipular tablas de datos (como si trabajaras en Excel pero con código)
# Limpiar datos (quitar nulos, duplicados, errores)
# Filtrar, agrupar, ordenar o transformar datos
# Hacer estadísticas básicas y análisis de series temporales

# =========Pandas tiene dos estructuras de datos principales:===========

# Series → como una columna de Excel
# ------------------------------------
# import pandas as pd

# serie = pd.Series([10, 20, 30])
# print(serie)
# ------------------------------------
# 0    10
# 1    20
# 2    30
# dtype: int64

# DataFrame → como una tabla de Excel
# ------------------------------------
# import pandas as pd

# datos = {
#     "Nombre": ["Ana", "Luis", "Pedro"],
#     "Edad": [22, 35, 29]
# }

# df = pd.DataFrame(datos)
# print(df)

# ------------------------------------
#   Nombre  Edad
# 0    Ana    22
# 1   Luis    35
# 2  Pedro    29

# =====Leer un archivo CSV con pandas======

# import pandas as pd

# df = pd.read_csv("archivo.csv")
# print(df.head())  # Muestra las primeras 5 filas

