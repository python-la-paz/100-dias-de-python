"""
        Bienvenido al día 69 de #100diasdepython    
                El reto de hoy es:
Utiliza Regex para extraer todas las 'a' seguidas de 
        una o mas 'b's de la siguiente cadena 
        'abholaaaaabaaabbpythonistaaaaaabbbbb'
Imprime una lista con las subcadenas extraídas
"""
import re

cadena = "abholaaaaabaaabbpythonistaaaaaabbbbb"
patron = "a+b?"
subcadenas = re.findall(patron, cadena)
print(subcadenas)
# Resultado:
# ['ab', 'aaaaab', 'aaab', 'aaaaaab']
