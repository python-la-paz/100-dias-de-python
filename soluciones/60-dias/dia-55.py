"""
    Bienvenido al día 55 de #100diasdepython    
            El reto de hoy es:
    Crea una funcion recursiva para hacer una 
            cuenta regresiva a 0
La funcion tiene como parametro de entrada un numero
    Ejecuta la funcion para el numero 5
Imprime el valor de la cuenta en cada iteracion
"""


def atras(num: int):
    """
    Funcion para hacer una cuenta regresiva

    Args:
        num (int): inicio de la cuenta artras
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
