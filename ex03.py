"""
Realizar un algoritmo que, dado un texto, lo devuelve en nomenclatura pascal case, es decir, que empiecen con mayúscula, que por cada espacio, su siguiente letra debería ser un mayúscula y todas las demás en minúsculas. 
Considerar solo letras del alfabeto A-Z y espacios (no ñ, ni tildes, etc).
Por ejemplo:

Texto: company rEpository
Texto en Pascal Case: CompanyRepository
"""

def pascal_case(texto):
    pascal = ""

    try:
        lista = texto.strip().split()
        for palabra in lista:
            palabra_limpia = ""

            for letra in palabra:

                if("A"<=letra<="Z" or "a"<=letra<="z"):
                    palabra_limpia = palabra_limpia + letra

            if palabra_limpia !="":
                primera_letra = palabra_limpia[0].upper()
                resto_palabra = palabra_limpia[1:].lower()
                pascal = primera_letra + resto_palabra

    except AttributeError:
        print("Debe ingresar un texto")
        return

    return print(pascal)

pascal_case('company rEpository')

'''
Revisión:

* ¿Cómo se haría sin el método title?
'''