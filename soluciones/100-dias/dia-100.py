"""
Bienvenido al día 🎉100🎉 de #100diasdepython        
            El reto de hoy es:
Utiliza try para capturar e imprimir la excepcion 
dentro de  la siguiente funcion y agrega un mensaje 
            final utilizando finally
    En este reto si se aceptan multiples print
"""


def dia100():
    try:
        mensaje = "Llegaste al último día"
        print(mensaje[len(mensaje)])
    except Exception as e:
        print("Error: {}".format(e))
    finally:
        print("Muchas gracias por participar!!")


dia100()
# Resultado:
# Error: string index out of range
# Muchas gracias por participar!!
