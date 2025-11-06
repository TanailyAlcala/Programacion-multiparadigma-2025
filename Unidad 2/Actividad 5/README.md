 # TANAILY ALCALA BARRAZA 21100152

# Actividad 5: **Sistema de Biblioteca con encapsulación y persistencia**

En esta actividad se usuaron las clases `Libro`, `Usuario` y `Biblioteca`, aplicando principios de **Programación Orientada a Objetos (POO)** enfocandonos en **encapsulación**, **abstracción** y **métodos especiales**. Además, la **persistencia** de datos mediante archivos **JSON** para conservar el estado entre ejecuciones.

---

## 1. Diseño de la clase **Libro**

La clase `Libro` representa como tal los objetos Libro que serán gestionados por la biblioteca.

### Encapsulación aplicada

| Atributo | Modificador                           | Justificación                                                                                        |
| -------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `titulo` | **Publico**                           | Identificador principal del libro.
| `autor`  | **Publico**                           | Acompaña a `titulo` como parte descriptiva      |
| `año`    | **Publico**                           | Dato informativo                                |
| `estado` | **Publico**                           | Alterna entre `disponible` y `prestado`; se modifica **solo** a través de `Biblioteca`. |
| `id`     | **Publico (solo lectura)** | Se genera automaticamente con `uuid4` (8 caracteres) y **no debe** cambiarse manualmente.            |

### Abstracción y métodos especiales

* **Generación de identificador**: en el constructor, `id = str(uuid.uuid4())[:8]` simplifica el manejo y evita colisiones.
* **`__str__`**: permite imprimir un libro en un formato amigable, por ejemplo:

  ```
  [A1B2C3D4] 'El resplandor' por Sthphen King (1995) - Estado: DISPONIBLE
  ```
* **`to_dict()`**: abstrae la serializacion del objeto a un diccionario listo para guardar en JSON.

---

## 2. Diseño de la clase **Usuario**

La clase `Usuario` representa a la persona que presta y devuelve libros.

### Encapsulación aplicada

| Atributo           | Modificador                                   | Justificación                                                                                      |
| ------------------ | --------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `nombre`           | **Publico**                                   | Identidad del usuario.      |
| `id`               | **Publico (solo lectura)**         | Generado con `uuid4` (8 caracteres) para referencia interna.                                       |
| `libros_prestados` | **Publico (lista controlada por Biblioteca)** | Se **modifica únicamente** mediante `prestar_libro` y `devolver_libro`, garantizando consistencia. |

### Métodos especiales

* **`__str__`**: formato legible con conteo de libros prestados.
* **`to_dict()`**: preparación para persistencia en JSON.

---

## 3. Diseño de la clase **Biblioteca** 

`Biblioteca` es la que gestiona las colecciones de `Libro` y `Usuario`, centralizando reglas y validaciones.

### Encapsulación aplicada

* `self.libros` y `self.usuarios` se administran **exclusivamente** por métodos de `Biblioteca`, evitando modificaciones externas.

### Métodos clave

* `agregar_libro(libro)`: añade un `Libro` a la colección.
* `agregar_usuario(usuario)`: registra un `Usuario`.
* `mostrar_libros_disponibles()`: lista los libros cuyo `estado == 'disponible'`.
* `buscar_libro_por_id(id)` / `buscar_usuario_por_id(id)`: utilitarios para localizar entidades.
* `prestar_libro(libro_id, usuario_id)`: reglas del préstamo:

  * Valida existencia de libro y usuario.
  * Evita prestar un libro ya `prestado`.
  * Cambia `estado → 'prestado'` y agrega el `id` del libro a `usuario.libros_prestados`.
* `devolver_libro(libro_id, usuario_id)`: reglas de devolución:

  * Verifica que el libro esté `prestado` al usuario.
  * Cambia `estado → 'disponible'` y retira el `id` de `libros_prestados`.
* `guardar_y_salir()`: delega en `persistencia.guardar_datos` para escribir las colecciones en JSON.

---

## 4. Persistencia con **JSON**

El modulo `persistencia.py` abstrae lectura y escritura de datos en archivos `libros.json` y `usuarios.json`.

### Funciones

* `guardar_datos(libros, usuarios, archivo_libros='libros.json', archivo_usuarios='usuarios.json')`

  * Serializa las listas usando `to_dict()` y guarda con `json.dump()` (UTF‑8, `indent=4`).
  * Maneja errores de E/S con mensajes descriptivos.

* `cargar_datos(archivo_libros='libros.json', archivo_usuarios='usuarios.json')`

  * Crea instancias de `Libro` y `Usuario` a partir del contenido JSON.
  * Recupera `id`, `estado` y `libros_prestados` para mantener el estado entre ejecuciones.
  * Tolera archivos vacíos/dañados iniciando listas vacías.

---

## 5. Prueba de funcionamiento
Este es el menu principal con el que estaremos trabajando, el cual proporciona todas las acciones que puede realizar nuestro programa. 
![Funcion](img/1.png)


Al seleccionar la opción 1 podremos agregar un nuevo libro, para ello se nos solicitará el título, autor y el año de publicación del libro. 
![Funcion](img/2.png) 


Con la opción 2, podremos agregar un usuario. Aquí solo se nos pedirá el nombre del usuario que queremos agregar. 
![Funcion](img/3.png)

Al seleccionar la opción 3 veremos la lista de libros disponibles, en donde podemos ver el id, el nombre del libro, el autor, el año y el estado del libro. 
![Funcion](img/4.png) 

Con la opción 4, podemos realizar la opción de prestar un libro. 
Primero se nos muestra la lista de libros y los usuarios. 
Después nos pide ingresar el id del libro a prestar y el id del usuario que lo tomara. 
![Funcion](img/5.png) 

Al seleccionar la opción 5 podemos realizar la opción de devolver el libro, aquí se nos pide nuevamente el id del libro prestado y el id del usuario al cual se le prestó. 
![Funcion](img/6.png) 


La opción 6 nos muestra la lista de los usuarios que han sido guardados con sus respectivos datos.  
![Funcion](img/7.png)

Por último la opción 7 nos permitirá guardar los datos y salir del programa. 
![Funcion](img/8.png)
