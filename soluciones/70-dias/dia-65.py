"""
        Bienvenido al día 65 de #100diasdepython    
                    El reto de hoy es:
Utiliza Regex para quitar los prefijos telefonicos de los 
            telefonos de la siguiente lista
["+54 11 1234 5678", "+591 68754321", "+56 9 8765 4321"]
Imprim una lista con los telefonos sin prefijos telefonicos
"""
import re

phones = ["+54 11 1234 5678", "+591 68754321", "+56 9 8765 4321"]
limpio = [re.sub("\+[0-9]* ", "", ip) for ip in phones]
print(limpio)
# R: ['11 1234 5678', '68754321', '9 8765 4321']
