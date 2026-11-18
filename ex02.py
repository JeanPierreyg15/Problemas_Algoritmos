"""
Crear un algoritmo que multiplique 2 números sin usar el operador de multiplicación. Por ejemplo:

Multiplicando: 5
Multiplicador: 10

Producto: 50

"""

def crear_multiplicador(multiplicando,multiplicador):
    respuesta=0
    try:
        float(multiplicando)
        float(multiplicador)
        multiplicador_positivo = positivo_o_negativo(multiplicador)
        if(not multiplicador_positivo):
            multiplicador *= (-1)
        
        for index in range(1,multiplicador+1):
            respuesta += multiplicando
            index +=1
    except TypeError:
        return print("Debe ingresar un numero")
    
    return print(f"Multiplicando: {multiplicando}\n",
                    f"Multiplicador: {multiplicador if multiplicador_positivo else multiplicador*(-1)}\n",
                    f"Respuesta: {respuesta if multiplicador_positivo else respuesta*(-1)}")

def positivo_o_negativo(numero):
    if numero<0 :
        return False
    return True

crear_multiplicador(-9,-4)

'''
Revisión:

* No ofusquemos los errores de la entrada (ejm: número negativos) porque no favorece la UX (user experience).
'''