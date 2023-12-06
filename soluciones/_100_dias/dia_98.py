"""
Bienvenido al día 98 de #100diasdepython
            El reto de hoy es:
Utiliza timeit para obtener el tiempo de
    ejecución de la siguiente función
Imprime el resultado en una sola línea
"""
import timeit


def lazy():
    suma = 0
    for i in range(0, 50000000):
        suma += i


start = timeit.default_timer()
lazy()
end = timeit.default_timer()
print(end - start)

# Resultado aprox: 2.634737699998368
