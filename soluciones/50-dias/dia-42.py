"""
    Bienvenido al día 42 de #100diasdepython
            El reto de hoy es:
    Utiliza los conjunto del reto anterior, 
    para encontrar la union de ambos conjuntos
    sin usar ciclos e imprime el resultado
"""
animales = {"perro", "pájaro", "león", "tigre"}
mascotas = {"perro", "gato"}
union = animales.union(mascotas)
print(union)
# Resultado: {'león', 'tigre', 'perro', 'gato', 'pájaro'}
