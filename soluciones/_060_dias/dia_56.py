"""
    Bienvenido al día 56 de #100diasdepython
            El reto de hoy es:
    Utiliza una función lambda para encontrar la raíz
cuadrada de esta lista de números [49, 4, 36, 16, 25]
    Imprime el resultado en nueva lista
"""
from math import sqrt


números = [49, 4, 36, 16, 25]
cuadrados = list(map(lambda x: sqrt(x), números))
print(cuadrados)
# Resultado: [7.0, 2.0, 6.0, 4.0, 5.0]
