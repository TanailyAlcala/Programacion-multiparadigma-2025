# TANAILY ALCALA BARRAZA 21100152

import json
import os

from modelos import Libro, Usuario

def guardar_datos(libros, usuarios, archivo_libros='libros.json', archivo_usuarios='usuarios.json'):
    """
    guarda las listas de libros y usuarios en json separados

    """
    try:
        # 1. guarda libros
        datos_libros = [libro.to_dict() for libro in libros]
        with open(archivo_libros, 'w', encoding='utf-8') as f:
            json.dump(datos_libros, f, indent=4, ensure_ascii=False)

        # 2. guarda usuarios
        datos_usuarios = [usuario.to_dict() for usuario in usuarios]
        with open(archivo_usuarios, 'w', encoding='utf-8') as f:
            json.dump(datos_usuarios, f, indent=4, ensure_ascii=False)

        print("Datos guardados correctamente")
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")

def cargar_datos(archivo_libros='libros.json', archivo_usuarios='usuarios.json'):
    """
    carga los datos de libros y usuarios desde el json

    """
    libros = []
    usuarios = []

    # 1. cargar libros
    if os.path.exists(archivo_libros):
        try:
            with open(archivo_libros, 'r', encoding='utf-8') as f:
                datos_libros = json.load(f)
                for data in datos_libros:
                    libro = Libro(data['titulo'], data['autor'], data['año'])
                    libro.id = data['id']
                    libro.estado = data['estado']
                    libros.append(libro)
            print(f"{len(libros)} libros cargados.")
        except (IOError, json.JSONDecodeError):
            print("Archivo de libros dañado o vacio. Iniciando lista vacia.")
    else:
        print("Archivo de libros no encontrado. Iniciando lista vacia.")
    
    # 2. cargar usuarios
    if os.path.exists(archivo_usuarios):
        try:
            with open(archivo_usuarios, 'r', encoding='utf-8') as f:
                datos_usuarios = json.load(f)
                for data in datos_usuarios:
                    usuario = Usuario(data['nombre'])
                    usuario.id = data['id']
                    usuario.libros_prestados = data['libros_prestados']
                    usuarios.append(usuario)
            print(f"{len(usuarios)} usuarios cargados.")
        except (IOError, json.JSONDecodeError):
            print("Archivo de usuarios dañado o vacio. Iniciando lista vacia.")
    else:
        print("Archivo de usuarios no encontrado. Iniciando lista vacia.")

    return libros, usuarios