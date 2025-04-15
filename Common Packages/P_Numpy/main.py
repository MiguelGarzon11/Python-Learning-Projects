# Entendimiento de Numpy.

# Es la librería base para cálculos numéricos y científicos. Permite trabajar con arrays, 
# operaciones matemáticas rápidas, y sirve como base para otras librerías como pandas, 
# scikit-learn, matplotlib, etc.

# ===========Lo que aprenderás con NumPy:=================

# Qué es un array de NumPy y cómo crearlo.
# Operaciones básicas con arrays (suma, resta, producto, etc.).
# Indexado y slicing.
# Funciones estadísticas (mean, sum, std, etc.).
# Broadcasting.
# Generación de datos aleatorios.


# import numpy as np

# Crear un array bidimensional

# matriz = np.array([[1,2],[3,4]])  # Convierte una lista o lista de listas de python en un array de Numpy
# print(matriz)

# Crear arrays con valores automáticos

# print(np.zeros(5))        # [0. 0. 0. 0. 0.]  # Crea un array de n elementos todos con valor de 0
# print(np.ones((2, 3)))    # matriz 2x3 de unos    # Crea un array de n elementos todos con valor de 1
# print(np.arange(0, 10, 2))  # [0 2 4 6 8]     # Crea un array de números que empiezan en (inicio), termina en (fin), y salta de (paso).
# print(np.linspace(0, 1, 5)) # 5 valores entre 0 y 1   # Crea un array con una cantidad fija de valores equidistantes entre (inicio) y (fin), incluyendo el final.