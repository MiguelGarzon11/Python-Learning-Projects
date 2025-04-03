# Ejercicio de Atributos y Metodos.

class Cajero:
    def __init__(self, saldo):
        self.saldo = saldo
        self.billetes = [5000,10000,20000,50000,100000]

    def retirar(self, monto):
        contador = {} 
        if monto > self.saldo:
            print("No hay suficiente dinero en el cajero")
            return
        
        self.billetes.sort(reverse=True)

        for billete in self.billetes:
            if billete > monto:
                return billete + 1
            elif billete < monto:
                monto -= billete
                contador.append("Número Billetes:", {billete})
                return 
            print(f"{contador}. billete de $ {billete:,.0f}".replace(".", ","))
            