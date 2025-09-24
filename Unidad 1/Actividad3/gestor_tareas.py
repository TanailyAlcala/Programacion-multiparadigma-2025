# Tanaily Alcalá Barraza 21100152

# Gestor de tareas personales 

# Lista para guardar las tareas, cada tarea será un diccionario con 'nombre' y 'estado'
tareas = []

def mostrar_menu():
    """Menú de opciones"""
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def agregar_tarea():
    """Permite al usuario agregar una nueva tarea"""
    tarea = input("Escribe la nueva tarea: ")
    tareas.append({"nombre": tarea, "estado": "pendiente"})
    print(f"✅ Tarea '{tarea}' agregada.")

def listar_tareas():
    """Mostrar las tareas pendientes y completadas"""
    if not tareas:
        print("No hay tareas registradas.")
    else:
        print("\n--- LISTA DE TAREAS ---")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea['nombre']} - {tarea['estado']}")

def marcar_completada():
    """Permite al usuario marcar una tarea como completada"""
    listar_tareas()
    if tareas:
        try:
            num = int(input("Número de tarea a completar: "))
            if 1 <= num <= len(tareas):
                tareas[num - 1]["estado"] = "completada"
                print(f"✅ Tarea '{tareas[num - 1]['nombre']}' marcada como completada.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Ingresa un número válido.")

def eliminar_tarea():
    """Permite eliminar una tarea de la lista"""
    listar_tareas()
    if tareas:
        try:
            num = int(input("Número de tarea a eliminar: "))
            if 1 <= num <= len(tareas):
                tarea_eliminada = tareas.pop(num - 1)
                print(f"Tarea '{tarea_eliminada['nombre']}' eliminada.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Ingresa un número válido.")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        listar_tareas()
    elif opcion == "3":
        marcar_completada()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
