"""
    Bienvenido al día 71 de #100diasdepython
            El reto de hoy es:
    Utiliza itertools para generar una serie
    de sumas acumuladas con los números de la
    siguiente lista [0, 1, 1, 2, 3, 5, 8]
            Imprime el resultado
"""
import itertools

data = [0, 1, 1, 2, 3, 5, 8]
print(list(itertools.accumulate(data)))
# Resultado:
# [0, 1, 2, 4, 7, 12, 20]
