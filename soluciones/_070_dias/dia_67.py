"""
        Bienvenido al día 67 de #100diasdepython
                El reto de hoy es:
Utiliza Regex para cambiar el formato de las fechas
de YYYYMMDD a YYYY-MM-DD de las fechas de la lista
["20221205", "19930612", "20050126", "20211008"]
        Imprime una lista con las fechas
"""
import re

fechas = ["20221205", "19930612", "20050126", "20211008"]
valido = [re.sub(r"(\d{4})(\d{1,2})(\d{1,2})", r"\1-\2-\3", f) for f in fechas]
print(valido)
# Resultado:
# ['2022-12-05', '1993-06-12', '2005-01-26', '2021-10-08']
