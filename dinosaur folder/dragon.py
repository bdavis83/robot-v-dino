from dinoweapon import DinoWeapon
import random

class Dragon:
    def __init__ (self):
        self.name = "Dragon"
        self.hp = 170
        self.attack_list = [DinoWeapon.fire_ball(), DinoWeapon.tail(), DinoWeapon.bite ()]
    
    
    def attack(self, opponent: object):
        self.hp -= opponent.attack_list      #need to fill in
        opponent.hp -= self.attack_list [random.choice(self.attack_list)]
