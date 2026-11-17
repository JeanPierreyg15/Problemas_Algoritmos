"""
Realizar un algoritmo que tome un texto y lo separe por espacios según una cantidad de caracteres determinada por el usuario.
Considerar que si un grupo de caracteres es menor a la cantidad ingresada por el usuario, sean completados por asteriscos. Por ejemplo:

Texto: “It’s not a fashion statement, it’s a deathwish”
Cantidad de caracteres: 3

Texto segmentado: “It’ s** not a** fas hio n** sta tem ent ,** it’ s** a** dea thw ish”
"""

def convertir_texto(texto,cantidad):
    try:
        int(cantidad)
        palabras = texto.split(" ")
        bloques_finales = []

        for palabra in palabras:
            if not palabra:
                continue

            for i in range(0,len(palabra),cantidad):
                bloque = palabra[i:i+cantidad]
                bloque_completo = bloque.ljust(cantidad,"*")
                bloques_finales.append(bloque_completo)

        print(" ".join(bloques_finales))
    except ValueError:
        return print("Valor ingresado invalido")
    except AttributeError:
        return print("Debe ingresar una texto")



convertir_texto("It’s not a fashion statement, it’s a deathwish",3)