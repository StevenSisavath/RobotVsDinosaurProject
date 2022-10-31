from robot import Robot
class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        health = robot - self.attack_power
        if health <= 0:
            health = 0
        return health