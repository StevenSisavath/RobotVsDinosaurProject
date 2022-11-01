from robot import Robot
import random
class Fleet:

    def __init__(self):
        self.scrappy = Robot('Scrappy')
        self.rusty = Robot('Rusty')
        self.dayta = Robot('Dayta')
        self.fleet = [self.scrappy, self.rusty, self.dayta]