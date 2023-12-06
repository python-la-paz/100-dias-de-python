"""
    Bienvenido al día 54 de #100diasdepython
            El reto de hoy es:
Crea una función que reciba una lista de cadenas y
    devuelva un diccionario con la cantidad
            de vocales de cada cadena
Ejemplo de entrada: ['Python', 'es', 'cool']
Ejemplo de salida: {'Python': 1, 'es': 1, 'cool': 2}
            Imprime el resultado
"""


def vocales(cadenas: list):
    """
    Función que cuenta la cantidad de vocales en una lista de cadenas

    Args:
        cadenas (list): lista de cadenas

    Returns:
        dict: diccionario con la cantidad devocales de cada cadena
    """
    salida = {}
    cadenas = [c.lower() for c in cadenas]
    for cadena in cadenas:
        contador = 0
        for vocal in "aeiou":
            contador += cadena.count(vocal)
        salida[cadena] = contador
    return salida


ejemplo = ["Python", "es", "cool"]
print(vocales(ejemplo))
# Resultado: {'Python': 1, 'es': 1, 'cool': 2}
