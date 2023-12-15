"""
    Bienvenido al día 50 de #100diasdepython
            El reto de hoy es:
    Genera 5 números enteros de forma aleatoria
            Almacena el resultado en una lista
        Suma la lista e imprime el resultado
"""
import random

lista_random = [random.randint(0, 100) for i in range(5)]
suma_random = sum(lista_random)
print(suma_random)
