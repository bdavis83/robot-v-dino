class Bender:

    def __init__ (self):
        self.name = "Bender"
        self.hp = 170
        self.attack_list = []

        def attack(self, opponent: object):
        self.hp -= opponent.attack_list      #need to fill in
        opponent.hp -= self.attack_list [random.choice(self.attack_list)]