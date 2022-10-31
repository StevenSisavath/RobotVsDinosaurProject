from weapon import Weapon
import random
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = random.choice(weapon_options)

    def attack(self, dinosaur):
        health = dinosaur - self.active_weapon.attack_power
        if health <= 0:
            health = 0
        return health

lightbringer = Weapon('Lightbringer', 30)
excalibur = Weapon('Excalibur', 40)
harpe = Weapon('Harpe', 20)
weapon_options = [lightbringer, excalibur, harpe]