"""
Crear una función que dado un número n, sume los números naturales desde 1 a n. Por ejemplo:

Número n: 10

Suma de 1 a n: 1 + 2 + 3… + 10 = 55

"""

def suma_numeros_consecutivos_formula(numero_final):
    try:
        int(numero_final)
        if(numero_final<=0):
            return print("Debes ingresar un numero entero y positivo")
        resultado = (numero_final*(numero_final+1))/2
    except TypeError:
        return print("Debes ingresar un numero entero")
    return print(f"Suma de 1 a {numero_final} : {resultado}")

suma_numeros_consecutivos_formula(10)

'''
Revisión:

* Recuerda que son números naturales (deben salir como enteros no como decimales).
'''