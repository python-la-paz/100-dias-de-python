"""
Bienvenido al día 83 de #100diasdepython
            El reto de hoy es:
    Utiliza datetime para convertir la fecha
        "Jul 11 2022 1:30AM" al formato
            "2022-07-11 01:30:00"
            Imprime el resultado
"""
from datetime import datetime

fecha = "Jul 11 2022 1:30AM"
resultado = datetime.strptime(fecha, "%b %d %Y %I:%M%p")
print(resultado)
# Resultado:
# 2022-07-11 01:30:00
