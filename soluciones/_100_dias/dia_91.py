"""
    Bienvenido al día 91 de #100diasdepython
                El reto de hoy es:
    Crea una función que devuelva los cuadrados
de los primeros 10 números enteros iniciando en 1
                utilizando yields
        Imprime el resultado en una Lista
"""


def cuadrados(limite):
    i = 1
    while i <= limite:
        yield i * i
        i += 1


lista = list(cuadrados(10))
print(lista)
# Resultado:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
