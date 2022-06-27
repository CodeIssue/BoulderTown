## der Nutzer, der Anweisungen erfüllt.
## Controller wählt zum Beispiel Wand und Route-Setter, um einen Boulder zu bauen oder abzubauen.

import sys
from player import Player
from wall import *
from route_setter import *

class Controller:

    @staticmethod
    def build_boulder(rs:RouteSetter, wall:Wall):
        wall.boulders = [Boulder(random.choice(list(V)[0:rs.max_skill+1]), rs.skill)]


    @staticmethod
    def create_player():
        sys.stdout.flush()
        name = input("Name : ")
        return Player(name)

