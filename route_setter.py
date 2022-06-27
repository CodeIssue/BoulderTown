"""
Alles zum Routesetten wird definiert.

- routesetter

"""
from wall import *
from boulder import *

class RouteSetter:
    def __init__(self, skill_level = 5):
        self.skill = skill_level

    def set_wall(self, wall:Wall, v = V.V1):
        wall.boulders = [Boulder(V.V1, self.skill) for _ in wall.list_of_terrain]
