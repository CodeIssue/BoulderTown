from enum import Enum, unique

# V1-15
@unique
class V(Enum):
    V1 = 1
    V2 = 2
    V3 = 3
    V4 = 4
    V5 = 5
    V6 = 6
    V7 = 7
    V8 = 8
    V9 = 9
    V10 = 10
    V11 = 11
    V12 = 12
    V13 = 13
    V14 = 14
    V15 = 15

# Basic Stats eines Kletterers.
@unique
class BasicStats(Enum):
    FINGER_STRENGTH = 0
    STRENGTH = 1
    BALANCE = 2
    AGILITY = 3
    FOOTWORK = 4
    PRECISION = 5


# Skills die ein Kletterer erlernen kann -> hier sammelt er Erfahrung
@unique
class Skills(Enum):
    SLAB_BALANCE = 1
    ROOF = 2
    FLAG = 3
    BACKFLAG = 4
    KNEEBAR = 5
    BATHANG = 6 
    

# Wand-typ -> Modifikatoren für Technik
@unique
class Terrain(Enum):
    SLAB = 1
    VERTICAL = 2
    SLIGHT_OVERHANG = 3
    OVERHANG = 4
    ROOF = 5