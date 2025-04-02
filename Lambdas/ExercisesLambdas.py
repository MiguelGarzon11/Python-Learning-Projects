# Ejercicios basicos para entender lambdas

# Elevar número al cuadrado.
numero_cuadrado = lambda n: n * n
print(f"El número cuadrado de 5 es: {numero_cuadrado(5)}")

# Verificar si un número es Par o Impar.
es_par = lambda n: f"{n} Es un número par" if n % 2 == 0 else f"{n} Es un número impar"
print(es_par(5))
print(es_par(6))
print(es_par(8))
print(es_par(1))

# Obtener la primera letra de una palabra.
primera_letra = lambda palabra: f"La primera letra de {palabra} es la {palabra[0]}" 
print(primera_letra("Pollita"))

# Convertir temperaturas con map().
celcius = [0,10,20,30,40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celcius))
print(f"Temperaturas en Fahrenheit: {fahrenheit}")

# Filtrar números impares con filter().
numeros = [1,2,3,4,5,6,7,8,9,0]
impares = list(filter(lambda x: x % 2 != 0, numeros))

print(f"Números impares: {impares}")
