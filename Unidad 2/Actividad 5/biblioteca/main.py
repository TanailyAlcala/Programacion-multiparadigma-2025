# TANAILY ALCALA BARRAZA 21100152

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modelos import Libro, Usuario
from operaciones import Biblioteca
from persistencia import cargar_datos

def mostrar_menu():
    """menu principal de opciones """
    print("\n--- Sistema de Gestión de Biblioteca ---")
    print("1. Agregar libro")
    print("2. Agregar usuario")
    print("3. Mostrar libros disponibles")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Mostrar todos los usuarios")
    print("7. Guardar y salir")
    return input("Seleccione una opción: ")

def obtener_datos_libro():
    """ se piden los datos para crear un nuevo libro """
    print("\n--- Nuevo Libro ---")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    try:
        año = int(input("Año de publicacion: "))
        return Libro(titulo, autor, año)
    except ValueError:
        print("Error: El año debe ser un numero entero.")
        return None

def obtener_datos_usuario():
    """ se piden los datos para crear un nuevo usuario."""
    print("\n--- Nuevo Usuario ---")
    nombre = input("Nombre del usuario: ")
    return Usuario(nombre)

def mostrar_usuarios(biblioteca):
    """ muestra la lista completa de usuarios."""
    if not biblioteca.usuarios:
        print("\n--- No hay usuarios registrados. ---")
        return
    print("\n--- Lista de usuarios ---")
    for usuario in biblioteca.usuarios:
        print(f" * {usuario}")
    print("-------------------------")

def main():
    """funcion principal"""
    
    libros, usuarios = cargar_datos()
    biblioteca = Biblioteca(libros, usuarios)

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            libro = obtener_datos_libro()
            if libro:
                biblioteca.agregar_libro(libro)

        elif opcion == '2':
            usuario = obtener_datos_usuario()
            biblioteca.agregar_usuario(usuario)

        elif opcion == '3':
            biblioteca.mostrar_libros_disponibles()

        elif opcion == '4':
            biblioteca.mostrar_libros_disponibles()
            mostrar_usuarios(biblioteca)
            libro_id = input("Ingrese el id del libro a prestar: ")
            usuario_id = input("Ingrese el id del usuario: ")
            biblioteca.prestar_libro(libro_id, usuario_id)

        elif opcion == '5':
            mostrar_usuarios(biblioteca)
            libro_id = input("Ingrese el id del libro a devolver: ")
            usuario_id = input("Ingrese el id del usuario que devuelve: ")
            biblioteca.devolver_libro(libro_id, usuario_id)

        elif opcion == '6':
            mostrar_usuarios(biblioteca)
            
        elif opcion == '7':
            biblioteca.guardar_y_salir()
            break

        else:
            print("Opción no valida. Intente de nuevo.")

if __name__ == "__main__":
    main()