"""
    Bienvenido al día 41 de #100diasdepython
            El reto de hoy es:
    Utiliza el conjunto del reto anterior, 
    define un nuevo conjunto de mascotas, 
encuentra la interseccion de ambos conjuntos
    sin usar ciclos e imprime el resultado
"""
animales = {"perro", "pajaro", "leon", "tigre"}
mascotas = {"perro", "gato"}
interseccion = animales.intersection(mascotas)
print(interseccion)
# Resultado: {'perro'}
