"""
Bienvenido al día 98 de #100diasdepython
            El reto de hoy es:
Utiliza timeit para obtener el tiempo de
    ejecución de la siguiente función
Imprime el resultado en una sola línea
"""


def lazy():
    suma = 0
    for i in range(0, 50000000):
        suma += i
