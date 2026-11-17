"""
Realizar un algoritmo que dado un número, te muestre su tabla de multiplicar, del 1 al 12. Por ejemplo:

Número: 4
Tabla de multiplicar:
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
…
4 x 12 = 48

"""

def tabla_multiplicar(numero):

    try:
        int(numero)
        if numero<=0:
            return print("Debe ingresar un numero mayor a 0 ")
        for index in range(1,13):
            print(f" {numero} x {index} = {numero*index}")
    except ValueError:
        return print("Debes ingresar un numero")

tabla_multiplicar(6)