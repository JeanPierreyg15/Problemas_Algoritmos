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

        if (total<=0):
            return print("El total de dinero debe ser un numero positivo y mayor a 0")

        if (total%10!=0):
            return print("El total debe ser multiplo de 10")

        billetes_200 = total // 200
        billetes_100 = (total % 200) // 100
        billetes_50 =  ((total % 200) % 100) // 50
        billetes_20 = (((total % 200) % 100) % 50)//20
        billetes_10 = ((((total % 200) % 100) %  50 ) % 20 ) // 10

        print(f"Cantidad de dinero: {total}")
        print(f"Cantidad de billetes:")
        if billetes_200>0:    
            print(f"Billetes de 200: {billetes_200}")
        if billetes_100>0:    
            print(f"Billetes de 100: {billetes_100}")
        if billetes_50>0:    
            print(f"Billetes de 50: {billetes_50}")
        if billetes_20>0:    
            print(f"Billetes de 20: {billetes_20}")
        if billetes_10>0:    
            print(f"Billetes de 10: {billetes_10}")

    except ValueError:
        return print("Debes ingresar numeros")

billetes_por_tipo(80)

'''
Revisión:

* ¿Cómo se simplificaría la solución usando un diccionario?
'''