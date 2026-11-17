"""
Realizar un algoritmo que dado 2 textos, verifique si el segundo es un anagrama del primero, es decir si tienen las mismas letras independientemente del orden. Por ejemplo:

Primera palabra: “amor”
Segunda palabra: “roma”

"""

def detectar_anagrama(primera_palabra,segunda_palabra):
    try:
        es_anagrama = 1

        for i in primera_palabra.lower():
            if i in segunda_palabra.lower():
                es_anagrama *=1
            else:
                es_anagrama*=0

        if es_anagrama:
            return print(f"{segunda_palabra} es anagrama de {primera_palabra}")
        else:
            return print("No son anagramas")
    except AttributeError:
        return print("Debes ingresar solamente textos")

detectar_anagrama("Croacia",4)