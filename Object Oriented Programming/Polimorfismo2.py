# Polimorfismo en POO: múltiples clases con el mismo método pero comportamiento diferente.

class Transporte:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        print(f"El transporte {self.marca} {self.modelo} se está moviendo.")

class Bicicleta(Transporte):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def mover(self):
        print(f"La bicicleta {self.tipo} {self.marca} modelo {self.modelo} avanza pedaleando.")

class Automovil(Transporte):
    def __init__(self, marca, modelo, combustible):
        super().__init__(marca, modelo)
        self.combustible = combustible

    def mover(self):
        print(f"El automóvil {self.marca} {self.modelo} se mueve usando {self.combustible}.")

class Avion(Transporte):
    def __init__(self, marca, modelo, aerolinea):
        super().__init__(marca, modelo)
        self.aerolinea = aerolinea

    def mover(self):
        print(f"El avión {self.marca} {self.modelo} de {self.aerolinea} está despegando.")

# Crear instancias de cada transporte
bici = Bicicleta("GW", "Xtreme", "montaña")
auto = Automovil("Toyota", "Corolla", "gasolina")
avion = Avion("Boeing", "737", "Avianca")

# Lista de transportes
transportes = [bici, auto, avion]

# Usamos polimorfismo: todos tienen el mismo método mover()
for t in transportes:
    t.mover()

print("\nMoviendo cada transporte por separado:")
bici.mover()
auto.mover()
avion.mover()