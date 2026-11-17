"""
Crear una función que, dado un vector (x, y), devuelva su magnitud (RAIZ CUADRADA DE X^2 + Y^2). Por ejemplo:

Vector componente X: 3
Vector componente Y: 4

Resultado: 25

"""

def calcular_magnitud(x=0,y=0):
    try:
        float(x)
        float(y)
    except ValueError:
        return print("Debes ingresar numeros")

    magnitud = ((x)**2 + (y)**2)**(1/2)

    return print(f"Vector componente X : {x} \n",
                f"Vector componente Y : {y} \n",
                f"Resultado : {magnitud}")

calcular_magnitud(3,4)