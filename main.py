import msvcrt


from typing import NamedTuple
from menu import *
from route import *
from wall import *
from route_setter import *
from player import *

context = NamedTuple( "Context",
    state = Menu,
    player = Player,
    wall = Wall
)
    


def main_menu():
    print("Willkommen!")
    print("Lust zu klettern?")
    print("(N) - um ein neues Spiel zu beginnen.")
    print("(ESC) - um das Spiel zu verlassen")

    c = msvcrt.getch()
    _switch_state(c)


def create_new_game():
    global context
    print("Climber wird erstellt")
    context.player = Player()
    print("neue Halle wird gebaut")
    context.wall = Wall()
    print("Routesetter werden ausgebildet...")
    main_route_setter = RouteSetter()
    print("Boulder werden geschraubt")
    main_route_setter.set_wall(context.wall)
    # context.wall.boulders = [main_route_setter]
    
    context.state = Menu.CHOOSE_BOULDERS




def choose_boulders():
    global context
    print("Hallo.")
    print(Wall)

    _switch_state(msvcrt.getch())


def _switch_state(c):
    global context

    if c == b'q' or c == b'\x1b':
        print("exit")
        context.state = Menu.EXIT
    if c == b'N':
        context.state = Menu.NEW_GAME
    else:
        print(f"falsche Eingabe : {c} ist nicht definiert")

if __name__ == "__main__":
    context.state = Menu.MAIN_MENU

    while True:
        
        if context.state == Menu.MAIN_MENU:
            main_menu()

        if context.state == Menu.NEW_GAME:
            create_new_game()

        if context.state == Menu.CHOOSE_BOULDERS:
            choose_boulders()
            
        if context.state == Menu.EXIT:
            exit()