#import child classes
from Human import human
from Art_Intel import art_intel
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
        pass

    def run_game(self):
        pass

    def greeting(self):
        pass

    def ending(self):
        pass

    def play_again(self):
        pass

    def human_plays(self):
        self.human = human

    def ai_plays(self):
        self.ai = art_intel

    def who_plays(self):
        self.players = input('How many human players dare to play? (Choose 0, 1, or 2)')
        return self.players
