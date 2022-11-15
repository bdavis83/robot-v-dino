from roboweapon import RoboWeapons
import random

class Roomba:

    def __init__ (self):
        self.name = "Roomba"
        self.attack_list = [RoboWeapons.metal_fist(), RoboWeapons.laser(), RoboWeapons.vacuum()]

    def attack(self, opponent: object):
        opponent.hp -= self.attack_list [random.choice(self.attack_list [len])]