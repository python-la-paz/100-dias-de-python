"""
        Bienvenido al día 96 de #100diasdepython
                    El reto de hoy es:
Crea una función que use argumentos arbitrarios de tipo
Keyword para recibir nombre, apellido y edad y devuelva
estos argumentos en un diccionario en el siguiente formato
    {"nombre": "Pepito", "apellido":"Perez","edad":25}
                Imprime el resultado
"""


def persona(**atributos):
    resultado = dict()
    for key, value in atributos.items():
        resultado[key] = value
    return resultado


print(persona(nombre="Pepito", apellido="Perez", edad=25))
# Resultado: {'nombre': 'Pepito', 'apellido': 'Perez', 'edad': 25}
