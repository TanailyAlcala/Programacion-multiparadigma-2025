# Ejercicio 1: Cálculo de áreas
# Tanaily Alcala Barraza 21100152

import math  # Importamos librería math para usar el valor de pi

while True:  # Bucle para que el usuario elija la opción que desea
    print("\n--- Cálculo de áreas ---")
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Círculo")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")  # El usuario elige una opción

    if opcion == "1":
        # Área del triángulo = (base * altura) / 2
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")

    elif opcion == "2":
        # Área del cuadrado = lado * lado
        lado = float(input("Ingresa el lado del cuadrado: "))
        area = lado * lado
        print(f"El área del cuadrado es: {area}")

    elif opcion == "3":
        # Área del círculo = pi * radio^2
        radio = float(input("Ingresa el radio del círculo: "))
        area = math.pi * (radio ** 2)
        print(f"El área del círculo es: {area}")

    elif opcion == "4":
        # Salimos y terminamos el programa
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")

