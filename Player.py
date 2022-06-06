#Class defined by name and array of rpsls options
class Player:
    def __init__(self, passed_name):
        self.name = passed_name
        self.moves = ['Rock','Paper','Scizzors','Lizard','Spock']
        self.choice = ''
        self.wins = 0

    def choose_move(self):
        pass
    