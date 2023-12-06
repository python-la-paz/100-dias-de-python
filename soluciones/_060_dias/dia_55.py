"""
    Bienvenido al día 55 de #100diasdepython    
            El reto de hoy es:
    Crea una función recursiva para hacer una 
            cuenta regresiva a 0
La función tiene como parámetro de entrada un numero
    Ejecuta la función para el numero 5
Imprime el valor de la cuenta en cada iteración
"""


def atras(num: int):
    """
    Función para hacer una cuenta regresiva

    Args:
        num (int): inicio de la cuenta atrás
    """
    print(num)
    num = num - 1
    if num >= 0:
        atras(num)
    pass


atras(5)
# Resultado:
# 5
# 4
# 3
# 2
# 1
# 0
