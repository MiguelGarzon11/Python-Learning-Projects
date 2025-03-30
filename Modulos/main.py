# Ejercicio básico para entender modulos

import modulos

# print(modulos.saludar("Miguel"))
# print(f"El valor de PI es {modulos.PI}")


while True:
    print("MENÚ PRINCIPAL DE OPERACIONES\n")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    try:
        opcion = int(input("\nDigite un número del (1-5):\n"))

        if opcion in [1,2,3,4]:
            num1 = int(input("Digite su primer número\n"))
            num2 = int(input("Digite su segundo número\n"))
        
            if opcion == 1:
                print(f"La suma es: {modulos.suma(num1, num2)}\n")
            elif opcion == 2:
                print(f"La resta es: {modulos.resta(num1, num2)}\n")
            elif opcion == 3:
                print(f"La multiplicación es: {modulos.multiplicacion(num1, num2)}\n")
            elif opcion == 4:
                print(f"La división es: {modulos.division(num1, num2)}\n")

        elif opcion == 5:
            print("Saiendo del programa...\n")
            break
        else:
            print("Error: opción incorrecta")

    except ValueError:
        print("\nERROR: Ingrese valores validos\n")