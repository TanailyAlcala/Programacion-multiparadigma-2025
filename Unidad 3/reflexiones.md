## TANAILY ALCALA BARRAZA 21100152 

## PARTE 1: Identificación y análisis de Funciones 

Analiza las siguientes funciones. Para cada una indica:

* Si es pura o impura
* Por qué (identifica el problema específico si es impura)
* Cómo la convertirías a pura (si aplica)

| Función | ¿Pura o impura? | Por qué | Conversión a pura |
| :--- | :--- | :--- | :--- |
| **Función A: `calcular_promedio`** | **Pura** | Su resultado depende solo del argumento de entrada (`numeros`) y no modifica la lista original ni las variables. Es determinista. | Ya es pura. |
| **Función B: `siguiente_id`** | **Impura** | **Problema:** Depende de y modifica el estado externo (`global contador`).No es determinista | Se extrae el estado como parametro y retorna el nuevo estado.<br>```python<br>def siguiente_id_puro(contador):<br>    return f"ID-{contador + 1}", contador + 1<br>``` |
| **Función C: `agregar_fecha`** | **Impura** | **Problema 1:** Modifica el argumento mutable `registro` *in-place*. **Problema 2:** No es determinista porque el valor de `datetime.now()` cambia con cada llamada. | Retornar una nueva estructura y aislar la fecha.<br>```python<br>def agregar_fecha_puro(registro, fecha):<br>    return {**registro, 'fecha': fecha}<br>``` |
| **Función D: `filtrar_positivos`** | **Pura** | Utiliza una comprensión de lista que crea una nueva lista como resultado, sin modificar el argumento original (`numeros`). Es completamente determinista. | Ya es pura. |
| **Función E: `mezclar_lista`** | **Impura** | **Problema 1:** Modifica el argumento mutable `lista` *in-place* mediante `random.shuffle()`. **Problema 2:** No es **determinista** porque depende de un generador de números aleatorios. | Retornar una nueva estructura (copia) antes de modificarla.<br>```python<br>def mezclar_lista_puro(lista):<br>    import random<br>    nueva_lista = lista.copy() # Copia inmutable<br>    random.shuffle(nueva_lista)<br>    return nueva_lista<br>``` |



## PARTE 4: Reflexión Final

### 1. ¿Qué significa que una función sea "pura"?

Una función es **pura** si el resultado de la funcion depende unicamente de los argumentos que se le pasan. Por ejemplo, si la llamas 100 veces con los mismos argumentos, siempre obtendrás exactamente el mismo resultado.
#### Ejemplo de la vida cotidiana
Un ejemplo que podemos ver en el dia a dia podriamos verlo en una tostadora, si siempre usas el mismo tipo de pan y el mismo nivel "3", la tostadora siempre producirá el mismo nivel de tostado, sin importar el día, el mes, o si acabas de hacer otro pan tostado.

### 2. En la Parte 3, ¿por qué `crear_transformador` retorna una función en lugar de aplicar directamente la transformación? ¿Qué ventaja ofrece este diseño?

El retorno de una función permite separar la configuración de la ejecución. Esto significa que podemos definir la lógica operativa una vez y reutilizarla en diversos contextos. La ventaja clave es su utilidad para la composición funcional, donde se conectan fácilmente operaciones atómicas para formar procesos de datos complejos y ordenados.

### 3. ¿Qué dificultades encontraste al convertir el código imperativo a funcional en la Parte 2?

En lo personal estoy acostumbrada a realizar mis códigos de otra manera, mas desordenada aunque intento arreglar eso, implementar estos nuevos conceptos para realizarlos de una manera optima si resulto un pequeño reto debido a que tuve que corregir varias cosas que hacia por inercia, como lo es acoplar todo en ciclos.  

### 4. Si tuvieras que explicar la diferencia entre programación imperativa y funcional a alguien que no programa, ¿qué analogía usarías?

Creo que la analogía de la preparación de una ensalada de frutas aplica bien. La programacion imperativa es como un chef de cocina solitario que es el cómo, quien utiliza un unico tazon mutable (el estado) y realiza todos los pasos (cortar, mezclar, agregar azúcar) modificando ese tazon directamente; la logica se centra en la secuencia precisa de acciones y si el chef comete un error, el estado del tazón queda alterado permanentemente. Es como una cadena de producción especializada, el qué, donde los ingredientes pasan por una línea de ensamblaje de funciones puras (filtro de madurez, cortar en cubitos, agregar crema), y cada función recibe una caja de frutas y devuelve una nueva caja con la transformación aplicada, sin modificar la caja de entrada (inmutabilidad), asegurando que el proceso sea predecible, componible y enfocado únicamente en la definición de las transformaciones necesarias.