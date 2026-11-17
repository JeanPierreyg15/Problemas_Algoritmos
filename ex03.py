"""
Realizar un algoritmo que, dado un texto, lo devuelve en nomenclatura pascal case, es decir, que empiecen con mayúscula, que por cada espacio, su siguiente letra debería ser un mayúscula y todas las demás en minúsculas. 
Considerar solo letras del alfabeto A-Z y espacios (no ñ, ni tildes, etc).
Por ejemplo:

Texto: company rEpository
Texto en Pascal Case: CompanyRepository
"""

def pascal_case(texto):
    try:
        lista = texto.title().strip().split()
    except AttributeError:
        print("Debe ingresar un texto")
        return
    pascal = ""
    for palabra in lista:
        pascal += palabra

    return print(pascal)

pascal_case(4)