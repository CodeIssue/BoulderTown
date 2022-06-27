"""
Alles zum Routesetten wird definiert.

- routesetter

"""
from wall import *
from boulder import *

class RouteSetter:
    def __init__(self, skill_level = 5, max_skill = 8):
        self.skill = skill_level        # skill als Route-setter.
        self.max_skill = max_skill      # kann routen bis zu dem Skill schrauben
