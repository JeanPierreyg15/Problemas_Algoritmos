"""
Crear un algoritmo que muestre un texto definido por el usuario con un caracter eliminado que el usuario también haya proporcionado.
Considerar validar que sea solo un caracter el ingresado. Por ejemplo:

Texto: “Eyes set to kill”
Caracter: “e”

Texto sin el caracter: “ys st to kill”

"""


def eliminar_caracter(texto,caracter):
    try:
        if(not texto.strip()):
            return print("No puede ingresar un texto vacio")

        if not caracter.strip():
            return print("No puede ingresar un caracter vacio")
        
        if (len(caracter)>1):
            return print("El caracter a eliminar solo puede tener un caracter")
        
        nuevo_palabra = ""

        for letra in texto:
            if letra.lower()==caracter.lower():
                continue
            nuevo_palabra += letra

        print(f"Texto: {texto}")
        print(f"Caracter: {caracter}")
        print(f"Texto sin el caracter: {nuevo_palabra}")
    except TypeError:
        return print("Debe ingresar texto")
    except AttributeError:
        return print("Debe ingresar texto")

eliminar_caracter("Eyes set to kill","e")

'''
Revisión:

* Falta validar textos no vacíos.
'''