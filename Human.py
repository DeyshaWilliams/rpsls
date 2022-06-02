#Child class of Player class
#defines user name and user input for array in parent class
from Player import Player

class Human(Player):
    def __init__(self, passed_name):
        super().__init__(passed_name)
    pass
