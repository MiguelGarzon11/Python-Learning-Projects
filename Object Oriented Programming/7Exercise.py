# Dunder Methods Ejemplo practico 

class TiendaVirtual:

    def __init__(self, nombre, prod):
        self._nombre = nombre
        self._prod = prod

    def __repr__(self):
        return f"TiendaVirtual(nombre='{self._nombre}', productos={self._prod})"
    
    def __add__(self, other):
        nueva_lista = self._prod + other._prod 
        nuevo_nombre = self._nombre + "_" + other._nombre
        return TiendaVirtual(nuevo_nombre, nueva_lista)

    def __radd__(self, other):
        if isinstance(other, int):
            nuevo_producto = f'Producto {other}'
            self._prod.append(nuevo_producto)
        return self
    
    def __eq__(self, other):
        if isinstance(other, TiendaVirtual):
            return self._nombre == other._nombre
        return False
    
    def __lt__(self, other):
        if isinstance(other, TiendaVirtual):
            return len(self._prod) < len(other._prod)
        return NotImplemented


t1 = TiendaVirtual("TechStore", ["Mouse", "Teclado"])
t2 = TiendaVirtual("OfficeStore", ["Silla"])

# __repr__
print(t1)  # TiendaVirtual(nombre='TechStore', productos=['Mouse', 'Teclado'])

# __add__
t3 = t1 + t2
print(t3)  # TiendaVirtual(nombre='TechStore_OfficeStore', productos=['Mouse', 'Teclado', 'Silla'])

# __radd__
5 + t1
print(t1)  # Producto 5 debería agregarse

# __eq__
print(t1 == t2)  # False

# __lt__
print(t1 < t2)  # Depende de cuántos productos tenga cada tienda
