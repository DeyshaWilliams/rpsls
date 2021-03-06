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
            if self.p1.wins == 2 or self.p2.wins == 2:
                self.announce_winner()
                self.play_again()

    def rounds(self):
        self.p1_turn = self.p1.choose_move()
        self.p2_turn = self.p2.choose_move()

    def round_winner(self):
        self.rounds()
        if self.p1_turn == self.p2_turn:
            print("It's a tie!")
        elif self.p1_turn == 'Rock' and self.p2_turn == 'Paper':
            print(f'Paper covers Rock! {self.p2.name} wins this round!')
            self.p2.wins += 1
        elif self.p1_turn == 'Rock' and self.p2_turn == 'Scizzors':
            print(f'Rock crushes Scizzors! {self.p1.name} wins this round!')
            self.p1.wins += 1
        elif self.p1_turn == 'Rock' and self.p2_turn == 'Lizard':
            print(f'Rock smashes Lizard! {self.p2.name} wins this round!')
            self.p2.wins += 1
        elif self.p1_turn == 'Rock' and self.p2_turn == 'Spock':
            print(f'Spock vaporizes Rock! {self.p2.name} wins this round!')
            self.p2.wins += 1
        elif self.p1_turn == 'Paper' and self.p2_turn == 'Scizzors':
            print(f'Scizzors cuts Paper! {self.p2.name} wins this round!')
            self.p2.wins += 1
        elif self.p1_turn == 'Paper' and self.p2_turn == 'Lizard':
            print(f'Lizard eats Paper! {self.p2.name} wins this round!')
            self.p2.wins += 1
        elif self.p1_turn == 'Paper' and self.p2_turn == 'Spock':
            print(f'Paper disproves Spock! {self.p1.name} wins this round!')
            self.p2.wins += 1
        elif self.p1_turn == 'Lizard' and self.p2_turn == 'Spock':
            print(f'Lizard poisons Spock! {self.p1.name} wins this round!')
            self.p1.wins += 1
        elif self.p1_turn == 'Lizard' and self.p2_turn == 'Scizzors':
            print(f'Scizzors decapitate Lizard! {self.p2.name} wins this round!')
            self.p2.wins += 1
        elif self.p1_turn == 'Spock' and self.p2_turn == 'Scizzors':
            print(f'Spock smashes Scizzors! {self.p1.name} wins this round!')
            self.p1.wins += 1
        elif self.p2_turn == 'Rock' and self.p1_turn == 'Paper':
            print(f'Paper covers Rock! {self.p1.name} wins this round!')
            self.p1.wins += 1
        elif self.p2_turn == 'Rock' and self.p1_turn == 'Scizzors':
            print(f'Rock crushes Scizzors! {self.p2.name} wins this round!')
            self.p2.wins += 1
        elif self.p2_turn == 'Rock' and self.p1_turn == 'Lizard':
            print(f'Rock smashes Lizard! {self.p1.name} wins this round!')
            self.p1.wins += 1
        elif self.p2_turn == 'Rock' and self.p1_turn == 'Spock':
            print(f'Spock vaporizes Rock! {self.p1.name} wins this round!')
            self.p1.wins += 1
        elif self.p2_turn == 'Paper' and self.p1_turn == 'Scizzors':
            print(f'Scizzors cuts Paper! {self.p1.name} wins this round!')
            self.p1.wins += 1
        elif self.p2_turn == 'Paper' and self.p1_turn == 'Lizard':
            print(f'Lizard eats Paper! {self.p1.name} wins this round!')
            self.p1.wins += 1
        elif self.p2_turn == 'Paper' and self.p1_turn == 'Spock':
            print(f'Paper disproves Spock! {self.p2.name} wins this round!')
            self.p2.wins += 1
        elif self.p2_turn == 'Lizard' and self.p1_turn == 'Spock':
            print(f'Lizard poisons Spock! {self.p2.name} wins this round!')
            self.p2.wins += 1
        else:
            print(f'Spock smashes Scizzors! {self.p2.name} wins this round!')
            self.p2.wins += 1
        time.sleep(1.5)

    def announce_winner(self):
        if self.p1.wins == 2:
            print(f'{self.p1.name} has won against {self.p2.name}!')
        else:
            print(f'{self.p2.name} has won against {self.p1.name}!')
        time.sleep(1.5)

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
        print(f'Thank you for playing {self.name} with us!')
        {time.sleep(.6)}
        print(f'Come again!')

    def play_again(self):
        user_input = input(f'Would you like to play {self.name} again? (y/n) ')
        if user_input == 'n':
            self.ending()
            quit()

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
