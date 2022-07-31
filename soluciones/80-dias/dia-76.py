"""
Bienvenido al día 76 de #100diasdepython        
            El reto de hoy es:
Utiliza itertools para obtener el valore 
maximo de cada tupla de la siguiente lista
    [(2, 4, 6), (7, 8, 5, 6), (5, 10)]
    Imprime el resultado en una lista
"""
import itertools

lista = [(2, 4, 6), (7, 8, 5, 6), (5, 10)]
resultado = list(itertools.starmap(max, lista))
print(resultado)
# Resultado: [6, 8, 10]
