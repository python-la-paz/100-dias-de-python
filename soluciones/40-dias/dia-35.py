"""
    Bienvenido al día 35 de #100diasdepython
            El reto de hoy es:
Utiliza el diccionario de palabras del reto 
anterior para agregar una nueva palabra y su 
definicion, imprime la cantidad de elementos 
            del diccionario
"""
palabras = {
    "programacion": "la programación es la creación de software",
    "python": "lenguaje de programación multiparadigma",
    "html": "lenguaje estándar de marcado de etiquetas",
    "css": "hojas de estilo en cascada",
    "flask": "framework de python",
}
palabras["api"] = "interfaz de programación de aplicaciones"
print(len(palabras))
# Resultado: 6
