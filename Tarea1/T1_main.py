# DESCRIPCION:  Main de la Tarea 1 - Juego piedra, papel o tijeras
# AUTHOR:       Félix Armenta Aguiñaga - IECA PADTS 3

import random
from paqueteT1.moduloT1 import validacion

# Opcion con ciclo for en main
if __name__ == '__main__':
    opciones = ("Piedra", "Papel", "Tijera")
    print("\nBIENVENIDO A PIEDRA, PAPEL O TIJERA")

    for contador in range(5, 0, -1):
        print(f"\t\tJuego {6-contador} de 5")
        print("[1] Piedra - [2] Papel - [3] Tijera")
        print("Presiona [X] para elegir tu opcion:", end=" ")

        seleccionUsuario = input()

        random.seed()
        seleccionPC = random.randint(1,3)

        print(f"Usuario: {opciones[int(seleccionUsuario)-1]} \n\tVS \nPC: {opciones[seleccionPC-1]}")

        if (int(seleccionUsuario) != seleccionPC):
            validacion(int(seleccionUsuario), seleccionPC)
        else:
            print("EMPATE!\n")
