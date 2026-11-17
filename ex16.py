"""
Crear un algoritmo que, dado un texto, muestre el texto con cada una de las letras desplazada una posición en el alfabeto.
Considerar contar las ñ, y si es una z, debe reemplazarse por a.

Texto: “Donde entra el comercio, no entran las balas.”

Texto con letras desplazadas: “Epñef fñusb fm dpnfsdjp, mp flusbñ mbt cbmbt.”

"""

def desplazar_letras(texto):
    abc_min = "abcdefghijklnñopqrstuvwxyz"
    abc_may = "ABCDEFGHIJKLNÑOPQRSTUVWXYZ"

    palabra_nueva = ""

    for letra in texto:

        if letra in abc_min:
            palabra_nueva += abc_min[(abc_min.index(letra)+1)%len(abc_min)]

        elif letra in abc_may:
            palabra_nueva += abc_may[(abc_may.index(letra)+1)%len(abc_may)]

        else:
            palabra_nueva += letra

    print(palabra_nueva)

desplazar_letras("Donde entra el comercio, no entran las balas.")


