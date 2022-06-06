#import child classes
from Human import Human
from Art_Intel import Art_intel
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
        self.name = 'Rock, Paper, Scizzors, Lizard, Spock'
        self.p1 = None
        self.p2 = None
        pass

    def run_game(self):
        self.greeting()
        self.who_plays()
        is_done = False
        while is_done == False:
            self.round_winner()
            self.play_again()
            pass

    def rounds(self):
        self.p1_turn = self.p1.choose_move()
        self.p2_turn = self.p2.choose_move()

    def round_winner(self):
        for round in self.rounds():
            if self.p1_turn == self.p2_turn:
                print("It's a tie!")
            elif self.p1_turn == '':
                ''
        pass

    def announce_winner(self):
        pass

    def greeting(self):
        print(f'''
********************************************************************************************
    Welcome to {self.name}!
    Here you will find the best of the best and maybe find if you are among them.
    The rules are simple:
        ''')
        {time.sleep(2)}
        print('''
    Rock beats Scizzors;
    Scizzors beat Paper:
    Paper beats Rock;
    Rock beats Lizard;
    Lizard beats Spock;
        ''')
        {time.sleep(2)}
        print('''
    Spock beats Scizzors;
    Scizzors beat Lizard;
    Lizard beats Paper;
    Paper beats Spock;
    Spock beats Rock.
        ''')
        {time.sleep(2)}
        print('''
    Winner is best out of 3 rounds.
    ......................... Good luck ;) ..........................
********************************************************************************************        
        ''')
        {time.sleep(3)}    

    def ending(self):
        print(f'Thank you for playing {self.name} with us! {time.sleep(.6)}Come again!')
        pass

    def play_again(self):
        user_input = input(f'Would you like to play {self.name} again? (y/n) ')
        if user_input == 'n':
            self.ending()
            is_done = True
            quit()
        return is_done

    def who_plays(self):
        is_correct = False
        
        while is_correct == False:
            self.players = input('How many human players dare to play? (Choose 0, 1, or 2) ')

            if self.players == '0':
                self.p1 = Art_intel('Arty')
                self.p2 = Art_intel('Atticus')
                is_correct = True
            elif self.players == '1':
                self.p1 = Human(input('What is your name? '))
                self.p2 = Art_intel('A1 Sauce')
                is_correct = True
            elif self.players == '2':
                self.p1 = Human(input('What is your name? '))
                self.p2 = Human(input('What is your name? '))
                is_correct = True
            else:
                print(f'{self.players} was not an option.')
                time.sleep(1)
