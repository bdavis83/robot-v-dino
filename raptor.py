from dinoweapon import DinoWeapon
import random

class Raptor:

    def __init__ (self):
        self.name = "Raptor"
        self.hp = 100
        self.attack_list = [DinoWeapon.raptor_claw(), DinoWeapon.tail(), DinoWeapon.bite()]

    
    def attack(self, opponent: object):
        opponent.hp -= self.attack_list opponent-= self.attack_list [random.choice((len(self.attack_list)))]
