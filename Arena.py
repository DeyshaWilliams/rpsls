#import child classes
from Human import Human
from Art_Intel import Art_intel
import random
import time
#greet user
#ask about players
#utilize classes to carry out each round (3)
#game cont until someone wins or the thrid round is complete
#be sure to use the .pause function
#once a winner is found, they are announced
#announce the end of the game
#ask user if they want to play again
#if yes, repeat the whole game
#if no, print sign off

class arena:
    def __init__(self):
        self.name = ''
        self.who_plays()
        pass

    def run_game(self):
        pass
        

    def greeting(self):
        pass

    def ending(self):
        pass

    def play_again(self):
        pass

    def who_plays(self):
        is_correct = False
        
        while is_correct == False:
            self.players = input('How many human players dare to play? (Choose 0, 1, or 2) ')
            
            if self.players == '0':
                self.a1 = Art_intel('Arty')
                self.a2 = Art_intel('Atticus')
                is_correct = True
            elif self.players == '1':
                self.human = Human(input('What is your name? '))
                self.ai = Art_intel('A1 Sauce')
                is_correct = True
            elif self.players == '2':
                self.h1 = Human(input('What is your name? '))
                self.h2 = Human(input('What is your name? '))
                is_correct = True
            else:
                print(f'{self.players} was not an option.')
                time.sleep(1)
