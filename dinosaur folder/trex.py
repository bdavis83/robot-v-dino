from dinoweapon import DinoWeapon
import random

class Trex:
   
    def __init__ (self):
        self.name = "T-Rex"
        self.hp = 150
        self.attack_list = [DinoWeapon.trex_chomp(), DinoWeapon.tail(), DinoWeapon.bite ()]

    def attack(self, opponent: object):
        self.hp -= opponent.attack_list      #need to fill in
        opponent.hp -= self.attack_list [random.choice(self.attack_list)]
