"""
    Bienvenido al día 51 de #100diasdepython
            El reto de hoy es:
Crea una función que calcule el volumen de un cilindro
    Los parámetros de entrada son base y altura
    El valor de salida el el volumen del cilindro
Ejecuta la función para el caso base= 5, altura= 7
            Imprime el resultado
"""
from math import pi


def volumen_cilindro(base: float, altura: float):
    """
    Función que calcula el volumen de un cilindro
    Args:
        base (float): diámetro del cilindro
        altura (float): altura del cilindro

    Returns:
        float: volumen calculado del cilindro
    """
    radio = base / 2
    volumen = pi * (radio**2) * altura
    return volumen


volumen = volumen_cilindro(5, 7)
print(volumen)
# Resultado: 137.44467859455347
