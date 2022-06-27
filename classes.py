from enum import Enum

# V1-16
class V(Enum):
    V1 = 1
    V2 = 2
    V3 = 3
    V4 = 4
    V5 = 5

# Basic Stats eines Kletterers.
class BasicStats(Enum):
    STRENGTH = 1
    BALANCE = 2
    AGILITY = 3
    FOOTWORK = 4
    PRECISION = 5
    FINGER_STRENGTH = 6


# Skills die ein Kletterer erlernen kann -> hier sammelt er Erfahrung
class Skills(Enum):
    SLAB_BALANCE = 1
    ROOF = 2
    FLAG = 3
    BACKFLAG = 4
    KNEEBAR = 5
    BATHANG = 6 
    

# Wand-typ -> Modifikatoren für Technik
class Terrain(Enum):
    SLAB = 1
    VERTICAL = 2
    SLIGHT_OVERHANG = 3
    OVERHANG = 4
    ROOF = 5