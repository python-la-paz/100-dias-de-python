"""
    Bienvenido al día 90 de #100diasdepython        
                El reto de hoy es:
    Utiliza datetime para imprimir la fecha y hora
en formato de 12 horas ejemplo "2022/07/18 11:30 PM"
        Imprime el resultado en una cadena
"""
from datetime import datetime

fecha = datetime.today()
formato = fecha.strftime("%Y/%m/%d %I:%M %p")
print(formato)
# Resultado:
# 2022/07/18 01:35 AM
