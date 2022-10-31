from dinosaur import Dinosaur
from robot import Robot
class Battlefield:
    
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()

    def run_game(self):
        Battlefield.display_welcome()
        Battlefield.battle_phase()
        Battlefield.display_winner

    def display_welcome(self):
        print('''
Welcome to an epic battle of the ages!
Only one side can win!
''')

    def battle_phase(self):
        battling = True
        while battling:
            self.dinosaur.attack(Robot.health)
            self.robot.attack(Dinosaur.health)
            if Robot.health <= 0 or Dinosaur.health <= 0:
                battling = False

    def display_winner(self):
        if self.robot.health <= 0 and self.dinosaur.health > 0:
            print(f'''
{self.dinosaur.name} made {self.robot.name} extinct!
{self.dinosaur.name} is the winner!
''')
        elif self.dinosaur.health <= 0 and self.robot.health > 0:
            print(f'''
{self.robot.name} made {self.dinosaur.name} extinct!
{self.robot.name} is the winner!
''')
        elif self.dinosaur.health <= 0 and self.robot.health <=0:
            print(f'''
{self.robot.name} and {self.dinosaur.name} are both extinct!
It's a tie! Neither {self.robot.name} or {self.dinosaur.name} win!
''')


# battlefield_one = Battlefield()
# battlefield_two = Battlefield()
# battlefield_three = Battlefield()