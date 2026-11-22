"""
Crear un función que dado un texto ingresado, retorne un texto cifrado como secuencia de asteriscos que sigan el patrón del texto. Por ejemplo:

Texto: “Cuando no es como debería ser”

Texto cifrado: “****** ** ** **** ****** ***”

"""

def cifrar_texto(texto):
    try:
        if not texto.strip():
            return print("No puede ingresar un texto vacio")
        # Código muerto
        texto_sin_espaciado = texto.strip()
        texto_cifrado = ""
        for letra in texto:
            if letra == " ":
                texto_cifrado += letra
            else:
                texto_cifrado += "*"

        print(texto_cifrado)
    except AttributeError:
        return print("Debe ingresar un texto")

cifrar_texto("Cuando no es como deberia ser")


'''
Revisión:

* Falta validar textos no vacíos.
'''