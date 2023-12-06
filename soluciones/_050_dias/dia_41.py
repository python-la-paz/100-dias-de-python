"""
    Bienvenido al día 41 de #100diasdepython
            El reto de hoy es:
    Utiliza el conjunto del reto anterior,
    define un nuevo conjunto de mascotas,
encuentra la intersección de ambos conjuntos
    sin usar ciclos e imprime el resultado
"""
animales = {"perro", "pájaro", "león", "tigre"}
mascotas = {"perro", "gato"}
interseccion = animales.intersection(mascotas)
print(interseccion)
# Resultado: {'perro'}
