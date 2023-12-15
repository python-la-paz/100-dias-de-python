"""
        Bienvenido al día 70 de #100diasdepython
                El reto de hoy es:
    Utiliza Regex para extraer todas las palabras que
    contengan al menos una 'a' en la siguiente cadena
        'Llevas programando 70 días seguidos'
    Imprime una lista con las palabras extraídas
"""
import re

cadena = "Llevas programando 70 dias seguidos"
patron = r"\w*a.\w*"
subcadenas = re.findall(patron, cadena)
print(subcadenas)
# Resultado:
# ['Llevas', 'programando', 'dias']
