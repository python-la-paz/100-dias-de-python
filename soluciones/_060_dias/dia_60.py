"""
    Bienvenido al día 60 de #100diasdepython    
            El reto de hoy es:
Utiliza una función lambda para capitalizar las 
        palabras de la siguiente lista
["llevo", "sesenta", "dias", "programando","wiii"]
        Imprime el resultado en nueva lista
"""
cadenas = ["llevo", "sesenta", "dias", "programando", "wiii"]
cadenas = list(map(lambda x: x.capitalize(), cadenas))
print(cadenas)
# Resultado: ['Llevo', 'Sesenta', 'Dias', 'Programando', 'Wiii']
