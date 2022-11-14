from dinoweapon import DinoWeapon
import random

class Raptor:

    def __init__ (self):
        self.name = "Raptor"
        self.hp = 100
        self.attack_list = [DinoWeapon.raptor_claw(), DinoWeapon.tail(), DinoWeapon.bite]

    
    def attack(self, opponent: object):
        self.hp -= opponent.attack_list      #need to fill in
        opponent.hp -= self.attack_list [random.choice(self.attack_list)]
