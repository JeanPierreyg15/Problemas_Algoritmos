"""
Crear un algoritmo que, dados dos vectores (x1, y2) y (x2, y2), determine su producto punto (|A|.|B| = (Ax1 * Ax2, Ay1 * Ay2). Por ejemplo:

Vector componente X1: 3
Vector componente Y1: 5
Vector componente X2: 6
Vector componente Y2: 2

Producto punto: (18, 10)
"""

def determinar_producto_punto(x1,y1,x2,y2):
    try:
        vector1=(x1,y1)
        vector2=(x2,y2)
        
        validar_numeros_vectores(vector1)
        validar_numeros_vectores(vector2)
        
            

        producto_punto = (vector1[0]*vector2[0],vector1[1]*vector2[1])

    except ValueError:
        return print("Error")
    return print(f"Vector componente x1: {x1}\n",
                f"Vector componente Y1: {y1}\n",
                f"Vector componente X2: {x2}\n",
                f"Vector componente Y2: {y2}\n",
                f"Producto punto: {producto_punto}")




def validar_numeros_vectores(vector):
    for coordenadas in vector:
        try:
            return float(coordenadas)
        except ValueError:                
            raise ValueError("Debe ingresar numeros")

determinar_producto_punto("a",5,6,2)