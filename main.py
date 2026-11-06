import json
import math

def calculate_isotherm(v1, v2):
    """
    Рассчитывает изотермический процесс.
    P * V = const. => P = C / V
    """
    # Температура и количество вещества (константы для простоты)
    T = 300  # Кельвины
    n = 1    # моль
    R = 8.314 # Дж/(моль*К)
    
    # Константа C = n*R*T
    C = n * R * T
    
    # Генерируем точки от V1 до V2
    steps = 50
    v_data = []
    p_data = []
    
    # Чтобы график был красивым, берем диапазон с шагом
    # Если V1 > V2, шаг будет отрицательным
    step = (v2 - v1) / steps if v2 != v1 else 0.1
    
    for i in range(steps + 1):
        v = v1 + i * step
        if v <= 0:
            continue # Избегаем деления на ноль
        p = C / v
        v_data.append(v)
        p_data.append(p)
    
    # Возвращаем JSON-строку, которую распарсит JS
    return json.dumps({
        "v_data": v_data,
        "p_data": p_data
    })
