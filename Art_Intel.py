#Child class of Player class
from Player import player
import random
#Defines name and randomizes choices from array in parent class
class art_intel(player):
    def __init__(self, passed_name):
        super().__init__(passed_name)
        passed_name = random.choice(list_of_names)
        list_of_names = ['A1 Sauce', 'Arty', 'Atticus', 'Atlas']
        pass

       
    
