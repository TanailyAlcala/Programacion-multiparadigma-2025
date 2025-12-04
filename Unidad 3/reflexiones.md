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