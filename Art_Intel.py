#Child class of Player class
from Player import Player
import random
import time
#Defines name and randomizes choices from array in parent class
class Art_intel(Player):
    def __init__(self, passed_name):
        super().__init__(passed_name)

    def choose_move(self):
        self.chosen = random.choice(self.moves)
        print(f'{self.name} has chosen {self.chosen}!')
        time.sleep(1.5)
