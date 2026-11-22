"""
Crear una función que, dado un texto, retorne su acrónimo (todo en mayúsculas). Por ejemplo:

Texto: “My Chemical Romance”

Acrónimo: “MCR”

"""

def crear_acronimo(texto):
    try:
        lista  = texto.strip().title().split(" ")
        acronimo = ""
        for palabras in lista:
            acronimo = acronimo + palabras[0]

        print(f"El acronimo de {texto} es {acronimo}")
    except AttributeError:
        return print("Debe ingresar una cadena de texto")


crear_acronimo("My Chemical Romance")

'''
Revisión:

* Falta validar textos no vacíos.

Psdt:
Buena banda jeje
'''