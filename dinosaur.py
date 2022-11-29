import random
class Dinosaur:


    def __init__ (self):
        self.name = "Carl"
        self.health = 100
        self.attack_power_list = [3,15,25]

    def attack (self, opponent:object):
        attack = random.choice (self.attack_power_list)
        opponent.health -= attack
        print (f'Dino attack happened leaving opponent with {opponent.health}')