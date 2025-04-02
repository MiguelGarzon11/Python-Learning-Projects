# Ejercicios de Iterators.
# Ejercicio de Cajero Automático

class Cajero:
    def __init__(self, dinero, billete):
        self.dinero = dinero
        self.billete = billete
        self.restante = self.dinero
        self.valores_permitidos = [5000, 10000, 20000, 50000, 100000]

        if self.billete not in self.valores_permitidos:
                    raise ValueError("Billete no encontrado")
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.restante < self.billete:
             raise StopIteration
        
        self.restante -= self.billete
        return self.billete
    
cajero = Cajero(300000, 100000)

for i,billete in enumerate(cajero, start=1):
      print(f"{i}. Entregando billete de: ${billete}")
        