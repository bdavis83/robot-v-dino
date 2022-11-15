from roboweapon import RoboWeapons
import random

class Droid:

    def __init__ (self):
        self.name = "Droid"
        self.hp = 170
        self.attack_list = [RoboWeapons.metal_fist(), RoboWeapons.laser(), RoboWeapons.droid_slap()]

    def attack(self, opponent: object):
        opponent.hp -= self.attack_list [random.choice(self.attack_list [len])]