"""
Bienvenido al día 85 de #100diasdepython
            El reto de hoy es:
Utiliza datetime para imprimir la fecha y
            hora actual en UTC
"""
from datetime import datetime, timezone

utc = datetime.now(timezone.utc)
print(utc)
# Resultado:
# 2022-07-13 05:35:58.236244+00:00
