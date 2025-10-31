"""
Módulo que define la estructura de una Tarea.
Contiene la clase 'Tarea' y sus métodos asociados.
"""

class Tarea:
    """
    Representa una tarea con un nombre y un estado.

    Atributos:
        nombre (str): El nombre o descripción de la tarea.
        estado (str): El estado actual de la tarea ("Pendiente", "Completada").
    """
    def __init__(self, nombre, estado="Pendiente"):
        """
        Constructor de la clase Tarea.

        Parámetros:
            nombre (str): Nombre de la tarea.
            estado (str, opcional): Estado inicial de la tarea. Por default es "Pendiente".
        """
        self.nombre = nombre
        self.estado = estado

    def mostrar_info(self):
        """
        Muestra la información de la tarea en un formato legible.

        Retorna:
            str: Una cadena formateada con el nombre y el estado de la tarea.
        """
        return f"Tarea: {self.nombre} - Estado: {self.estado}"