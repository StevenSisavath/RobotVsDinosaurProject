from dinosaur import Dinosaur
import random
class Herd:

    def __init__(self):
        self.smallzilla = Dinosaur('Smallzilla', 20)
        self.deno = Dinosaur('Deno', 30)
        self.spyke = Dinosaur('Spyke', 40)
        self.herd = [self.smallzilla, self.deno, self.spyke]