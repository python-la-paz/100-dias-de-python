"""
    Bienvenido al día 37 de #100diasdepython
            El reto de hoy es:
Utiliza el diccionario de palabras del reto 
anterior para eliminar todos los elemento del
diccionario sin usar ciclos, imprime el resultado
"""
palabras = {
    "python": "lenguaje de programacion multiparadigma",
    "html": "lenguaje estandar de marcado de etiquetas",
    "css": "hojas de estilo en cascada",
    "flask": "framework de python",
    "api": "interfaz de programación de aplicaciones",
}
palabras.clear()
print(palabras)
# Resultado: {}
