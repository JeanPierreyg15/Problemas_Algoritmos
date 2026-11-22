"""
Realizar un algoritmo que dada una lista de números, se determine cuál es el número menor y cuál es el mayor. Por ejemplo:

Números: 10, 15, 5, 35

Mínimo: 5
Máximo: 35

"""

def calcular_minimo_maximo(lista_numeros):
    try:
        for numero in lista_numeros:
            float(numero)

        lista_ordenada = sorted(lista_numeros)

        print(lista_ordenada)

        numero_menor = lista_ordenada[0]
        numero_mayor = lista_ordenada[len(lista_ordenada)-1]

        print(f"El numero menor es : {numero_menor} ")
        print(f"El numero mayor es : {numero_mayor}")
    except ValueError:
        return print("La lista solo puede contener numeros")

lista = [12,67,89,-323,3434,90,10]
calcular_minimo_maximo(lista)

'''
Revisión:

* Es más práctico usar min() y max() para obtener el mínimo y máximo de la lista, en lugar de ordenar toda la lista.
'''

"""
Nota : No hice cambios , lo hice con las listas solo por intentar hacerlo diferente del min y max xd
"""