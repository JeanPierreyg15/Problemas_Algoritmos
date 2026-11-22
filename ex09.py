"""
Realizar un algoritmo que funcione como un cajero automático, es decir, dada una cantidad de dinero, muestre la cantidad de billetes mínimo que se necesita por cada tipo de billete (10, 20, 50, 100, 200 soles) para cubrir la demanda.
Considerar validar que el dinero a retirar sea mayor a 0 y solo permita múltiplos de 10. Por ejemplo:

Cantidad de dinero: 130
Cantidad de billetes:
Billetes de 100: 1
Billetes de 20: 1
Billetes de 10: 1

"""

def billetes_por_tipo(total):
    try:
        float(total)
        billetes = [200,100,50,20,10]
        resultado = {}

        if (total<=0):
            return print("El total de dinero debe ser un numero positivo y mayor a 0")

        if (total%10!=0):
            return print("El total debe ser multiplo de 10")

        restante = total

        for billete in billetes:
            cantidad = restante // billete
            restante %= billete
            if cantidad>0 :
                resultado[billete] = cantidad
            
        
        print(f"Cantidad de dinero: {total}")
        print(f"Cantidad de billetes:")

        for billete,cantidad in resultado.items():
            print(f"Billetes de {billete} : {cantidad}")

    except ValueError:
        return print("Debes ingresar numeros")
    except TypeError:
        return print("No puedes ingresar numeros en cadenas")

billetes_por_tipo(80)

'''
Revisión:

* ¿Cómo se simplificaría la solución usando un diccionario?
'''