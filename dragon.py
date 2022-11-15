from dinoweapon import DinoWeapon
import random

class Dragon:
    def __init__ (self):
        self.name = "Dragon"
        self.hp = 170
        self.attack_list = [DinoWeapon.fire_ball(), DinoWeapon.tail(), DinoWeapon.bite ()]
    
    
    def attack(self, opponent: object):
        opponent.hp -= self.attack_list [random.choice((len(self.attack_list)))]
