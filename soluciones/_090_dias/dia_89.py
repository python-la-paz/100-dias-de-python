"""
        Bienvenido al día 89 de #100diasdepython
                    El reto de hoy es:
        Utiliza calendar para obtener los días lunes
                del mes Julio del año 2022
            Imprime el resultado en una lista
"""
from calendar import monthcalendar

lunes = [s[0] for s in monthcalendar(2022, 7) if s[0] != 0]
print(lunes)
# Resultado: [4, 11, 18, 25]
