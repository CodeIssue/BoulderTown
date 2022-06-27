"""
Alle Funktionen zum Spieler werden definiert.

Player
- stats
- skills
- klettern

"""
from classes import *

class Player:
    def __init__(self):
        self.strength = 10
        self.balance = 10
        self.foot_technique = 10
        self.fatigue = 0
    
    def __repr__(self):
        return f"""STR: {self.strength}
BLC: {self.balance}
FTT: {self.foot_technique}
FATIGUE: {self.fatigue}"""

    # def climb(self, boulder:_Boulder):
    #     for (number, move) in enumerate(boulder.moves): 
    #         chance_strength = 0.95 + (self.strength - move.strength_r)/100
    #         chance_balance = 0.95 + (self.balance - move.balance_r)/100
    #         chance_foot = 0.95 + (self.foot_technique - move.foot_r)/100

    #         if chance_strength < 1:
    #             if random.random() > chance_strength:
    #                 print(f"failed in move {number} on str")
    #                 self.fatigue += 5
    #                 return False
    #             else: # chance of learning?
    #                 self.fatigue += 1
    #                 if random.random() > chance_strength - 0.05:
    #                     print("got 1 str")
    #                     self.strength += 1

    #         if chance_balance < 1:
    #             if random.random() > chance_balance:
    #                 print(f"failed in move {number} on balance")
    #                 self.fatigue += 5
    #                 return False
    #             else:
    #                 self.fatigue += 1
    #                 if random.random() > chance_balance - 0.05:
    #                     print("got 1 balance")


    #         if chance_foot < 1:
    #             if random.random() > chance_foot:
    #                 print(f"failed in move {number} on foot")
    #                 self.fatigue += 5
    #                 return False
    #             else:
    #                 self.fatigue += 1
    #                 if random.random() > chance_foot - 0.05:
    #                     print("got 1 footwork")
    #                     self.foot_technique += 1
            
        

        print(f"climb passed! gz")
        return True # -> passed


