"""
    Bienvenido al día 33 de #100diasdepython
            El reto de hoy es:
    Declara una cadena que sea un palíndromo
        y verifica que lo sea sin usar
            funciones adicionales
    Imprime el resultado en una sola línea
"""
palabra = "reconocer"
palabra_revertida = palabra[::-1]
palindromo = palabra == palabra_revertida
print(palindromo)
