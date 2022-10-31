from weapon import Weapon
from dinosaur import Dinosaur
class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.ative_weapon = Weapon()

    def attack(self, dinosaur):
        health = dinosaur - self.active_weapon.attack_power
        print(f'The dinosaur has {health} health remaing!')
