## TANAILY ALCALA BARRAZA 21100152

class Libro:
    # Atributo de Clase (lo comparten todos los objetos Libro)
    biblioteca = "Biblioteca Central"

    # Método __init__ (es constructor para inicializar los atributos de instancia
    def __init__(self, titulo: str, autor: str, año_publicacion: int):
        # Atributos de Instancia (estos son unicos para cada objeto Libro)
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.prestado = False  

    # Método prestar (cambia el estado del libro a prestado)
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"\n✅ El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"\n⚠️ El libro '{self.titulo}' ya está prestado.")

    # Método devolver (cambia el libro a disponible)
    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"\n🔄 El libro '{self.titulo}' ha sido devuelto y está disponible.")
        else:
            print(f"\n⚠️ El libro '{self.titulo}' no estaba prestado.")

    # Método mostrar_estado (imprime la info completa )
    def mostrar_estado(self):
        estado = "Sí" if self.prestado else "No"
        print("---------------------------------")
        print(f"📖 Título: {self.titulo}")
        print(f"✍️ Autor: {self.autor}")
        print(f"🗓️ Año de Publicación: {self.año_publicacion}")
        print(f"🏛️ Ubicación: {Libro.biblioteca}")  
        print(f"➡️ Prestado: {estado}")
        print("---------------------------------")


# _______________________________________________
if __name__ == "__main__":
    print("--- Creación de Objetos ---")
    
    # instanciamos objetos
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)
    libro3 = Libro("Harry Potter", "JK Rawling", 2008)
    
    print("\n--- Mostrar Estado Inicial ---")
    libro1.mostrar_estado()
    libro2.mostrar_estado()
    
    print("\n--- Manipulación de Estado (Préstamos y Devoluciones) ---")
    
    # llamamos al metodo 
    libro1.prestar()
    libro3.prestar()
    
    # intentamos prestar libro1 de nuevo 
    libro1.prestar()
    
    # devolvemos libro3
    libro3.devolver()

    # mostramos el estado final de los 3 libros
    print("\n---  Mostrar Estado Final ---")
    libro1.mostrar_estado()
    libro2.mostrar_estado()  
    libro3.mostrar_estado()