# Ejercicios de recursión

# Ejercicio 1

def contar_atras(n):
    if n < 0:
        return
    print(n)
    contar_atras(n-1)

# contar_atras(6)

# Ejercicio 2 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

#print(factorial(5))

# Ejercicio 4

def suma_digitos(n):
    if n < 10:
        return n 
    return (n % 10) + suma_digitos(n // 10)

#print(suma_digitos(67548))

# Ejercicio 5

def contar_letra(palabra,letra):
    if len(palabra) == 0:
        return 0
    else:
        contar_primera = 1 if palabra[0] == letra else 0

        return contar_primera + contar_letra(palabra[1:], letra) # [1:] Significa toma la lista desde el segundo elemento hasta el final

# print(contar_letra("banana", "a"))

# Ejercicio 6

def contar_elementos(lista):
    if lista == []:
        return 0
    else:
        return 1 + contar_elementos(lista[1:])
    
#print(contar_elementos([1,6,7,88,89,4,5,4,43,3]))

# Ejercicio 7

def sumar_elementos(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + sumar_elementos(lista[1:])
    
#print(sumar_elementos([1,4,5,6,8,2,4,5,6,2]))

# Ejercicio 8

def numero_grande(lista):
    if len(lista) == 1:
        return lista[0]
    
    mayor = numero_grande(lista[1:])

    if lista[0] > mayor:
        return lista[0]
    else:
        return mayor
    
#print(numero_grande([1,56,343,4,78]))

# Ejercicio 9 # Slicing texto[1:] -> Te da la cadena sin el primer caracter # texto [:-1] -> Te da la cadena sin el último caracter

def invertir_cadena(texto):
    if len(texto) == 1:
        return texto[0]
    else:
        ultima_letra = texto[-1]
        return ultima_letra + invertir_cadena(texto[:-1])
    
#print(invertir_cadena("Hola"))
#print(invertir_cadena("pollita"))

# Ejercicio 9 

def contar_numeros(numero):
    if numero < 10:
        return 1
    else: 
        numero = (numero // 10)
        return 1 + contar_numeros(numero)

#print(contar_numeros(9))
#print(contar_numeros(45678))

# Ejercicio 10

def contar_creciente(actual, limite):
    if actual > limite:
        return
    print(actual)
    contar_creciente(actual + 1, limite)

#contar_creciente(1, 7)

# Ejercicio 11

def contar_descendete(numero):
    if numero == 0:
        return
    print(numero)
    contar_descendete(numero - 1)

#contar_descendete(10)

# Ejercicio 12

def contar_vocales(texto):
    if texto == "":
        return 0
    else:
        vocales = ["a","e","i","o","u"]
        if texto[0].lower() in vocales:
            return 1 + contar_vocales(texto[1:])
        else:
            return contar_vocales(texto[1:])

#print(contar_vocales("Pollita"))

# Ejercicio 13

def dar_comida(comida, personas):
    if comida <= 0:
        print("No queda más comida.")
        return
    if personas <= 0:
        print("No hay más personas en la fila.")
        return
    n_comida = comida - min(2, comida)
    n_personas = personas - 1

    print(f"Quedan {n_comida} porciones de pizza, y {n_personas} personas en la fila.")
    return dar_comida(n_comida, n_personas)

# dar_comida(10, 20)

# Ejercicio 14

def potencia_numero(a, b):
    if a == 0:
        return 0
    if b == 0:
        return 1
    
    return a * potencia_numero(a, b - 1) 

#print(potencia_numero(5, 6))