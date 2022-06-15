"""
    Bienvenido al día 36 de #100diasdepython
            El reto de hoy es:
Utiliza el diccionario de palabras del reto 
anterior para eliminar el primer elemento del
diccionario, imprime la cantidad de elementos 
            del diccionario
"""
palabras = {
    "programacion": "la programacion es la creacion de software",
    "python": "lenguaje de programacion multiparadigma",
    "html": "lenguaje estandar de marcado de etiquetas",
    "css": "hojas de estilo en cascada",
    "flask": "framework de python",
    "api": "interfaz de programación de aplicaciones",
}
palabras.pop("programacion")
print(len(palabras))
# Resultado: 5
