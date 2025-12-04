# TANAILY ALCALA ARRAZA 2110152 

from typing import List, Dict, Tuple


# PARTE 2: Conversión de Paradigmas


def filtrar_por_monto_minimo(monto_minimo: float, venta: Dict) -> bool:
    """Funcion pura - filtro: retorna true si la venta excede el monto minnimo"""
    return venta['monto'] > monto_minimo

def calcular_y_formatear_venta(venta: Dict, factor_impuesto: float) -> Dict:
    """Funcion pura -transformacion/map: crea un nuevo diccionario con impuesto y asegura la inmutabilidd al 
    no modificar la venta original"""
    monto_con_impuesto = venta['monto'] * factor_impuesto
    return {
        'id': venta['id'],
        'monto_original': venta['monto'],
        'monto_final': monto_con_impuesto
    }

def obtener_monto_final(venta_procesada: Dict) -> float:
    """Funcion pura -utilidad: extrae el monto final de una venta procesada."""
    return venta_procesada['monto_final']


# ----------------------------------------------------------------------
MONTO_MINIMO = 100
FACTOR_IMPUESTO = 1.15 # 1 + 0.15

def procesar_ventas_funcional(ventas: List[Dict]) -> Tuple[List[Dict], float]:
    """Hace el pipeline funcional de procesamiento de ventas.Utiliza funciones como 
    ciudadanos de primera clase (map, filter).
    """

    # Paso1: Filtrar 
    # creamos una versión parcial de filtrar_por_monto_minimo fijando MONTO_MINIMO
    filtro_valido = lambda v: filtrar_por_monto_minimo(MONTO_MINIMO, v)
    ventas_filtradas = filter(filtro_valido, ventas)
    
    # Paso 2: Mapear / transformar
    # creamos una versión de calcular_y_formatear_venta fijando FACTOR_IMPUESTO
    transformador = lambda v: calcular_y_formatear_venta(v, FACTOR_IMPUESTO)
    ventas_procesadas = list(map(transformador, ventas_filtradas))
    
    # Paso 3: Reducir / agregar el total
    # mapeamos los resultados para obtener solo los montos finales y usamos sum()
    total_acumulado = sum(map(obtener_monto_final, ventas_procesadas))
    
    return ventas_procesadas, total_acumulado

# datos de pruebas s 

ventas_ejemplo = [
    {'id': 1, 'monto': 50},
    {'id': 2, 'monto': 150},
    {'id': 3, 'monto': 200},
    {'id': 4, 'monto': 80},
    {'id': 5, 'monto': 300},
]

# ejecucion
lista_final, gran_total = procesar_ventas_funcional(ventas_ejemplo)

print("--- Resultado del procesamiento funcional ---")
print("\n[Ventas Procesadas (Filtradas > $100 y Transformadas con Impuesto)]")
print(lista_final)

print("\n[Total Acumulado de Montos Finales]")
print(f"${gran_total:.2f}")