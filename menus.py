from abc import ABC, abstractmethod
import msvcrt
import os
from time import sleep

from enum import Enum, unique

from player import Player
from wall import Wall


# @unique
# class Menu(Enum):
#     MAIN_MENU = 0
#     GAME_MENU = 1
#     CHAR_MENU = 2
#     SKILL_MENU = 3
#     WALL_MENU = 4
#     BOULDER_MENU = 5
#     NEW_GAME = 6


class GameState(ABC):
    """Abstract State for Game."""
    _player:Player
    _wall:Wall

    def __init__(self, player:Player = None, wall:Wall = None) -> None:
        self._player = player
        self._wall = wall

    @abstractmethod
    def next(self):
        """Next State"""

    @abstractmethod
    def show(self):
        """super().print_slow Information (Menu)"""

    @staticmethod
    def print_slow(s:str):
        """super().print_slow slow and center"""

        new_s = ""
        for line in s.splitlines():
            new_s += line.center(79) + "\n"

        for c in new_s:
            print(c, end = '', flush=True)
            # sleep(0.03)
        

class Main_Menu(GameState):
    _player = None
    _wall = None

    def __init__(self, player = None, wall = None):
        super(Main_Menu, self).__init__(player, wall)

    def next(self):
        c = msvcrt.getch()
        if c == b'N':
            super().print_slow("next state should be New Game")
            return New_Game_Menu(self._player, self._wall)
        if c == b'\x1b':
            exit()
        if c == b'\r' and self._player is not None:
            return Game_Menu(self._player, self._wall)
        super().print_slow(f"{c} - ungültiger Input.")
        return self.next()

    def show(self):
        os.system('cls')
        super().print_slow("(N) - Neues Spiel")
        super().print_slow("(ENTER) - Spiel fortsetzen")
        super().print_slow("(ESC) - Spiel verlassen")



class New_Game_Menu(GameState):

    def __init__(self, player = None, wall = None):
        super(New_Game_Menu, self).__init__(player, wall)

    def next(self):
        return Game_Menu(self._player, self._wall)

    def show(self):
        os.system('cls')
        super().print_slow("Neues Spiel wird gestartet..")
        super().print_slow("Hallo und Willkommen in der Boulderhalle.")
        super().print_slow("wie heißt du?")
        
        while True:
            name = input("Name : ")
            self._player = Player(name)
            self._wall = Wall()
            super().print_slow(f"Hallo {self._player.name}")
            super().print_slow("Ist der Name richtig? (ENTER)")
            if msvcrt.getch() == b'\r':
                break


class Game_Menu(GameState):

    def __init__(self, player, wall):
        super(Game_Menu, self).__init__(player, wall)

    def show(self):
        os.system('cls')
        super().print_slow(f"Hallo {self._player.name}!")
        super().print_slow(f"Du hast noch {self._player.energy} Energie.")
        super().print_slow("-"*79)
        super().print_slow(f"(C) - Char Stats")
        super().print_slow(f"Skills")
        super().print_slow(f"Wand anschauen")
        super().print_slow("-"*79)
        super().print_slow("(BACKSPACE, ESC) - Main Menu")


    def next(self):
        c = msvcrt.getch()
        if c == b'c':
            return Char_Menu(self._player, self._wall)
        if c == b'\x1b' or c == b'\x08':
            return Main_Menu(self._player, self._wall)
        return self
        

class Char_Menu(GameState):
    
    def __init__(self, player, wall):
        super(Char_Menu, self).__init__(player, wall)
    

    def show(self):
        os.system('cls')
        super().print_slow(str(self._player))
        super().print_slow("-"*79)
        super().print_slow("(BACKSPACE, ESC) - Main Menu")

    def next(self):
        c = msvcrt.getch()

        if c == b'\x08' or b'\x1b':
            return Game_Menu(self._player, self._wall)


