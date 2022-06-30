"""
    Bienvenido al día 64 de #100diasdepython    
            El reto de hoy es:
Utiliza Regex para quitar los ceros innecesarios
        de las direcciones IP de la lista
["192.08.001.5", "10.120.023.001", "192.160.2.1"]
        Imprime una lista con las IPs validas
"""
import re

ips = ["192.08.001.5", "10.120.023.001", "192.160.2.1"]
validos = [re.sub("\.[0]*", ".", ip) for ip in ips]
print(validos)
# R: ['192.8.1.5', '10.120.23.1', '192.160.2.1']
