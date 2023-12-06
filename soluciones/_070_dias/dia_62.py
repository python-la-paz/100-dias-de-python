"""
    Bienvenido al día 62 de #100diasdepython
            El reto de hoy es:
    Utiliza Regex para validar la lista de emails
        ["pythonlapaz@gmail.com", "dias.com",
    "comidita@.com", "programando@outlook.com"]
        Imprime una lista con los emails validos
"""
import re

correos = [
    "pythonlapaz@gmail.com",
    "dias.com",
    "comidita@.com",
    "programando@outlook.com",
]
patron = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
validos = [c for c in correos if re.search(patron, c)]
print(validos)
# R: ["pythonlapaz@gmail.com", "programando@outlook.com"]
