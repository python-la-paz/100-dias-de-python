"""
    Bienvenido al día 36 de #100diasdepython
            El reto de hoy es:
Utiliza el diccionario de palabras del reto
anterior para eliminar el primer elemento del
diccionario, imprime la cantidad de elementos
            del diccionario
"""
palabras = {
    "programacion": "la programación es la creación de software",
    "python": "lenguaje de programación multiparadigma",
    "html": "lenguaje estándar de marcado de etiquetas",
    "css": "hojas de estilo en cascada",
    "flask": "framework de python",
    "api": "interfaz de programación de aplicaciones",
}
palabras.pop("programacion")
print(len(palabras))
# Resultado: 5
