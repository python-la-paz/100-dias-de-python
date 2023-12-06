"""
    Bienvenido al día 61 de #100diasdepython
            El reto de hoy es:
    Utiliza Regex para validar que las cadenas de
        la lista sean totalmente numéricas
["20200806", "jun122022", "202204DD", "20221208", "22mar2022"]
    Imprime una lista con las cadenas numéricas
"""
import re

correos = ["20200806", "jun122022", "202204DD", "20221208", "22mar2022"]
patron = "[\d]{8}"
validos = [c for c in correos if re.search(patron, c)]
print(validos)
# Resultado: ['20200806', '20221208']
