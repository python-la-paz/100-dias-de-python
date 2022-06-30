"""
    Bienvenido al día 56 de #100diasdepython    
            El reto de hoy es:
    Utiliza una funcion lambda para encontrar la raiz 
cuadrada de esta lista de numeros [49, 4, 36, 16, 25]
    Imprime el resultado en nueva lista
"""
from math import sqrt


numeros = [49, 4, 36, 16, 25]
cuadrados = list(map(lambda x: sqrt(x), numeros))
print(cuadrados)
# Resultado: [7.0, 2.0, 6.0, 4.0, 5.0]
