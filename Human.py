#Child class of Player class
#defines user name and user input for array in parent class
from Player import player

class human(player):
    def __init__(self, passed_name):
        super().__init__(passed_name)
        passed_name = input('What is your name? ')
    pass
