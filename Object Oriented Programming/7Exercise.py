# Dunder Methods Ejemplo practico 


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

persona = Persona("Miguel", 18)
print(persona) 


