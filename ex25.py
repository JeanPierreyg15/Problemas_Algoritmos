"""
Crear un algoritmo que, dado un texto, sus vocales sean reemplazadas por determinados números (a=1, e=2, i=3, o=4, u=5). Por ejemplo:

Texto: “Ya no es así, me dejaste morir (perdón por existir)”

Texto con vocales reemplazadas: “Y1 n4 2s 1s3, m2 d2j1st2 m4r3r (p2rd4n p4r 2x3st3r)”
"""


def reemplazar_letras(texto):
    vocales="aeiou"
    nuevo_texto=""
    try:    
        for letra in texto:
            if letra.lower() in vocales:
                nuevo_texto += str(vocales.index(letra)+1)
                continue
            nuevo_texto += letra

        print(f"Texto: {texto}")
        print(f"Texto con vocales reemplazadas: {nuevo_texto}")
    except TypeError:
        return print("Debes ingresar un texto")

reemplazar_letras("Ya no es así, me dejaste morir (perdón por existir)")