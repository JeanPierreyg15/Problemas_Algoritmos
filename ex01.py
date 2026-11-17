"""
Realizar una función que te devuelva la cantidad de vocales de un texto pasado como argumento. Por ejemplo:

Texto: “Algoritmo de la felicidad”
Cantidad de vocales: 10

"""

def contar_vocales(palabra):
    vocales="aeiouAEIOUáéíóúÁÉÍÓÚ"
    contador=0
    try:
        for letra in palabra:
            if letra in vocales:
                contador +=1
    except TypeError:
        print("Debe ingresar una palabra")
        return

    print(f"La palabra {palabra} tiene {contador} vocales")

contar_vocales(2)