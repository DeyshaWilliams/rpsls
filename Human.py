#Child class of Player class
#defines user name and user input for array in parent class
from Player import Player
import time

class Human(Player):
    def __init__(self, passed_name):
        super().__init__(passed_name)

    def choose_move(self):
        is_range = False
        while is_range == False:
            print('Choose your move!')
            for move in self.moves:
                print(f'Press {self.moves.index(move) + 1} for {move}.')
                time.sleep(.7)
            user_input = int(input(': '))
            if user_input == 0:
                print('Invalid choice')
            else:
                try:
                    self.chosen = self.moves[user_input -1]
                    print(f'{self.name} has chosen {self.chosen}.')
                    is_range = True
                except IndexError as error:
                    print('Invalid choice...', error)
                    time.sleep(1)
        time.sleep(1.5)    
