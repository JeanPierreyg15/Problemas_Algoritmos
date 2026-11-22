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
        todos_segmentos_texto_rellenado = []

        for palabra in palabras:
            if not palabra:
                continue

            for i in range(0,len(palabra),cantidad):
                segmento_texto = palabra[i:i+cantidad]
                segmento_texto_rellenado = segmento_texto.ljust(cantidad,"*")
                segmento_texto_rellenado.append(segmento_texto_rellenado)

        print(" ".join(segmento_texto_rellenado))
    except ValueError:
        return print("Valor ingresado invalido")
    except AttributeError:
        return print("Debe ingresar una texto")



convertir_texto("It’s not a fashion statement, it’s a deathwish",3)

'''
Revisión:

* Evitemos spanglish, o solo español o solo inglés, y te sugiero que siempre sea inglés porque es el estándar ya que todo código que usamos está en inglés (ojo, hablamos de código de datos, los datos pueden estar en el idioma que requiera la aplicaicón).
* Te sugiero ser más preciso con los identificadores, por ejemplo, bloques_finales, bloque, bloque_completo, etc, no logran transmitir muy bien lo que representan, sería mejor algo como:
    - bloque -> base_segmented_text | Indica que es segmento de texto original.
    - bloque_completo -> segmented_and_filled_text | Indica que es el segmento de texto ya rellenado.
    - bloques_finales -> all_segmented_and_filled_text | Indica que es la lista de todos los segmentos de texto ya rellenados.
Algo que puede ayudarte a saber cuál sería el mejor nombre es revisar los términos que se usan a nivel del problema planteado, por ejemplo, en este caso se habla de "texto segmentado", entonces los identificadores deberían reflejar eso. Entonces, evitemos cosas muy abstractos o demasiado técnicas para facilitar la comprensión.
'''