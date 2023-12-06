"""
    Bienvenido al día 95 de #100diasdepython
                El reto de hoy es:
Crea una función que use argumentos arbitrarios
    para recibir N-números y determine cual es
el mayor y el menor y los devuelva en un diccionario
en el siguiente formato {"mayor": 5, "menor":-10}
                Imprime el resultado
"""


def mayor_menor(*números):
    mayor = max(números)
    menor = min(números)
    return {"mayor": mayor, "menor": menor}


print(mayor_menor(1, -3, 5, 8, -6, 8, 10))
# Respuesta: {'mayor': 10, 'menor': -6}
