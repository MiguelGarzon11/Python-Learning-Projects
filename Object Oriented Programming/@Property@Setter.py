#   @property -> convierte un metodo en un atributo de solo lectura.
#   @setter -> cuando quieres modificar un atributo pero con reglas o validaciones, usas @setter.

# class Cuadrado:
#     def __init__(self, lado):
#         self._lado = lado

#     @property
#     def lado(self):
#         return self._lado
      
#     @lado.setter
#     def lado(self, valor):
#         if valor < 0:
#             raise ValueError("EL lado no puede ser negativo")
#         self._lado = valor
    
#     @property
#     def area(self):
#         return self._lado ** 2
    
# c = Cuadrado(6)

# print(c.lado)
# print(c.area)
# c.lado = 8
# print(c.area)
# c.lado = -2

# Ejercicio de control de salarios de empleados.

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self._nombre = nombre
        self._cargo = cargo
        if salario < 1160000:
            raise ValueError("El salario no cumple con los parametros de salario minimo establecido.\n")
        self._salario = salario

    @property
    def salario(self):
        return f"{self._salario:,.0f}".replace(".",",")
    
    @property 
    def salario_anual(self):
        n_salario = self._salario * 12
        return f"{n_salario:,.0f}".replace(".",",")
    
    @salario.setter
    def salario(self, valor):
        if valor < 1160000:
            raise ValueError("El salario no cumple con los parámetros mínimos.")
        if valor == self._salario:
            raise ValueError("El nuevo salario es igual al actual.")

        self._salario = valor
        print(f"El nuevo salario para el empleado {self._nombre} es de $ {self._salario:,.0f}".replace(".",","))
    
e = Empleado("Miguel", "Gerente", 1200000)
print(f"Información del empleado {e._nombre}.")
print("Salario:")
print(e.salario)
print("Salario anual:")
print(e.salario_anual)
e.salario = 5000000




