"""
Bienvenido al día 77 de #100diasdepython
            El reto de hoy es:
    Utiliza itertools para obtener los
    múltiplos de 5 de la siguiente lista
        [1,5,10,23,3,555,11,10]
    Imprime el resultado en una lista
"""
import itertools

lista = [1, 5, 10, 23, 3, 555, 11, 10]
predicado = lambda x: x % 5 != 0
multiplos = list(itertools.filterfalse(predicado, lista))
print(multiplos)
# Resultado: [5, 10, 555, 10]
