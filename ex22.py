import random

"""
Crear un juego de piedra, papel o tijera, que dada una cantidad de partidas, se juegue con la computadora esa cantidad de veces y que al final muestre si fue Victoria, Derrota o Empate, según corresponda.

"""


def piedra_papel_tijera():
    seguir_jugando = True
    contador_victorias = 0
    contador_derrotas = 0
    contador_empate = 0
    while(seguir_jugando):
        opcion_jugador = input("Ingrese si elige piedra , papel o tijera: ")

        if (opcion_jugador.lower().strip() != "piedra" and opcion_jugador.lower().strip() != "tijera"
            and opcion_jugador.lower().strip() != "papel"):
            seguir_jugando = False
            print("Ingrese una opción correcta . Saliendo del juego")
            continue

        opcion_maquina = random.choice(["piedra","papel","tijera"])

        if opcion_jugador == "piedra":
            if opcion_maquina == "papel":
                contador_derrotas +=1
                print("PERDISTE")
            elif opcion_maquina == "tijera":
                contador_victorias +=1
                print("GANASTE")
            else:
                contador_empate +=1
                print("ES UN EMPATE")
        elif opcion_jugador == "papel":
            if opcion_maquina == "tijera":
                contador_derrotas +=1
                print("PERDISTE")
            elif opcion_maquina == "piedra":
                contador_victorias +=1
                print("GANASTE")
            else:
                contador_empate +=1
                print("ES UN EMPATE")
        else:
            if opcion_maquina == "piedra":
                contador_derrotas +=1
                print("PERDISTE")
            elif opcion_maquina == "papel":
                contador_victorias +=1
                print("GANASTE")
            else:
                contador_empate +=1
                print("ES UN EMPATE")

        continuar = input("Desea seguir jugando?(si/no): ")

        if (continuar.lower().strip()=="no"):
            seguir_jugando = False
            print("Saliendo del juego")
        elif (continuar.lower().strip()=="si"):
            print("Se continuara jugando")
        else:
            seguir_jugando = False
            print("Opción incorrecta . Saliendo del juego")

    print("CONTADOR FINAL:")
    print(f"Cantidad de victorias: {contador_victorias}")        
    print(f"Cantidad de derrotas: {contador_derrotas}")
    print(f"Cantidad de empates: {contador_empate}")

piedra_papel_tijera()

    