# Sistema de archivos de Personas
# Crear un sistema que lea archivos con datos de personas y procese esos datos de diferentes 
# formas dependiendo del tipo de persona. 


class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = int(edad)

    def presentarse(self):
        pass
    
class Estudiante(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def presentarse(self):
        print(f"Hola, soy {self._nombre} y tengo {self._edad} años. Soy estudiante.")

class Profesor(Persona):
    
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def presentarse(self):
        print(f"Hola, soy {self._nombre}, profesor con {self._edad} años de experiencia de vida.")

personas = []

with open("personas.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    tipo, nombre, edad = linea.strip().split(",")
    if tipo == "Estudiante":
        personas.append(Estudiante(nombre, edad))
    elif tipo =="Profesor":
        personas.append(Profesor(nombre, edad))

print("\n=== Presentaciones ===\n")
for persona in personas:
    persona.presentarse()
