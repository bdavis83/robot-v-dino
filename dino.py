#(10 points): As a developer, I want a Dinosaur to have a name, health, and attack power.
from dinoweapon import DinoWeapon

class Dinosaur:
    def __init__ (self, name, dino_type_str):
        self.name = name
        self.dino_type = dino_type_str
        self.health = 100
        self.attack_list = []
    

    def raptor (self):
        name = "Raptor"
        dino_type = 'Velociraptor'
        attack_list = [DinoWeapon.raptor_claw(), DinoWeapon.tail(), DinoWeapon.bite]
        

    def t_rex (self):
        name = "T-rex"
        dino_type = "Taranasaurus Rex"
        attack_list = [DinoWeapon.trex_chomp (), DinoWeapon.tail (), DinoWeapon.bite()]


    def dragon_dino (self):
        name = "Draco"
        dino_type = "Dragon"
        attack_list = [DinoWeapon.tail(), DinoWeapon.bite(), DinoWeapon.fire_ball ()]

    def create_attacke (self):
        attack
        
        