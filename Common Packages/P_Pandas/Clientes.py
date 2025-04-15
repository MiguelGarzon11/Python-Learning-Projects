# Ejercicio de Practica con la libreria Pandas.
 
import pandas as pd 
from rich import print
from rich.table import Tablei

df = pd.read_csv("clientes.csv")

promedio_compras = df["compras"].mean() # Se calcula el promedio de compras.

top3 = df.sort_values(by="total_gastado", ascending=False).head(3)

tabla = Table(title="Top 3 clientes mayores compras", title_style="bold purple", border_style="yellow")
tabla.add_column("Nombre", style="bold")
tabla.add_column("Edad")
tabla.add_column("Ciudad")
tabla.add_column("Compras", justify="right")
tabla.add_column("Total gastado", justify="right")
tabla.add_column("Promedio de compras", justify="right")

for _, fila in top3.iterrows():
    tabla.add_row(
        fila["nombre"],
        str(fila["edad"]),
        fila["ciudad"],
        str(fila["compras"]),
        f"$ {fila['total_gastado']:,}",
        f"{promedio_compras:.2f}",
    )

print(tabla)

gastos = df["total_gastado"].sum()
gastos_str = f"{gastos:,}".replace(".",",")
print(f"\n[bold orange]Gastos totales por los clientes: [/bold orange] ${gastos_str}")
