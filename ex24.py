"""
Crear una función que identifique cuántos subtextos hay en un texto con una longitud determinada por el usuario. Por ejemplo:

Texto: “Hace tiempo atrás te aseguro que tú eras mi huracán”
Longitud de los subtextos: 4

Cantidad de subtextos con la longitud: 2
"""

def contar_subtexto(texto,longitud):
    try:
        int(longitud)

        if not texto.strip():
            return print("No puede ingresar un texto vacio")

        if longitud<=0:
            return print("Debes ingresar un numero mayor a 0 para la longitud")
        
        texto_lista = texto.strip().split()
        contador_subtextos = 0

        for palabra in texto_lista:
            if len(palabra)==longitud:
                contador_subtextos += 1

        print(f"Texto : {texto}")
        print(f"Longitud de los subtextos: {longitud}")
        print(f"Cantidad de subtextos con la longitud: {contador_subtextos}")
    except AttributeError:
        return print("Debes ingresar un texto")
    except ValueError:
        return print("Debes ingresar un numero entero para la longitud")

contar_subtexto("Hace tiempo atrás te aseguro que tú eras mi huracán",4)

'''
Revisión:

* Falta validar textos no vacíos.
'''