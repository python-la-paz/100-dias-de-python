"""
Bienvenido al día 79 de #100diasdepython        
            El reto de hoy es:
Utiliza itertools para obtener los elementos 
    de la siguiente lista hasta que alguno 
            contenga un "0" 
    [2, 3, 5, 7, 13, 103, 25, 15, 45] 
    Imprime el resultado en una lista    
"""
import itertools

lista = [[[[[2, 3, 5, 7, 13, 103, 25, 15, 45]]]]]
predicado = lambda x: "0" not in str(x)
resultado = list(itertools.takewhile(predicado, lista))
print(resultado)
# Resultado:
# [2, 3, 5, 7, 13]
