"""
Realizar un algoritmo que, dado un texto, muestre el caracter inicial y final.
Considerar validar que el texto no esté vacío ni con solo espacios. Por ejemplo:

Texto: “Vampires will never hurt you”

Caracter inicial: “V”
Caracter final: “u”

"""

def caracter_inicial_final(texto):
    if not texto:
        return print("Debe ingresar texto")

    print(f"Caracter inicial : {texto[0]}")
    print(f"Caracter final: {texto[len(texto)-1]}")

caracter_inicial_final("Vampires will never hurt you")