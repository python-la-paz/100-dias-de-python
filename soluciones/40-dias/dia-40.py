"""
    Bienvenido al día 40 de #100diasdepython
            El reto de hoy es:
Utiliza el conjunto del reto anterior y elmina
al gato del conjunto, si es que existiera, sin 
usar sentecias condicionales e imprime el resultado
"""
animales = {"perro", "gato", "pajaro", "leon", "tigre"}
animales.discard("gato")
print(animales)
# Resultado: {'pajaro', 'tigre', 'perro', 'leon'}
