#  Ejercicio de Programación Orietada a Objetos. Clases y Objetos

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    
    def mostrar_informacion(self):
        print(f"El empleado {self.nombre} tiene un cargo de {self.cargo} y su salario es de $ {self.salario:,.0f}".replace(".",","))

    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * (porcentaje / 100)
        print(f"El nuevo salario de {self.nombre} es de: $ {self.salario:,.0f}".replace(".", ","))

empleado1 = Empleado("Miguel", "Administrador", 5000)
empleado2 = Empleado("Camila", "Gerente", 10000)
empleado3 = Empleado("Oliver", "Contratista", 2000)

empleados = [empleado1, empleado2, empleado3]

for empleado in empleados:
    empleado.mostrar_informacion()

empleado1.aumentar_salario(30)
