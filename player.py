"""
Alle Funktionen zum Spieler werden definiert.

Player
- stats
- skills
- klettern

"""
from classes import *

class Player:
    def __init__(self, name):
        assert len(name) > 2, "Die Eingabe ist zu kurz"
        assert len(name) < 20, "Die Eingabe ist zu lang"

        self.name = name
        self.energy = 100
        self.basic_attributes = dict()

        for stat in list(BasicStats):
            self.basic_attributes[stat.name] = 10


    def __repr__(self):
        res = f"Name: {self.name}\n"
        
        res = f"Energie: {self.energy}\n"

        res += f"Basic Attributes:\n\n"
        for key in self.basic_attributes:
            res += f"{key} : {self.basic_attributes[key]}\n"


        return res

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


