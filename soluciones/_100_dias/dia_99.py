"""
Bienvenido al día 99 de #100diasdepython
            El reto de hoy es:
    Utiliza try para capturar e imprimir la
excepción de una división entre 0 del siguiente
            fragmento de código
"""
a = 7
try:
    b = a / 0
except Exception as e:
    print("Error: {}".format(e))
