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

caracter_inicial_final("    ")


'''
Revisión:

* Falta validar entradas con cadenas de solo espacios (hay que aplicar trim siempre en las entradas de texto para eliminar los espacios del inicio y final).
'''