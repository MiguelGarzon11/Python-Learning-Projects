import numpy as np
from rich import print

notas = np.array([
  [3.5, 4.0, 2.8],
  [4.2, 3.9, 4.5],
  [2.8, 3.1, 3.6],
  [5.0, 4.8, 4.9]
])

promedio = notas.mean()

print("Número de estudiantes:", notas.shape[0])
print("Número de materias:", notas.shape[1])
print(f"Nota promedio general: {promedio:.2f}")
print("Nota más alta:", notas.max())
print("Nota más baja:", notas.min())

p_fila = notas.mean(axis=1)
for i, nota in enumerate(p_fila, start=1):
    print(f"[yellow]Estudiante[/yellow] {i} [yellow]con promedio[/yellow] {nota:.1f}")

p_materia = notas.mean(axis=0)
for i, nota in enumerate(p_materia, start=1):
    print(f"[green]Promedio de calificación para la materia [bold violet]{i}[/bold violet]: [/green]{nota}")
    

