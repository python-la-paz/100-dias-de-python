"""
        Bienvenido al día 66 de #100diasdepython    
                El reto de hoy es:
    Utiliza Regex para elminar los caracteres que 
    no sean alfanumericos en las cadenas de la lista
["Python3.10", "Python3", "ProgramandoAndo", "jun2022", 
        "#100diasdecodigo", "Felicidades!"]
    Imprime una lista con las cadenas limpias
"""
import re

cadenas = [
    "Python3.10",
    "Python3",
    "ProgramandoAndo",
    "jun2022",
    "#100diasdecodigo",
    "Felicidades!",
]
validos = [re.sub("[^A-Za-z0-9]+", "", c) for c in cadenas]
print(validos)
# Resultado:
# ['Python310', 'Python3', 'ProgramandoAndo', 'jun2022', '100diasdecodigo', 'Felicidades']
