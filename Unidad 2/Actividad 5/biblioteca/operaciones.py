# TANAILY ALCALA BARRAZA 21100152

from modelos import Libro, Usuario
from persistencia import guardar_datos

class Biblioteca:
    """
    clase para gestionar los libros y usuarios.

    """
    def __init__(self, libros=None, usuarios=None):
        self.libros = libros if libros is not None else []
        self.usuarios = usuarios if usuarios is not None else []

    def agregar_libro(self, libro):
        """
        se agregr un objeto libro a la bibioteca

        """
        self.libros.append(libro)
        print(f"Libro agregado: {libro.titulo}")

    def agregar_usuario(self, usuario):
        """
        se agrega un objeto usuario a la bibloteca

        """
        self.usuarios.append(usuario)
        print(f"Usuario agregado: {usuario.nombre}")
    
    def buscar_libro_por_id(self, libro_id):
        """ busca un libro por id y lo regresa """
        for libro in self.libros:
            if libro.id == libro_id:
                return libro
        return None

    def buscar_usuario_por_id(self, usuario_id):
        """ busca un usuario por su id y lo regresa"""
        for usuario in self.usuarios:
            if usuario.id == usuario_id:
                return usuario
        return None

    def mostrar_libros_disponibles(self):
        """ muestra la lista de libros que estan disponibles para prestamo"""
        disponibles = [libro for libro in self.libros if libro.estado == 'disponible']
        
        if not disponibles:
            print("\n--- No hay libros disponibles. ---")
            return

        print("\n--- Libros Disponibles ---")
        for libro in disponibles:
            print(f" * {libro}")
        print("--------------------------")

    def prestar_libro(self, libro_id, usuario_id):
        """
        hace el prestamo de libro a un usuario

        """
        libro = self.buscar_libro_por_id(libro_id)
        usuario = self.buscar_usuario_por_id(usuario_id)

        if not libro:
            print(f"Error: Libro con ID {libro_id} no encontrado.")
            return

        if not usuario:
            print(f"Error: Usuario con ID {usuario_id} no encontrado.")
            return

        if libro.estado == 'prestado':
            print(f"Error: El libro '{libro.titulo}' ya esta prestado.")
            return

        # se hace el prestamo
        libro.estado = 'prestado'
        usuario.libros_prestados.append(libro.id)
        print(f"Éxito: '{libro.titulo}' prestado a {usuario.nombre}.")

    def devolver_libro(self, libro_id, usuario_id):
        """
        devolucion de un libro por el usuario

        """
        libro = self.buscar_libro_por_id(libro_id)
        usuario = self.buscar_usuario_por_id(usuario_id)

        if not libro or not usuario:
            print("Error: Libro o usuario no encontrado.")
            return

        if libro.estado == 'disponible':
            print(f"Error: El libro '{libro.titulo}' ya estaba disponible.")
            return

        if libro_id not in usuario.libros_prestados:
            print(f"Error: El libro {libro_id} no esta registrado como prestado por {usuario.nombre}.")
            return

        # se hace la devolucion
        libro.estado = 'disponible'
        usuario.libros_prestados.remove(libro_id)
        print(f"Éxito: '{libro.titulo}' devuelto por {usuario.nombre}.")

    def guardar_y_salir(self):
        """ se guardar los datos """
        guardar_datos(self.libros, self.usuarios)
        print("\n--- Programa finalizado. ---")