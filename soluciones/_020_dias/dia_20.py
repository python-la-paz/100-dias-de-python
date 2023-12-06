"""
            Bienvenido al día 20 de #100diasdepython
                    El reto de hoy es:
            De la siguiente cadena: 'PpYyTtHhOoNnIiSsTtAa' 
Separa las mayúsculas y minúsculas, sin usar ciclos, en nuevas cadenas 
            e imprime el resultado en una sola linea
"""
cadena = "PpYyTtHhOoNnIiSsTtAa"
mayusculas = cadena[::2]
minusculas = cadena[1::2]
print(mayusculas, minusculas)
# Resultado: PYTHONISTA pythonista
