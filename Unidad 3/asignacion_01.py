# TANAILY ALCALA BARRAZA 21100152 

#PARTE 3: Implementación Práctica 
from functools import reduce

def crear_transformador(funcion):
    """
    esto genera una funcion que aplica funcion a cada elemento de la lista y nos da el resultado
    """
    def transformador(lista):
        # esta es alternativa a map: list comprehension
        return [funcion(elem) for elem in lista]
    return transformador


def crear_filtro(predicado):
    """
    esto creaa una funcion que conserva solo los elementos que cumplan el predicado
    """
    def filtro(lista):
        # se hace reemplazo de filter por list comprehension
        return [elem for elem in lista if predicado(elem)]
    return filtro


def crear_reductor(funcion, valor_inicial):
    """
    Ddevuelve una funcion que minimiza la lista a partir de un valor inicial
    """
    def reductor(lista):
        # usamos la misma funcion
        return reduce(funcion, lista, valor_inicial)
    return reductor


def componer(*funciones):
    """
    se reciben varias funciones y devuelve una nueva funcion que va a ejecutarlas en cadena
    """
    def pipeline(entrada):
        resultado = entrada
        for paso in funciones:
            resultado = paso(resultado)
        return resultado
    return pipeline


# pruebas
if __name__ == "__main__":
    numeros = [1, -2, 3, -4, 5, -6, 7, 8, -9, 10]
    print("Datos:", numeros)

    pipeline = componer(
        crear_filtro(lambda x: x > 0),
        crear_transformador(lambda x: x * x),
        crear_reductor(lambda a, b: a + b, 0)
    )

    resultado = pipeline(numeros)
    print("Resultado:", resultado)

    esperado = 248
    print("Verificacion:",
          "Correcto" if resultado == esperado else f"Incorrecto, esperaba {esperado}")
