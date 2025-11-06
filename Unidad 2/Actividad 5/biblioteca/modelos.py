# TANAILY ALCALA BARRAZA 21100152

import uuid

class Libro:
    """
    esta clase representa el libro dentro de la biblioteca.

    """
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.estado = 'disponible'
        self.id = str(uuid.uuid4())[:8]

    def __str__(self):
        """regresa el objeto libro"""
        return f"[{self.id}] '{self.titulo}' por {self.autor} ({self.año}) - Estado: {self.estado.upper()}"

    def to_dict(self):
        
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'año': self.año,
            'estado': self.estado
        }

class Usuario:
    """
    usuario de la biblioteca.

    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.id = str(uuid.uuid4())[:8]
        self.libros_prestados = []

    def __str__(self):
        """regresa el objeto usuarip"""

        return f"[{self.id}] Usuario: {self.nombre} | Libros prestados: {len(self.libros_prestados)}"

    def to_dict(self):
        
        return {
            'id': self.id,
            'nombre': self.nombre,
            'libros_prestados': self.libros_prestados
        }