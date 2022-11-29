
from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    
    def __init__ (self):
        self.player_one = Dinosaur ()
        self.player_two = Robot ()
        pass



    def run_game (self):
        self.display_welcome ()
        self.print_opponents ()
        self.battle_phase ()
        self.display_winner ()
        pass



    def display_welcome (self):
        print ('\n Welcome to ROBO VS DINO, where past meets future!  Only one can win!\n')

    def print_opponents (self):
        print(f"\n Your oppoents are {self.player_one.name} and {self.player_two.name}!\n")

    
    def battle_phase (self):
        while self.player_one.health > 0 and self.player_two.health > 0:
            self.player_one.attack(self.player_two)
            if self.player_two.health > 0:
                self.player_two.attack(self.player_one)
            pass



    def display_winner (self):
        if self.player_one.health <0:
            print (f"\n{self.player_two.name} is the winner!\n")
        elif self.player_two.health <0:
            print (f"\n{self.player_two.name} is the winner!\n")
        pass
