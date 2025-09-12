# Ejercicio 2: Conversión de calificación
# Tanaily Alcala Barraza 21100152

# Programa que convierte una calificación en letra

while True:
    # se pide al usuario una calificación
    calificacion = int(input("Ingresa tu calificación (0-100): "))

    # se verifica en qué rango se encuentra la calificación
    if 90 <= calificacion <= 100:
        print("Tu calificación es: A")
    elif 80 <= calificacion <= 89:
        print("Tu calificación es: B")
    elif 70 <= calificacion <= 79:
        print("Tu calificación es: C")
    elif 60 <= calificacion <= 69:
        print("Tu calificación es: D")
    elif 0 <= calificacion < 60:
        print("Tu calificación es: F")
    else:
        print("Error: la calificación debe estar entre 0 y 100")

    # se pregunta si desea ingresar otra calificación
    continuar = input("¿Quieres convertir otra calificación? (s/n): ")
    if continuar.lower() != "s":
        print("Programa finalizado.")
        break
