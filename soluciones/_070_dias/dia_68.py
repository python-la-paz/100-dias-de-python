"""
        Bienvenido al día 68 de #100diasdepython
                El reto de hoy es:
Utiliza Regex para cambiar el formato de las fechas
de YYYY-MM-DD  a DDMMYYYY de las fechas de la lista
['2022-12-05', '1993-06-12', '2005-01-26', '2021-10-08']
Imprime una lista con las fechas con el nuevo formato
"""
import re

fechas = ["2022-12-05", "1993-06-12", "2005-01-26", "2021-10-08"]
patron = r"(\d{4})-(\d{2})-(\d{2})"
reemplazo = r"\3\2\1"
validos = [re.sub(patron, reemplazo, f) for f in fechas]
print(validos)
# Resultado:
# ['05122022', '12061993', '26012005', '08102021']
