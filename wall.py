import random

from classes import *
"""
alles über die Wand wird definiert.

Wall
- Space : Anzahl der Plätze
- liste der Terrains: 1-5
- Liste der Boulder
"""


class Wall:
    def __init__(self, v = V.V1):
        self.space = 10
        self.list_of_terrain = [random.choice(list(Terrain)) for _ in range(self.space)]
        self.boulders = []


