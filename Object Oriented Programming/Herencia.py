#  Herencia en POO (OOP) Es la capacidad de una clase de heredar atributos y metodos de otra clase.

class Factura:
    def __init__(self, numero, cliente, monto):
        self._numero = numero
        self._cliente = cliente
        self._monto = monto

    def mostrar_factura(self):
        print(f"\nLa factura {self._numero}\nCorrespondiente al cliente {self._cliente} tiene un costo de: $ {self._monto}".replace(".",","))
    
    def aplicar_descuento(self, porcentaje):
        if 0 == porcentaje < 10:
            raise ValueError("Porcentaje de descuento invalido")
        else:
            self._monto = self._monto - (self._monto * porcentaje // 100)
        
        return self._monto 
    
class FacturaNacional(Factura):
    def __init__(self, numero, cliente, monto, nit_cliente):
        super().__init__(numero, cliente, monto)
        self._nit_clientes = nit_cliente

    def mostrar_factura(self):
        print(f"\nLa factura {self._numero}\ncorrespondiente al cliente {self._cliente} con NIT {self._nit_clientes}")
        print(f"Tiene un monto de: $ {self._monto:,.0f}".replace(".","."))

class FacturaInternacional(Factura):
    def __init__(self, numero, cliente, monto, pais_cliente):
        super().__init__(numero, cliente, monto)
        self._pais_cliente = pais_cliente

    def calcular_impuesto(self, incremento):
        self._monto = self._monto + (self._monto * incremento // 100)
        self._
    def mostrar_factura(self):
        print(f"\nLa factura {self._numero}\n")
        print(f"correspondiente al cliente {self._cliente}\nDel país registrado: {self._pais_cliente}.\n")
        print(f"Tiene un monto de: $ {self._monto:,.0f} más impuesto".replace(".","."))


factura_base = Factura(1001, "Empresa XYZ", 200000)
factura_base.mostrar_factura()
factura_base.aplicar_descuento(5)
factura_base.mostrar_factura()

factura_nal = FacturaNacional(1002, "Juan Pérez", 300000, "123.456.789-0")
factura_nal.mostrar_factura()
factura_nal.aplicar_descuento(7)
factura_nal.mostrar_factura()

factura_int = FacturaInternacional(1003, "Global Corp", 500000, "Canadá")
factura_int.mostrar_factura()
factura_int.calcular_impuesto(15)
factura_int.mostrar_factura()
