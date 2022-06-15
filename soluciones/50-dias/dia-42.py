"""
    Bienvenido al día 42 de #100diasdepython
            El reto de hoy es:
    Utiliza los conjunto del reto anterior, 
    para encontrar la union de ambos conjuntos
    sin usar ciclos e imprime el resultado
"""
animales = {"perro", "pajaro", "leon", "tigre"}
mascotas = {"perro", "gato"}
union = animales.union(mascotas)
print(union)
# Resultado: {'leon', 'tigre', 'perro', 'gato', 'pajaro'}
