from modulos.modelos_tareas import Tarea
from modulos.utilidades import agregar_tarea, mostrar_tareas

def main():
    """
    Función principal para ejecutar el Gestor de Tareas Simples.
    Controla el flujo del programa.
    """
    lista_tareas = []

    # Uso de la lógica de los módulos
    tarea1 = Tarea("Comprar leche", "Pendiente")
    tarea2 = Tarea("Hacer ejercicio", "Completada")

    agregar_tarea(lista_tareas, tarea1)
    agregar_tarea(lista_tareas, tarea2)

    print("--- Listado de Tareas ---")
    mostrar_tareas(lista_tareas)

if __name__ == "__main__":
    main()