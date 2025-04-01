# Ejercicio de Gestión de ventas con lambda

precios_prod = [50,100,450,30,21,45,32,21,10,60,70]

precios_descuento = list(map(lambda x: x - (x * 0.10) if x >= 50 else x, precios_prod))
print("Los nuevos precios de los productos con descuento del 10% son:")
for i, precio in enumerate(precios_descuento, start=1):
    print(f"Producto {i}: ${precio:.1f}")
