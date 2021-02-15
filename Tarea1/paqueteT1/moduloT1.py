# DESCRIPCION:  Modulo para validacion - Juego piedra, papel o tijeras
# AUTHOR:       Félix Armenta Aguiñaga - IECA PADTS 3

def validacion(usuario, pc):
    """
    :param usuario: Recibe un entero del 1 al 3 - [1] Piedra, [2] Papel, [3] Tijera, Otro valor se descarta

    :param pc: Recibe un entero del 1 al 3 - [1] Piedra, [2] Papel, [3] Tijera
    """
    if (usuario == 1):
        if (pc == 2):
            print("PERDISTE! U_u\n")
        else:
            print("GANASTE! :)\n")
    elif (usuario == 2):
        if (pc == 3):
            print("PERDISTE! U_u\n")
        else:
            print("GANASTE! :)\n")
    elif (usuario == 3):
        if (pc == 1):
            print("PERDISTE! U_u\n")
        else:
            print("GANASTE! :)\n")
    else:
        print("SELECCION NO VALIDA\n")


# Opcion con while y entrada del usuario en el modulo
if __name__ == '__main__':
    from random import randint
    from random import seed
    continuar = True
    opciones = ("Piedra", "Papel", "Tijera")
    print("\nBIENVENIDO A PIEDRA, PAPEL O TIJERA")

    while(continuar):
        print("[1] Piedra - [2] Papel - [3] Tijera")
        print("Presiona [X] para elegir tu opcion:", end=" ")

        seleccionUsuario = input()

        seed()
        seleccionPC = randint(1,3)

        print(f"Usuario: {opciones[int(seleccionUsuario)-1]} \n\tVS \nPC: {opciones[seleccionPC-1]}")

        if (int(seleccionUsuario) != seleccionPC):
            validacion(int(seleccionUsuario), seleccionPC)
        else:
            print("EMPATE!\n")

        print("Deseas continuar jugando?")
        print("Presiona [s] para continuar:", end=" ")
        continuar_input = input()
        if (continuar_input == 's'):
            continuar = True
        else:
            continuar = False

        print("\n")
