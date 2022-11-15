from roboweapon import RoboWeapons
import random

class Bender:

    def __init__ (self):
        self.name = "Bender"
        self.hp = 170
        self.attack_list = [RoboWeapons.metal_fist(), RoboWeapons.laser(), RoboWeapons.bend()]

        def attack(self, opponent: object):
        opponent.hp -= self.attack_list [random.choice(self.attack_list)]