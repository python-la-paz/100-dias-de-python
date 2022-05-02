"""
                Bienvenido al día 12 de #100diasdepython
                        El reto de hoy es:
Intercambia los valores de dos variables e imprime su ubicación en memoria
                        utilizando la función id()
"""
años = 42
edad = "edad"
años, edad = edad, años
print(id(años), id(edad))
# Resultado: 1722722222704 140710691867584
