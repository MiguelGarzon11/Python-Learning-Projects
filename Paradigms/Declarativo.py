# Dado un texto cualquiera, encuentra todas las palabras que tienen más de 5 letras, 
# conviértelas a mayúsculas, y ordénalas alfabéticamente sin repeticiones.

from rich import print

print("[bold violet]Digite un texto que quiera cualquiera:\n[/bold violet]")
texto = input()

partes = texto.split()

palabras = sorted(set([x.upper() for x in partes if len(x) >= 5]))

print("[yellow]\nLas palabras con minimo 5 letras en mayusculas y ordenadas alfabéticamente son:\n[/yellow]")
print(palabras)
