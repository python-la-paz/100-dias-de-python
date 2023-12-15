"""
    Bienvenido al día 48 de #100diasdepython
            El reto de hoy es:
    Con un rango de 5 números crea una lista
    que refleje con valores booleanos cuales
        son pares e imprime el resultado
"""
lista_pares = []
for n in range(5):
    if n % 2 == 0:
        lista_pares.append(True)
    else:
        lista_pares.append(False)
print(lista_pares)
# Resultado:
# [True, False, True, False, True]
