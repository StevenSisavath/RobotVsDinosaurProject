from weapon import Weapon
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Lightbringer', 30)

    def attack(self, dinosaur):
        health = dinosaur - self.active_weapon.attack_power
        return health