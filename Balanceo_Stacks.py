# Verificar si los paréntesis, corchetes y llaves en una expresión están bien balanceados
# utilizando pila (Stack).

def validar_parentesis(expresion):
    stack = []
    contiene_parentesis = False

    for caracter in expresion:
        if caracter == "(":
            stack.append (caracter)
            contiene_parentesis = True
        elif caracter == ")":
            contiene_parentesis = True
            if not stack:
                return False
            stack.pop()

    # Si no hay parentesis en toda la expresión, se considera valida    
    if not contiene_parentesis:
        return True
        
    return len(stack) == 0

def validar_corchetes(expresion):
    stack = []
    contiene_corchetes = False

    for caracter in expresion:
        if caracter == "[":
            stack.append(caracter)
            contiene_corchetes = True
        elif caracter == "]":
            contiene_corchetes = True
            if not stack:
                return False
            stack.pop()
    
    #Si no hay corchetes en toda la expresión, se considera valida
    if not contiene_corchetes:
        return True
    
    return len(stack) == 0

def validar_llaves(expresion):
    stack = []
    contiene_llaves = False

    for caracter in expresion:
        if caracter == "{":
            stack.append(caracter)
            contiene_llaves = True
        elif caracter == "}":
            contiene_llaves = True
            if not stack:
                return False
            stack.pop()
    
    #Si no hay llaves en toda la expresión, Se considera valida
    if not contiene_llaves:
        return True
    
    return len(stack) == 0 

# 'expresion' es le expresión de la cual se quiere verificar el balanceo de corchetes,
# llaves o parentesis.

expresion = input(
    "Digite la expresión que quiere verificar el valanceo "
    "de corchetes, llaves o parentesis:\n")

resultado_parentesis = validar_parentesis(expresion)
resultado_corchetes = validar_corchetes(expresion)
resultado_llaves = validar_llaves(expresion)

print(f"Parentesis balanceados: {resultado_parentesis}")
print(f"Corchetes balanceados: {resultado_corchetes}")
print(f"Llaves balanceadas: {resultado_llaves}")

