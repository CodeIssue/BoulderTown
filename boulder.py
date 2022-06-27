import random
from classes import *


class Boulder:
    def __init__(self, v:V, rs_skill_level):
        assert isinstance(v, V), "wrong type"
        # assert type(rs_skill_level) == int

        self.num_of_moves = random.randint(2, 20)
        self.boulder_v = v
        self.boulder_type = random.choice(list(Terrain))
        self.moves = [_Move(self.boulder_v, rs_skill_level) for _ in range(self.num_of_moves)]

    def __repr__(self):
        res = f"Number of Moves : {self.num_of_moves}\n"
        res += f"V: {self.boulder_v.name}\n"
        res += f"Terrain: {self.boulder_type.name}\n"
        return res

    def inspect(self):
        for move in self.moves:
            print(move)



class _Move:
    def __init__(self, v:V, rs_skill_level:int):
        self.strength_r = v.value * 10 + random.randint(-rs_skill_level, rs_skill_level)
        self.balance_r = v.value * 10 + random.randint(-rs_skill_level, rs_skill_level)
        self.foot_r = v.value * 10 + random.randint(-rs_skill_level, rs_skill_level)

    def __repr__(self):
        res = f"Strength : {self.strength_r}\n"
        res += f"Balance : {self.balance_r}\n"
        res += f"Foot : {self.foot_r}\n"
        return res