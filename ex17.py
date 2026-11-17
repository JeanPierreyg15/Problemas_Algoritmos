"""
Si un desarrollador de software gana 10 soles por hora. Crea un algoritmo que dado un número de días devuelva la cantidad de dinero que le corresponde al desarrollador.
Considerando que trabaja 8 horas diarias.

Número de días: 15
Cantidad de dinero: 1200

"""

def calcular_sueldo_mensual(dias,sueldo_por_hora):

    try:
        int(dias)
        float(sueldo_por_hora)

        cantidad_horas = dias * 8

        sueldo_final = cantidad_horas * sueldo_por_hora

        print(f"El sueldo final es : {sueldo_final}")

    except ValueError:
        return print("Debe ingresar numeros")

calcular_sueldo_mensual(15, 10)