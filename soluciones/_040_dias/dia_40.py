"""
    Bienvenido al día 40 de #100diasdepython
            El reto de hoy es:
Utiliza el conjunto del reto anterior y elimina
al gato del conjunto, si es que existiera, sin
usar sentencias condicionales e imprime el resultado
"""
animales = {"perro", "gato", "pájaro", "león", "tigre"}
animales.discard("gato")
print(animales)
# Resultado: {'pájaro', 'tigre', 'perro', 'león'}
