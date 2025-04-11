# La abstracción consiste en ocultar la complejidad interna y mostrar solo lo necesario.
# Crear clases que definen lo que un objeto debe hacer, pero no cómo lo hace exactamente.
# Es una planilla base que otras clases deben heredar.
# Se usa el modulo abc (abstract base class) para definirla

from abc import ABC, abstractmethod
# ABC indica que una clase es abstracta
# @abdstractmethod marca un método que debe ser implementado por cualquier clase hija

# Imagina que estás construyendo un sistema de transporte. Todos los tipos de transporte tienen en común:

# Un método para arrancar.

# Un método para frenar.

# Pero cada uno lo hace diferente: un carro arranca con llave, una bicicleta con pedales, un tren con sistema eléctrico.

# Entonces:

# La clase abstracta Transporte define los métodos arrancar() y frenar(), pero no los implementa.

# Las clases Carro, Bicicleta, y Tren heredan de Transporte y tienen que implementar esos métodos a su manera.


class MetodoPago(ABC):

    @abstractmethod
    def validar_pago(self):
        pass

    @abstractmethod
    def procesar_pago(self):
        pass

class PagoTarjeta(MetodoPago):
    def validar_pago(self):
        print("Validando tarjeta...")
    
    def procesar_pago(self):
        print("Procesando pago con tarjeta.")

class PagoEfectivo(MetodoPago):
    def validar_pago(self):
        print("Validando billetes...")
    
    def procesar_pago(self):
        print("Pago en efectivo procesado.")

p1 = PagoTarjeta()
p1.validar_pago()
p1.procesar_pago()

p2 = PagoEfectivo()
p2.validar_pago()
p2.procesar_pago()
