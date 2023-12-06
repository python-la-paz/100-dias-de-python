"""
        Bienvenido al día 53 de #100diasdepython    
                El reto de hoy es:
    Crea una función que reciba una lista de 
números y devuelva una lista de los números al cuadrado
    Ejecuta la función para la lista [2, 3, 5, 7, 11]
                Imprime el resultado
"""


def cuadrados(números: list):
    """
    Función que eleva al cuadrado cada numero de la lista
    Args:
        números (list): lista de números
    Returns:
        list: lista de números
    """
    cuadrados = [n**2 for n in números]
    return cuadrados


lista = [2, 3, 5, 7, 11]
print(cuadrados(lista))
# Resultado: [4, 9, 25, 49, 121]
