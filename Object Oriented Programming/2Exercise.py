# Ejercicio de Atributos y Metodos.

class Cajero:
    def __init__(self, saldo):
        self.saldo = saldo
        self.billetes = [100000, 50000, 20000, 10000, 5000]

    def retirar(self, monto):
        print(f"Se esta retirando: $ {monto:,.0f}".replace(".", ","))

        if monto > self.saldo:
            print("No hay suficiente dinero en el cajero")
            return
        
        contador = {} 
        monto_original = monto

        for billete in self.billetes:
            cantidad_billetes = monto // billete
            if cantidad_billetes > 0:
                contador[billete] = cantidad_billetes
                monto -= cantidad_billetes * billete

        if monto > 0:
            print("El cajero no puede entregar el monto exacto con los billetes disponibles.")
            return
        
        self.saldo -= monto_original

        print("Entregando:")
        for billete, cantidad in contador.items():
            print(f"{cantidad} billete(s) de $ {billete:,.0f}".replace(".", ","))

        print(f"Saldo restante en el cajero: $ {self.saldo:,.0f}".replace(".", ","))

cajero = Cajero(200000)
cajero.retirar(155000)
cajero.retirar(10000)
cajero.retirar(85000)

            
            