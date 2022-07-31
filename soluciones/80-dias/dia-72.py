"""
        Bienvenido al día 72 de #100diasdepython        
                El reto de hoy es:
Utiliza itertools para obtener la cantidad de veces que 
        se repite cada numero en la lista
        [0, 1, 1, 2, 3, 2, 4, 5, 5, 8, 4]
Imprime el resultado en un diccionario con el formato 
        {numero:cantidad de repeticiones}
"""
import itertools

data = [0, 1, 1, 2, 3, 2, 4, 5, 5, 8, 4]
resultado = {}
data = sorted(data)
for k, g in itertools.groupby(data):
    resultado[k] = len(list(g))
print(resultado)
# Resultado:
# {0: 1, 1: 2, 2: 2, 3: 1, 4: 2, 5: 2, 8: 1}
