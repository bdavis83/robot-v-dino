from weapon import Weapon
import random

class Robot:
    def __init__ (self):
        self.name = "Bender"
        self.health = 100
        self.active_weapon_list = []
        self.make_weapons()
        
        

    def attack(self, opponent: object):
        weapon = random.choice(self.active_weapon_list)
        opponent.health -= weapon.attack_power
        print(f'{self.name} is attacking {opponent.name} with {weapon.name} leaving {opponent.name} with {opponent.health} health left.')
        pass

    def make_weapons(self):
        weapon_one = Weapon("Metal Fist", 3)
        self.active_weapon_list.append(weapon_one)
        weapon_two = Weapon("bazooka", 25)
        self.active_weapon_list.append(weapon_two)
        weapon_three = Weapon("sword", 15)
        self.active_weapon_list.append(weapon_three)




    