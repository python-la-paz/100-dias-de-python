"""
Bienvenido al día 97 de #100diasdepython        
            El reto de hoy es:
Crea una función que use argumentos arbitrarios 
de tipo Keyword para recibir los 3 lados de un 
        triangulo y calcule su perímetro
Imprime el resultado en un numero de punto flotante
"""


def perimetro(**atributos):
    a = atributos["a"]
    b = atributos["b"]
    c = atributos["c"]
    return float(a + b + c)


print(perimetro(a=3, b=4, c=4))
# Resultado: 11.0
