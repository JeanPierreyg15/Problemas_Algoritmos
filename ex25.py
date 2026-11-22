"""
Crear un algoritmo que, dado un texto, sus vocales sean reemplazadas por determinados números (a=1, e=2, i=3, o=4, u=5). Por ejemplo:

Texto: “Ya no es así, me dejaste morir (perdón por existir)”

Texto con vocales reemplazadas: “Y1 n4 2s 1s3, m2 d2j1st2 m4r3r (p2rd4n p4r 2x3st3r)”
"""


def reemplazar_letras(texto):
    vocales = {"a":1,"e":3,"i":5,"o":8,"u":9}
    nuevo_texto=""
    try:    
        for letra in texto:
            if letra.lower() in vocales:
                valor = str(vocales[letra])
                nuevo_texto += valor
                continue
            nuevo_texto += letra

        print(f"Texto: {texto}")
        print(f"Texto con vocales reemplazadas: {nuevo_texto}")
    except TypeError:
        return print("Debes ingresar un texto")

reemplazar_letras("Ya no es así, me dejaste morir (perdón por existir)")

'''
Revisión:

* Falta validar textos no vacíos.
* Es una forma que resulta; no obstante, si por ejemplo el diccionario cambiara o los códigos no fueran secuenciales y se definier así: a=1, e=3, i=5, o=8, u=9, sería más mantenible usar un diccionario.
'''