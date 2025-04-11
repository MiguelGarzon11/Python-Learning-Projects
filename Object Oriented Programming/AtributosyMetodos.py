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
            print(f"{cantidad} billete(s) de $ {billete:,.0f}".replace(".",","))

        print(f"Saldo restante en el cajero: $ {self.saldo:,.0f}".replace(".",","))

    def depositar(self, monto):
        if monto < 5000:
            print("\nError: Deposite más de 5.000\n")
        else:
            self.saldo = self.saldo + monto
            print(f"\n¡ Se deposito exitosamente ${monto:,.0f}!".replace(".",","))
            return self.saldo
        
    def mostrar_saldo(self):
        if self.saldo == 0 or self.saldo <= 5000:
            print("\nEl cajero no tiene suficiente dinero.")
        else:
            print(f"El saldo del cajero es de: $ {self.saldo:,.0f} pesos".replace(".",","))

cajero = Cajero(200000)

while True:
    try:
        print("\nC A J E R O  A U T O M Á T I C O")
        print("  M E N Ú  P R I N C I P A L \n")
        print("1. Retirar.")
        print("2. Depositar.")
        print("3. Mostrar saldo cajero.")
        print("4. Salir.")

        opcion = int(input("\nDigite un número del (1-4)\n"))
                
        if opcion == 1:
            retiro = int(input("\nDigite una cantidad a retirar: \n"))
            cajero.retirar(retiro)

        elif opcion == 2:
            deposito = int(input("\nDigite una cantidad a depositar: \n"))
            cajero.depositar(deposito)
        
        elif opcion == 3:
            cajero.mostrar_saldo()
        elif opcion == 4:
            print("\nGracias por usar el programa, Saliendo...\n")
            break
        else:
            print("\nIngrese una opción correcta\n") 

    except ValueError:
        print("Error: Opción incorrecta")

