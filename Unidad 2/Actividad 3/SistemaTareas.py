#TANAILY ALCALA BARRAZA 21100152
#Sistema Gestor de Tareas

import json 


# Clase base Tarea 

class Tarea:
    def __init__(self, titulo, descripcion, prioridad="Baja"):
        # encapsulacion
        self._titulo = titulo
        self._descripcion = descripcion
        self._prioridad = prioridad
        self._completada = False

    @property
    def titulo(self):
        return self._titulo

    # metodo para cambiar el estado de la tarea
    def marcar_completada(self):
        self._completada = True
        print(f"La tarea '{self._titulo}' ha sido completada.")

    # metodo comportamiento base
    def mostrar_info(self):
        estado = "Completada" if self._completada else "Pendiente"
        return f"[{estado}] Título: {self._titulo} | Prioridad: {self._prioridad} | Descripción: {self._descripcion}"

    # metodo para serializar el objeto 
    def to_dict(self):
        return {
            'tipo': self.__class__.__name__, 
            'titulo': self._titulo,
            'descripcion': self._descripcion,
            'prioridad': self._prioridad,
            'completada': self._completada
        }

# Clase 2 TareaUrgente

class TareaUrgente(Tarea):
    def __init__(self, titulo, descripcion, fecha_limite):
        super().__init__(titulo, descripcion, prioridad="Alta")
        self._fecha_limite = fecha_limite

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"URGENTE: {info_base} | ¡Fecha Límite: {self._fecha_limite}!"
    
    def to_dict(self):
        data = super().to_dict()
        data['fecha_limite'] = self._fecha_limite
        return data


# Clase 3 TareaRecurrente 

class TareaRecurrente(Tarea):
    def __init__(self, titulo, descripcion, prioridad, frecuencia):
        super().__init__(titulo, descripcion, prioridad)
        self._frecuencia = frecuencia 

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"Recurrente: {info_base} | Frecuencia: {self._frecuencia}"
        
    def to_dict(self):
        data = super().to_dict()
        data['frecuencia'] = self._frecuencia
        return data
    
# GestorTareas

class GestorTareas:
    def __init__(self, archivo='tareas.json'):
        self._lista_tareas = []
        self._archivo = archivo
        self.cargar_desde_json() 

    def agregar_tarea(self, tarea):
        self._lista_tareas.append(tarea)
        print(f"Tarea '{tarea.titulo}' agregada.")

    def listar_tareas(self):
        if not self._lista_tareas:
            print("No hay tareas registradas.")
            return

        print("\n--- LISTA DE TAREAS ---")
        for i, tarea in enumerate(self._lista_tareas):
            print(f"{i+1}. {tarea.mostrar_info()}")
        print("-----------------------\n")

    def marcar_completada(self, indice):
        try:
            tarea = self._lista_tareas[indice - 1]
            tarea.marcar_completada()
        except IndexError:
            print("Índice de tarea no válido.")

    def eliminar_tarea(self, indice):
        try:
            titulo_eliminado = self._lista_tareas[indice - 1].titulo
            del self._lista_tareas[indice - 1]
            print(f"Tarea '{titulo_eliminado}' eliminada.")
        except IndexError:
            print("Índice de tarea no válido.")

    def guardar_a_json(self):
        datos_json = [tarea.to_dict() for tarea in self._lista_tareas]
        try:
            with open(self._archivo, 'w') as f:
                json.dump(datos_json, f, indent=4)
            print(f"Datos guardados correctamente en {self._archivo}.")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def cargar_desde_json(self):
        try:
            with open(self._archivo, 'r') as f:
                datos_json = json.load(f)
            
            self._lista_tareas = []

            for data in datos_json:
                tipo = data.pop('tipo')
                
                if tipo == 'Tarea':
                    tarea = Tarea(**data)
                elif tipo == 'TareaUrgente':
                   
                    tarea = TareaUrgente(data['titulo'], data['descripcion'], data['fecha_limite'])
                    tarea._completada = data['completada'] 
                elif tipo == 'TareaRecurrente':
                    tarea = TareaRecurrente(data['titulo'], data['descripcion'], data['prioridad'], data['frecuencia'])
                    tarea._completada = data['completada']
                else:
                    continue 
                
                self._lista_tareas.append(tarea)
            
            print(f"Datos cargados desde {self._archivo}.")
        except FileNotFoundError:
            print("Archivo de tareas no encontrado. Iniciando con lista vacía.")
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON. Iniciando con lista vacía.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al cargar: {e}")


# menu


def mostrar_menu():
    print("\n--- Sistema de Gestión de Tareas ---")
    print("1. Agregar nueva tarea")
    print("2. Listar todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Guardar y Salir")
    return input("Seleccione una opción: ")

def crear_tarea_desde_input():
    print("\n--- Tipo de Tarea ---")
    print("1. Tarea General")
    print("2. Tarea Urgente")
    print("3. Tarea Recurrente")
    opcion = input("Elija el tipo de tarea (1-3): ")
    
    titulo = input("Título de la tarea: ")
    descripcion = input("Descripción: ")

    if opcion == '1':
        prioridad = input("Prioridad (Baja/Media/Alta): ")
        return Tarea(titulo, descripcion, prioridad)
    elif opcion == '2':
        fecha_limite = input("Fecha Límite (DD/MM/AAAA): ")
        return TareaUrgente(titulo, descripcion, fecha_limite)
    elif opcion == '3':
        prioridad = input("Prioridad (Baja/Media/Alta): ")
        frecuencia = input("Frecuencia (diaria/semanal/mensual): ")
        return TareaRecurrente(titulo, descripcion, prioridad, frecuencia)
    else:
        print("Opción inválida.")
        return None

def main():
    gestor = GestorTareas()
    
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            nueva_tarea = crear_tarea_desde_input()
            if nueva_tarea:
                gestor.agregar_tarea(nueva_tarea)

        elif opcion == '2':
            gestor.listar_tareas()

        elif opcion == '3':
            gestor.listar_tareas()
            try:
                indice = int(input("Ingrese el número de la tarea a completar: "))
                gestor.marcar_completada(indice)
            except ValueError:
                print("Entrada no válida.")

        elif opcion == '4':
            gestor.listar_tareas()
            try:
                indice = int(input("Ingrese el número de la tarea a eliminar: "))
                gestor.eliminar_tarea(indice)
            except ValueError:
                print("Entrada no válida.")
        
        elif opcion == '5':
            gestor.guardar_a_json()
            print("¡Hasta luego!")
            break

        else:
            print("Opción no reconocida. Intente de nuevo.")

if __name__ == "__main__":
    main()



