"""
    Bienvenido al día 94 de #100diasdepython        
                El reto de hoy es:
Crea una función que use argumentos arbitrarios 
    para recibir N-cadenas de nombres y 
        devuelva una lista de N-saludos
    ejemplo de salida ['Hola Katy','Hola Ariel']
        Imprime el resultado en una Lista
"""


def saludos(*nombres):
    resultado = ["Hola " + n for n in nombres]
    return resultado


lista = saludos("Katy", "Pepe", "Ariel")
print(lista)
# Resultado: ['Hola Katy', 'Hola Pepe', 'Hola Ariel']
