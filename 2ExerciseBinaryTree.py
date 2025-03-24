class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

raiz = Nodo(10)
raiz.izq = Nodo(5)
raiz.der = Nodo(15)
raiz.izq.izq =Nodo(3)
raiz.izq.der = Nodo(7)
raiz.der.der = Nodo(18)
raiz.der.izq = Nodo(12)

def buscar_valor(raiz, valor):
    if raiz is None:
        return False
    if raiz.valor == valor:
        return True
    
    return buscar_valor(raiz.izq, valor) or buscar_valor(raiz.der, valor)

print(buscar_valor(raiz, 7))
print(buscar_valor(raiz, 100))
    
