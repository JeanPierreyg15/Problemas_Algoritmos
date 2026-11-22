"""
Crear un algoritmo que, dado un texto, muestre el texto con cada una de las letras desplazada una posición en el alfabeto.
Considerar contar las ñ, y si es una z, debe reemplazarse por a.

Texto: “Donde entra el comercio, no entran las balas.”

Texto con letras desplazadas: “Epñef fñusb fm dpnfsdjp, mp flusbñ mbt cbmbt.”

"""

def desplazar_letras(texto):

    try:
        if not texto.strip():
            return print("No puede ingresar cadenas vacías")
        
        abc_min = "abcdefghijklmnñopqrstuvwxyz"
        abc_may = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

        palabra_nueva = ""

        for letra in texto:

            if letra in abc_min:
                palabra_nueva += reemplazar_letra(abc_min,letra)

            elif letra in abc_may:
                palabra_nueva += reemplazar_letra(abc_may,letra)

            else:
                palabra_nueva += letra

        print(palabra_nueva)
    except TypeError:
        print("Solo puede ingresar texto")

def reemplazar_letra(lista,letra):
    indice_letra = lista.index(letra)
    letra_siguiente = indice_letra + 1
    reemplazo = lista[(letra_siguiente)%len(lista)]

    return reemplazo



desplazar_letras("   ")

'''
Revisión:

* Ilegibilidad: El código se hace difícil de ententeder al haber muchas operaciones en una sola línea (línea 20 y 23).
* Duplicidad de código: En las líneas mencionadas se hace la misma operación solo que con diferente array, así que perfectamente puede extraerse a una función.
* Faltan validaciones de la entrada.
'''
