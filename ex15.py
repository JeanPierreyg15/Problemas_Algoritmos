"""
Realizar un algoritmo que dada una lista de números, devuelva su media armónica.
(promedio invertido)
Números: 5, 10, 8

Media armónica: 7.05

10, 11, 12

3/((1/11) + (1/12) + (1/13))

"""

def calcular_media_armonica(lista_numeros):
    try:
        denominador = 0
        for numero in lista_numeros:
            float(numero)
            if numero <= 0 :
                return "Solo se permiten numeros mayores a 0"
            denominador += (1/numero)

        numerador = len(lista_numeros)
        media_armonica = numerador / denominador

        print("Numeros: ",lista_numeros)
        print(f"Media Armonica: {round(media_armonica,2)} ")
    except ValueError:
        return print("Solo se pueden ingresar numeros en la lista")

lista = [5,10,8]
calcular_media_armonica(lista)
        