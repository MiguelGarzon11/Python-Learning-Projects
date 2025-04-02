# Ejercicio de Iterators.
# Registro de pedidos de restaurante.

class Pedidos:
    def __init__(self, lista):
        self.lista = lista
        self.indice = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice >= len(self.lista):
            print("No hay pedidos por procesarce")
            raise StopIteration
        pedido = self.lista[self.indice]
        self.indice += 1
        return pedido
    
lista_pedidos = ["Pizza", "Hamburguesa", "Ensalada", "Tacos"]
pedidos = Pedidos(lista_pedidos)

for pedido in pedidos:
    print("Procesando pedido:", pedido)
        