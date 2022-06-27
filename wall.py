import random
from boulder import Boulder

from classes import *
"""
alles über die Wand wird definiert.

Wall
- Space : Anzahl der Plätze
- liste der Terrains: 1-5
- Liste der Boulder
"""


class Wall:
    def __init__(self, id, space = random.randint(5,15)):
        self.id = id
        self.space = space
        self.terrain = random.choice(list(Terrain))
        self.boulders = []

    def __repr__(self) -> str:
        res = f"Wand-ID : {self.id}\n"
        res += f"Maximale Anzahl Boulder : {self.space}\n"
        res += f"Art der Wand : {self.terrain.name}\n"

        return res

