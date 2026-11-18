"""
Crear una función que dado un número en una base de 2 a 9, lo convierta a base 10. Por ejemplo:

Número: 102
Base: 3

Número en base 10: 11

"""

def convertir_base_10(numero,base):
    try:
        int(numero)
        int(base)
        numero_base_diez = 0

        if(numero<0):
            return "El numero debe ser positivo"
        if(base<0):
            return "La base debe ser positivo"

        i=0
        numero_string = str(numero)
        for index in numero_string:
            numero_base_diez+= int(index)*(base**(len(numero_string)-(i+1)))
            i+=1

        print(f"Número: {numero}")
        print(f"Base: {base}")
        print(f"Número en base 10: {numero_base_diez}")

    except ValueError:
        return print("Debes ingresar numeros")

convertir_base_10(102,3)
