import random

class Player:
    choices = {
        'p': 'paper',
        'r': 'rock',
        's': 'scissors'
    }

    def __init__(self):
        self.name = None
        self.score = 0
    
    def get_name(self):
        pass

    def next_move(self):
        pass


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()
        random.seed()

    def get_name(self):
        return 'Computer'

    def next_move(self):
        return random.choice(list(self.choices.keys()))


class HumanPlayer(Player):
    def get_name(self):
        return input('Enter your name: ')

    def _display_choices(self):
        for k, v in self.choices.items():
            print('{} - {}'.format(k, v))

    def next_move(self):
        self._display_choices()
        move = None
        while move not in list(self.choices.keys()):
            move = input('Choose next move: ')
        return move

class Game:
    winner_table = {
        ('p', 'r'): 0,
        ('p', 's'): 1,
        ('p', 'p'): None,
        ('r', 'r'): None,
        ('r', 's'): 0,
        ('r', 'p'): 1,
        ('s', 'r'): 1,
        ('s', 's'): None,
        ('s', 'p'): 0,
    }

    def __init__(self, num_of_rounds=5):
        self.players = [ComputerPlayer(), HumanPlayer()]
        self.num_of_rounds = num_of_rounds

    def start_game(self):
        for player in self.players:
            player.name = player.get_name()
    
    def get_game_winner(self):
        if self.players[0].score > self.players[1].score:
            return self.players[0]
        elif self.players[0].score < self.players[1].score:
            return self.players[1]
        else:
            return None

    def get_round_winner(self, choice0, choice1):
        return self.winner_table[(choice0, choice1)]

    def round(self):
        round_moves = []
        for player in self.players:
            print('{}, make your move.'.format(player.name))
            round_moves.append(player.next_move())
            print('DONE.')
            print('--')
        winner_idx = self.get_round_winner(*round_moves)
        if winner_idx is not None:
            winner = self.players[winner_idx]
            winner.score += 1
        else:
            winner = None
        return round_moves[0], round_moves[1], winner

    def run(self):
        print(20 * '=')
        print('NEW GAME')
        self.start_game()
        for round_number in range(self.num_of_rounds):
            print('ROUND {}'.format(round_number))
            choice0, choice1, round_winner = self.round()
            print('{}: {} - {}: {}'.format(self.players[0].name, Player.choices[choice0],
                                           self.players[1].name, Player.choices[choice1]))
            if round_winner is not None:
                print('{} won the round'.format(round_winner.name))
            else:
                print('Nobody won.')
            print(20 * '-')
        print('GAME OVER')
        winner = self.get_game_winner()
        if winner is not None:
            print('The WINNER is: {}'.format(winner.name))
        else:
            print("It's a draw")


if __name__ == '__main__':
    game = Game()
    game.run()
