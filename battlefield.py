from dinosaur import Dinosaur
from robot import Robot
from fleet import Fleet
from herd import Herd
import random
the_fleet = Fleet()
the_herd = Herd()
class Battlefield:
    
    def __init__(self):
        self.robot = random.choice(the_fleet.fleet)
        self.dinosaur = random.choice(the_herd.herd)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        self.remove_dino_and_robot()

    def display_welcome(self):
        print('''
Welcome to an epic battle of the ages!
Only one side can win!
''')

    def battle_phase(self):
        battling = True
        attack = ['tail whip', 'dino slash', 'head charge', 'stomp', 'claw cut']
        while battling:
            self.robot.health = self.dinosaur.attack(self.robot.health)
            print(f'''{self.dinosaur.name} hit {self.robot.name} with a {random.choice(attack)} for {self.dinosaur.attack_power} damage!
{self.robot.name} has {self.robot.health} health remaining!
            ''')
            self.dinosaur.health = self.robot.attack(self.dinosaur.health)
            print(f'''{self.robot.name} hit {self.dinosaur.name} with {self.robot.active_weapon.name} for {self.robot.active_weapon.attack_power} damage!
{self.dinosaur.name} has {self.dinosaur.health} health remaining!''')
            print('')
            if self.robot.health > 0 and self.dinosaur.health > 0:
                battling = True
            elif self.robot.health <= 0 or self.dinosaur.health <= 0:
                battling = False
                

    def display_winner(self):
        if self.robot.health <= 0 and self.dinosaur.health > 0:
            print(f'''{self.dinosaur.name} made {self.robot.name} extinct!
{self.dinosaur.name} is the Dino Champion!
''')
        elif self.dinosaur.health <= 0 and self.robot.health > 0:
            print(f'''{self.robot.name} made {self.dinosaur.name} extinct!
{self.robot.name} is the Robot Champion!
''')
        elif self.dinosaur.health <= 0 and self.robot.health <=0:
            print(f'''{self.robot.name} and {self.dinosaur.name} are both extinct!
It's a tie! Neither {self.robot.name} or {self.dinosaur.name} win!
''')
        
    def remove_dino_and_robot(self):
        the_fleet.fleet.remove(self.robot)
        the_herd.herd.remove(self.dinosaur)