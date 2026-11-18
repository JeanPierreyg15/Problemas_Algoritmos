"""
Hacer una función que devuelva el reverso de una cadena de texto. Por ejemplo:

Texto: “Arroz con leche”
Texto al revés: “ehcel noc zorrA”

"""

def invertir_cadena(texto):
    cadena_invertida = ""
    try:
        for letra in texto:
            cadena_invertida = letra + cadena_invertida
        print(cadena_invertida)
    except TypeError:
        return print("Debe ingresar un texto")

    
invertir_cadena("")

'''
Revisión:

* Falta validar entradas de cadena vacía.
'''