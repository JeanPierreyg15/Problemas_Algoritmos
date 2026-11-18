"""
Realizar un algoritmo que dado el precio de un producto y el dinero que tienes para comprarlo, muestre cuánto de cambio te corresponde.
Considerar validar que el dinero que tienes para comprarlo sea mayor o igual al precio del producto.
Por ejemplo:

Precio: S/. 8.40
Mi dinero: S/. 10.00

Cambio: S/. 1.60

"""

def dar_vuelto(mi_dinero,precio):
    try:
        float(mi_dinero)
        float(precio)
        if (mi_dinero<0):
            return print("Debe ingresar numeros positivos")

        if(precio<0):
            return print("Debe ingresar numeros positivos")

        if (precio>mi_dinero):
            return print("No tienes suficiente dinero para comprar este artículo")

        vuelto = mi_dinero - precio
        print(f"Precio: S/.{precio}")
        print(f"Mi dinero: S/.{mi_dinero}")
        print(f"Cambio: S/.{vuelto}")
    except ValueError:
        return print("Debe ingresar numeros")

dar_vuelto(mi_dinero=10,precio=12)