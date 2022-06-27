
import msvcrt
import os
import sys
from time import sleep


from typing import NamedTuple
from controller import Controller
from player import Player
from route_setter import RouteSetter

from wall import Wall


class Context(NamedTuple):
    player: Player
    main_route_setter: RouteSetter
    list_of_walls: list


def _main_menu(c):
    if c == b'N':
        print("Neues Spiel wird erstellt")
    elif c == b'\x1b':
        exit()
    else:
        print(f"{c} - diese Eingabe existiert nicht")


def print_slow(str):
    for c in str:
        print(c, end='', flush=True)
        sleep(0.05)

def press_enter():
    sys.stdout.flush()
    print("(ENTER ...)")
    passed = False
    while not passed:
        if msvcrt.getch() == b'\r':
            passed = True
    os.system('cls')

def start_game():
    os.system('cls')
    print_slow("Neues Spiel wird gestartet.\n")
    
    print_slow("Hallo! Wer bist du?\n")
    
    while True:
        try:
            p = controller.create_player()
            break
        except:
            print_slow("Der Name ist ungültig. Versuche es noch mal.\n")
            pass
    
    os.system('cls')
    print_slow(f"Hallo {p.name}\n")
    print_slow(f"Du bist zum ersten Mal in einer Boulderhalle. \n")
    print_slow(f"Mal schauen was auf dich zukommt... \n\n")

    press_enter()
    # Controller - Halle erstellen
    # Alle Wände mit Bouldern belegen
    print_slow(f"Ein Typ kommt auf dich zu.\nEr ist der Main-Route-Setter und hat gerade neue Boulder an die Wand gebracht")
    mrs = RouteSetter()                             # Main Route Setter

    print_slow(f"Die Halle hat 10 Wände, an jeder Wand sind 5-15 Boulder installiert.\n")
    list_of_walls = [Wall(id) for id in range(1,11)]     # 10 Leere Wände

    for (num, w) in enumerate(list_of_walls):
        # Installieren der Boulder
        controller.build_boulder(mrs, w)
        
        # Ausgabe
        print(f"Wand {num+1}:")
        print(w)
        print("\n")
    
    
    
    print_slow("Du siehst dich um...")
    
    press_enter()
    context = Context(p, mrs, list_of_walls)
    main_menu()

def main_menu():
    pass


if __name__ == "__main__":

    controller = Controller()

    while True:
        os.system('cls')
        print("Willkommen in BoulderTown!")
        print("Hast du Lust zu Klettern?")
        print()
        print("(Schift + N) - Neues Spiel")
        print("(Schift + L) - letzes Spiel laden")
        print("(BACKSLASH <--) - Spiel fortsetzen.")
        print("(ESC) - Spiel verlassen")

        c = msvcrt.getch()

        if c == b'N':
            start_game()
        elif c == b'\x1b':
            exit()
        elif c == b'\x08':
            # Spiel fortsetzen
            exit()
        else:
            print(f"{c} - diese Eingabe existiert nicht")
            msvcrt.getch()


# def main_menu():
#     print("Willkommen!")
#     print("Lust zu klettern?")
#     print("(N) - um ein neues Spiel zu beginnen.")
#     print("(ESC) - um das Spiel zu verlassen")

#     c = msvcrt.getch()
#     _switch_state(c)


# def create_new_game():
#     global context
#     print("Climber wird erstellt")
#     context.player = Player()
#     print("neue Halle wird gebaut")
#     context.wall = Wall()
#     print("Routesetter werden ausgebildet...")
#     main_route_setter = RouteSetter()
#     print("Boulder werden geschraubt")
#     main_route_setter.set_wall(context.wall)
#     # context.wall.boulders = [main_route_setter]

#     context.state = Menu.CHOOSE_BOULDERS


# def choose_boulders():
#     global context
#     print("Hallo.")
#     print(Wall)

#     _switch_state(msvcrt.getch())


# def _switch_state(c):
#     global context

#     if c == b'q' or c == b'\x1b':
#         print("exit")
#         context.state = Menu.EXIT
#     if c == b'N':
#         context.state = Menu.NEW_GAME
#     else:
#         print(f"falsche Eingabe : {c} ist nicht definiert")

# if __name__ == "__main__":
#     context.state = Menu.MAIN_MENU

#     while True:

#         if context.state == Menu.MAIN_MENU:
#             main_menu()

#         if context.state == Menu.NEW_GAME:
#             create_new_game()

#         if context.state == Menu.CHOOSE_BOULDERS:
#             choose_boulders()

#         if context.state == Menu.EXIT:
#             exit()
