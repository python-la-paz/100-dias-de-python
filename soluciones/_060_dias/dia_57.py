"""
    Bienvenido al día 57 de #100diasdepython
            El reto de hoy es:
    Utiliza una función lambda para encontrar los
        múltiplos de 3 en la lista de números
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        Imprime el resultado en nueva lista
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiplos = list(filter(lambda x: x % 3 == 0, lista))
print(multiplos)
# Resultado: [3, 6, 9]
