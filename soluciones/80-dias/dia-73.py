"""
        Bienvenido al día 73 de #100diasdepython        
                El reto de hoy es:
Utiliza itertools para obtener todas las permutaciones 
        posibles con las letras de la siguiente lista 
                ["r", "i", "o"]
        Imprime el resultado en una lista de tuplas
"""
import itertools

data = ["r", "i", "o"]
resultado = list(itertools.permutations(data))
print(resultado)
# Resultado:
# [
#     ("r", "i", "o"),
#     ("r", "o", "i"),
#     ("i", "r", "o"),
#     ("i", "o", "r"),
#     ("o", "r", "i"),
#     ("o", "i", "r"),
# ]
