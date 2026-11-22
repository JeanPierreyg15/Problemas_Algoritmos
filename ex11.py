"""
Realizar un algoritmo que dado 2 textos, verifique si el segundo es un anagrama del primero, es decir si tienen las mismas letras independientemente del orden. Por ejemplo:

Primera palabra: “amor”
Segunda palabra: “roma”

"""

def detectar_anagrama(primera_palabra,segunda_palabra):
    try:
        es_anagrama = 1

        p1 = primera_palabra.strip().lower()
        p2 = segunda_palabra.strip().lower()

        if not p1:
            return print("La primera palabra no puede estar vacía")

        if not p2:
            return print("La segunda palabra no puede estar vacía")
        
        if (len(p1)!=len(p2)):
            return print("No son anagramas")

        lista_segunda_palabra = list(p2)
        for i in primera_palabra.lower().strip():
            if i in lista_segunda_palabra:
                es_anagrama *=1
                lista_segunda_palabra.remove(i)
            else:
                es_anagrama*=0

        if es_anagrama:
            return print(f"{segunda_palabra} es anagrama de {primera_palabra}")
        else:
            return print("No son anagramas")
    except AttributeError:
        return print("Debes ingresar solamente textos")

detectar_anagrama("aab","abb")

'''
Revisión:

* Falta validar entradas de cadena vacía.
* Está fallando con:
    - armar, rama (falta 1 letra)
    - armar, ramax (falta 1 letra y sobra 1 letra)
'''
