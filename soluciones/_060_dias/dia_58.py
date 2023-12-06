"""
    Bienvenido al día 58 de #100diasdepython    
            El reto de hoy es:
Utiliza una función lambda para sumar las siguientes 
listas lista_a = [2, 4, 5] , lista_b = [6, 7, 1] 
        Imprime el resultado en nueva lista
"""

lista_a = [2, 4, 5]
lista_b = [6, 7, 1]
suma = list(map(lambda x, y: x + y, lista_a, lista_b))
print(suma)
# Resultado: [8, 11, 6]
