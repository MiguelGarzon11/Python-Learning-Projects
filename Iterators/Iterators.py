# Ejercicios Básicos para entender Iterators.

numeros = [10,20,30,40,50]
iterador = iter(numeros)

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

frutas = ["Manzana", "Piña", "Fresa", "Uva"]
iterador = iter(frutas)

print(next(frutas))
print(next(frutas))
print(next(frutas))
print(next(frutas))
print(next(frutas))

class Contador:     # Recursión
    def __init__(self, n):
        self.n = n

    def devolver(self, i=1):
        if i > self.n:
            return
        print(i)
        self.devolver(i + 1)

contador = Contador(7)        
contador.devolver()

class Contador1:    # Iter
    def __init__(self, n, actual=0):    # Se da un valor por defecto a actual
        self.n = n      # Limite hasta donde contara
        self.actual = actual    # Valor inicial del contador

    def __iter__(self):
        return self
    
    def __next__(self):
        # Devuelve el siguiente número en la secuencia y lo incrementa
        if self.actual >= self.n:   # Si el número actual supera al limite
            raise StopIteration     # Detiene la iteración

        valor = self.actual     # Guarda el valor actual
        self.actual += 1    # Incrementa el contador
        return valor    # Retorna el valor
    
contador = Contador1(5)     # Crea un iterador que cuenta hasta 5
for num in contador:
    print(num)


class Multiplos:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.contador >= self.n:
            raise StopIteration
        
        valor = self.m * self.contador
        self.contador += 1 
        return valor
    
multiplos = Multiplos(3, 5)
for num in multiplos:
    print(num)            
