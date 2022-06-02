#Child class of Player class
from Player import Player
import random
#Defines name and randomizes choices from array in parent class
class Art_intel(Player):
    def __init__(self, passed_name):
        super().__init__(passed_name)
        pass
    
