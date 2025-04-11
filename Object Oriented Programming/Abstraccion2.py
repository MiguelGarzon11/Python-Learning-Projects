# Sistema de alquiler de Vehículos.
# Simular un sistema que permite alquilar distintos tipos de vehículos. Cada tipo de vehículo tiene su propia 
# lógica para calcular el precio de alquiler.

from abc import ABC, abstractmethod

class VehiculoAlquilable(ABC):
    
    @abstractmethod
    def __init__(self, marca, modelo, color):
        pass

    @abstractmethod
    def calcular_precio(self, dias):
        pass

    @abstractmethod
    def mostrar_detalles(self):
        pass

class Automovil(VehiculoAlquilable):
    def __init__(self, marca, modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color

    def calcular_precio(self, dias):
        if dias <= 0:
            raise ValueError("No se puede alquilar un automovil menos de 1 día.")
        precio = dias * 100000
        return f"El precio para alquilar un automovil es de: $ {precio:,.0f}".replace(".",",")
    
    def mostrar_detalles(self):
        return f"Automovil marca: {self._marca}.\nModelo: {self._modelo}.\nColor: {self._color}."

class Bicicleta(VehiculoAlquilable):
    def __init__(self, marca, modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color

    def calcular_precio(self, dias):
        if dias <= 0:
            raise ValueError("No se puede alquilar una Bicicleta menos de 1 día.")
        precio = dias * 15000
        return f"El precio para alquilar una Bicicleta es de: $ {precio:,.0f}".replace(".",",")
    
    def mostrar_detalles(self):
        return f"Bicicleta marca: {self._marca}.\nModelo: {self._modelo}.\nColor: {self._color}."

class Motocicleta(VehiculoAlquilable):
    def __init__(self, marca, modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color

    def calcular_precio(self, dias):
        if dias <= 0:      
            raise ValueError("No se puede alquilar una Motocicleta menos de 1 día.")
        precio = dias * 50000
        return f"El precio para alquilar una Motocicleta es de: $ {precio:,.0f}".replace(".",",")
    
    def mostrar_detalles(self):
        return f"Motocicleta marca: {self._marca}.\nModelo: {self._modelo}.\nColor: {self._color}."


if __name__ == "__main__":
    # Crear instancias de cada vehículo
    auto = Automovil("Toyota", "Corolla", "Blanco")
    bici = Bicicleta("GW", "Urban", "Roja")
    moto = Motocicleta("Yamaha", "FZ25", "Negra")

    # Mostrar detalles
    print("=== DETALLES DE VEHÍCULOS ===")
    auto.mostrar_detalles()
    print()
    bici.mostrar_detalles()
    print()
    moto.mostrar_detalles()
    print()

    # Calcular precios de alquiler por 3 días
    print("=== PRECIOS DE ALQUILER POR 3 DÍAS ===")
    print(auto.calcular_precio(3))
    print(bici.calcular_precio(3))
    print(moto.calcular_precio(3))

    # Probar error con días inválidos
    print("\n=== PRUEBA DE VALIDACIÓN ===")
    try:
        print(auto.calcular_precio(0))
    except ValueError as e:
        print(f"Error: {e}")
