"""
    Bienvenido al día 63 de #100diasdepython
            El reto de hoy es:
Utiliza Regex para validar que las cadenas solo
        contengan caracteres alfanuméricos
["Python3.10", "Python3", "ProgramandoAndo", "jun2022",
        "#100diasdecodigo", "Felicidades!"]
    Imprime una lista con las cadenas validas
"""
import re

correos = [
    "Python3.10",
    "Python3",
    "ProgramandoAndo",
    "jun2022",
    "#100diasdecodigo",
    "Felicidades!",
]
patron = r"^[a-zA-Z0-9_]+$"
validos = [c for c in correos if re.search(patron, c)]
print(validos)
# Resultado: ['Python3', 'ProgramandoAndo', 'jun2022']
