"""
    Bienvenido al día 59 de #100diasdepython
            El reto de hoy es:
Utiliza una función lambda para ordenar de forma
ascendente la siguiente lista de tuplas tomando el
        valor numérico como referencia
[("Quimica", 88),("Fisica", 90), ("Lenguaje", 97)]
            Imprime el resultado
"""
notas = [("Quimica", 88), ("Fisica", 90), ("Lenguaje", 97)]
notas.sort(key=lambda x: x[1])
print(notas)
