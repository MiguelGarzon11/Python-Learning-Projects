# Encapsulación de OOP.
# Es el principio de ocultar los detalles internos de un objeto y permitir el acceso a los datos
# solo a través de metodos definidos, evitando el acceso directo a los atributos

# _atributo: Protegido (solo para uso interno, no lo modifiques directamente).
# __atributo: Privado (Python Encapsula o esconde ciertas operaciones para que no puedan ser modificadas)

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}")

    def cambiar_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Edad no valida")


p = Persona("Miguel", 17)
p.mostrar_info()
p.__edad = -5
p.cambiar_edad(18)
p.mostrar_info()

class Empleado:
    def __init__(self, nombre, edad, salario):
        self.__nombre = nombre
        if edad < 18:
            raise ValueError("\nLa edad no puede ser menor a 18.\n")
        else:
            self.__edad = edad
        if salario < 100000:
            raise ValueError("\nEl salario mensual no puede ser menor a 100.000 pesos .")
        else:
            self.__salario = salario
        
    def mostrar_informacion(self):
        print(f"El empleado {self.__nombre} de edad {self.__edad}, tiene un salario mensual de $ {self.__salario:,.0f}".replace(".",","))

    def cambiar_salario(self, n_salario):
        if n_salario < 100000 or n_salario == self.__salario:
            raise ValueError("\nEl nuevo salario es menor a $ 100.000 o puso el mismo salario.\n")
        self.__salario = n_salario
        return self.__salario

    def aumentar_salario(self, n):
        if 0 == n < 0:
            raise ValueError("Porcentaje no valido.\n")
        self.__salario = self.__salario + (self.__salario * n // 100)
        print(f"\nEL nuevo salario del empleado {self.__nombre} es de: {self.__salario:,.0f}".replace(".",","))
        return self.__salario
    

e = Empleado("Miguel", 18, 150000)
e.mostrar_informacion()

e.cambiar_salario(300000)
e.mostrar_informacion()

e.aumentar_salario(50)
e.mostrar_informacion()
