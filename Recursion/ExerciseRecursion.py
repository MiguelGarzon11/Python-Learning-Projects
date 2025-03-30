# Ejercicio de convertir un número en palabras(Sistema de pagos o cheques)
# utilizando Recursion

def convertir_numero(n):
    l20 = [
        "Cero","Uno","Dos","Tres","Cuatro","Cinco",
        "Seis","Siete","Ocho","Nueve","Diez","Once",
        "Doce","Trece","Catorce","Quince","Dieciseis",
        "Diecisiete","Dieciocho","Diecinueve","Veinte",
    ] 
    l30 = [
        "Veintiuno","Veintidos","Veintitres","Veinticuatro",
        "Veinticinco","Veintiseis","Veintisiete","Veintiocho",
        "Veintinueve"
    ]
    decenas = [
        "Treinta","Cuarenta","Cincuenta","Sesenta","Setenta",
        "Ochenta", "Noventa"
    ]
    centenas = [
        "Cien","Doscientos","Trescientos","Cuatrocientos",
        "Quinientos","Seiscientos","Setecientos","Ochocientos","Novecientos"
    ]
    if 0 <= n < 21:
        return l20[n]
    
    elif 21 <= n < 30:
        return l30[n - 21]
    
    elif n % 10 == 0 and n < 100:
        return decenas[n // 10 - 3]
    
    elif n > 30 and n < 100 and n % 10 != 0:
        decena = decenas[n // 10 - 3]
        unidad = convertir_numero(n % 10)

        return f"{decena} y {unidad}"
    
    elif n % 100 == 0:
        return centenas[n // 100 - 1]
    
    elif n < 1000:
        centena = "Ciento" if n < 200 else centenas[n // 100 - 1]
        resto = convertir_numero(n % 100)
        return f"{centena} {resto}"
    
    elif n == 1000:
        return "Mil"
    
    elif n < 1000000:
        miles = "Mil" if n // 1000 == 1 else convertir_numero(n // 1000) + " mil"
        resto = n % 1000
        return miles if resto == 0 else f"{miles} {convertir_numero(resto)}"

    elif n == 1000000:
        return "Un millón"
    
    elif n < 1000000000:
        millones = "Un millón" if n // 1000000 == 1 else convertir_numero(n // 1000000) + " millones"
        resto = n % 1000000
        return millones if resto == 0 else f"{millones} {convertir_numero(resto)}"
    
print(convertir_numero(20))
print(convertir_numero(245))
print(convertir_numero(139))
print(convertir_numero(999999999))
print(convertir_numero(34589793))
print(convertir_numero(485768379))