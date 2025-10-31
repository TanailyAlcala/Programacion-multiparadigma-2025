"""
Módulo con funciones de utilidad para la gestión de tareas.
Incluye funciones para manipular la lista de tareas.
"""
# No es necesario importar Tarea aquí si solo se manipula como un objeto genérico
# y se asume que ha sido definido en otro lugar (cohesión y bajo acoplamiento).

def agregar_tarea(lista: list, tarea) -> None:
    """
    Añade una tarea a la lista principal.

    Parámetros:
        lista (list): La lista de tareas donde se agregará.
        tarea: El objeto Tarea a añadir.

    Retorna:
        None: La función modifica la lista directamente (side effect).
    """
    lista.append(tarea)

def mostrar_tareas(lista: list) -> None:
    """
    Imprime la información de todas las tareas en la lista.

    Parámetros:
        lista (list): La lista de objetos Tarea a imprimir.

    Retorna:
        None: Solo realiza la impresión en consola.
    """
    if not lista:
        print("No hay tareas pendientes.")
        return

    for tarea in lista:
        # Se asume que 'tarea' tiene el método mostrar_info()
        print(tarea.mostrar_info())