"""
Crear un algoritmo que, dado un texto, muestre aquel texto sin vocales. Por ejemplo:

Texto: “Per aspera ad astra”

Texto sin vocales: “Pr spr d str”

"""

def mostrar_texto_sin_vocales(texto):
    try:
        if not texto.strip():
            return print("No puede ingresar cadenas vacías")
        
        vocales="aeiouáéíóú"
        nuevo_texto = ""

        for letra in texto:
            if(letra.lower() in vocales ):
                continue
            nuevo_texto = nuevo_texto + letra

        print(f"Texto: {texto} \n",
                f"Texto sin vocales: {nuevo_texto}")
    except TypeError:
        return print("Debes ingresar un texto")

mostrar_texto_sin_vocales("Per aspera ad astra")

'''
Revisión:

* Usar uppercase o lowercase en lugar de duplicarlas para minúsculas y mayúsculas.
* Falta validar entradas de cadena vacía.
'''