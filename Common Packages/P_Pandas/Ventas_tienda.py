# Ejercicio para practicar Pandas

import pandas as pd
from rich import print
from rich.table import Table

df = pd.read_csv("ventas.csv") # Se lee el archivo .csv y con pd. lo convertimos en un Dataframe

df["Total_Ventas"] = df["precio"] * df["cantidad"] # Se calcula el total vendido por producto.

top5 = df.sort_values(by="cantidad", ascending=False).head(5) # Obtiene los 5 productos más vendidos (por cantidad).

tabla = Table(title="Top 5 productos más vendidos", title_style="bold yellow", border_style="cyan")
tabla.add_column("Producto", style="bold")
tabla.add_column("Categoría")
tabla.add_column("Cantidad Vendida", justify="right")2
tabla.add_column("Total en $", justify="right")

for _, fila in top5.iterrows(): # Lo que hace es agregar una fila de datos a la tabla y convertir la cantidad en str antes de agregarlo.
    tabla.add_row(
        fila["producto"],
        fila["categoria"],
        str(fila["cantidad"]),
        f"$ {fila['Total_Ventas']:,}"
    )

print(tabla)

ingresos = df["Total_Ventas"].sum()
print(f"\n[bold green]Ingresos totales: [/bold green] ${ingresos:,}")

