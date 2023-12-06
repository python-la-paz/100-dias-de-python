"""
        Bienvenido al día 52 de #100diasdepython
                El reto de hoy es:
Crea una función que convierta un número entero en binario
                sin usar la función bin()
        El parámetro de entrada es un número entero
        El valor de salida es una cadena del valor
                del número en binario
        Ejecuta la función para el número 52
                Imprime el resultado
"""


def binario(num: int):
    """
    Convierte un número entero en binario

    Args:
        num (int): número entero a convertir

    Returns:
        str: valor del número en binario
    """
    if num <= 0:
        return "0"
    binario = ""
    while num > 0:
        residuo = int(num % 2)
        num = int(num / 2)
        binario = str(residuo) + binario
    return binario


print(binario(52))
# Resultado: 110100
