# Ejercicio 3: Menú de operaciones
# Tanaily Alcala Barraza 21100152

# Programa que muestra un menú de operaciones básicas

while True:
    # se muestra el menú
    print("\n--- MENÚ ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Salir")

    # se pide la opción al usuario
    opcion = input("Elige una opción: ")

    # se verifica la opción elegida
    if opcion == "1":
        # dos números para sumar
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(f"La suma de {num1} + {num2} es: {num1 + num2}")

    elif opcion == "2":
        # dos números para restar
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(f"La resta de {num1} - {num2} es: {num1 - num2}")

    elif opcion == "3":
        # salir del programa
        print("Saliendo del programa...")
        break

    else:
        # manejo de opción inválida
        print("Opción no válida, intenta de nuevo.")

