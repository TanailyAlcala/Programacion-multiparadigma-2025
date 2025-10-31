# Gestor de Tareas Simples

### Propósito del Programa
Este es un ejemplo simple de un sistema modular en Python diseñado para **gestionar una lista de tareas**. Su objetivo principal es demostrar la aplicación de los principios de **modularidad** y la **documentación** usando docstrings, como parte del desarrollo de código profesional.

### Estructura y Módulos
[cite_start]El proyecto está organizado en la carpeta `gestor_tareas_proyecto/` para facilitar la lectura y el mantenimiento[cite: 14].

* **`main.py`**: Es el archivo principal que se ejecuta. [cite_start]Controla el **flujo del programa**, instancia las clases y llama a las funciones de los módulos.
* **`modulos/modelo_tarea.py`**: Contiene la **clase `Tarea`** para definir la estructura de los datos (nombre, estado). [cite_start]Su responsabilidad es clara.
* **`modulos/utilidades.py`**: Contiene funciones **auxiliares** como `agregar_tarea` y `mostrar_tareas`, que manipulan los objetos de la clase `Tarea`.
* **`docs/manual_usuario.md`**: Este manual de usuario que describe el proyecto.

### Cómo Ejecutar el Proyecto
Asegúrate de tener Python instalado.

1.  Abre una terminal o símbolo del sistema en la carpeta principal del proyecto (`gestor_tareas_proyecto/`).
2.  Ejecuta el programa principal con el siguiente comando:
    ```bash
    python main.py
    ```
3.  La salida esperada será la impresión en consola de las tareas definidas en `main.py`.