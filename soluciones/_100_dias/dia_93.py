"""
    Bienvenido al día 93 de #100diasdepython        
                El reto de hoy es:
Crea una función que use yield y genere los primeros
        10 números de la serie de Fibonacci 
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        Imprime el resultado en una Lista
"""


def fibonnaci(limite):
    ultimo, actual = 0, 1
    while limite > 0:
        yield actual
        ultimo, actual = actual, ultimo + actual
        limite -= 1


serie = list(fibonnaci(10))
print(serie)
# Resultado: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
