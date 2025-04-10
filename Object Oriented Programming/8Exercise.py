# Dunder methods Ejercicio Practico Biblioteca.

class Biblioteca:
    lista_bibliotecas = []  

    def __init__(self, nombre, libros):
        self.nombre = nombre
        self.libros = libros

        for biblio in Biblioteca.lista_bibliotecas:
            if biblio.nombre == nombre:
                raise ValueError(f"Ya existe una biblioteca con el nombre '{nombre}'.")
        
        Biblioteca.lista_bibliotecas.append(self)
    
    def __repr__(self):
        return f"Biblioteca(nombre='{self.nombre}', Libros={self.libros})"
    
    def __len__(self):
        return len(self.libros)
    
    def __contains__(self, b_libro): #  __contains__ solo puede recibir un parametro
        return b_libro in self.libros
    
    def __getitem__(self, index):
        return self.libros[index]

    def __setitem__(self, index, value): #  __setitem__ modifica un libro en la lista utilizando su indice.
        self.libros[index] = value

    def __delitem__(self, index):
        del self.libros[index]

# Crear instancias de Biblioteca
b1 = Biblioteca("Central", ["1984", "Cien años de soledad", "Don Quijote"])
b2 = Biblioteca("Barrial", ["El Principito", "La Odisea"])

# __repr__
print(b1)

# __len__
print(len(b1))

# __contains__
print("1984" in b1)

# __getitem__
print(b1[1])

# __setitem__
b1[0] = "Rayuela"
print(b1)

# __delitem__
del b1[2]
print(b1)

# Intentar crear otra biblioteca con el mismo nombre
try:
    b3 = Biblioteca("Central", ["Nuevo libro"])
except ValueError as e:
    print(e)
