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

        if multiplicador<=0:
            return print("El multiplicador debe ser mayor a 0")
        
        
        for index in range(1,multiplicador+1):
            respuesta += multiplicando
            index +=1
    except TypeError:
        return print("Debe ingresar un numero")
    
    return print(f"Multiplicando: {multiplicando}\n",
                    f"Multiplicador: {multiplicador}\n",
                    f"Respuesta: {respuesta}")



crear_multiplicador(-9,-4)

'''
Revisión:

* No ofusquemos los errores de la entrada (ejm: número negativos) porque no favorece la UX (user experience).
'''