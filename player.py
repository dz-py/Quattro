class Player:
    """ Base class for Quattro players """
    def __init__(self, checker, name="Human"):
        """
        Initialize a player
        Args:
            checker: 'X' or 'O'
            name: Display name for the player
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        self.name = name
        
    def __repr__(self):
        return f'Player: {self.name} ({self.checker})'
    
    def opponent_checker(self):
        """ returns the opponent's checker """
        return 'O' if self.checker == 'X' else 'X'
        
    def next_move(self, board):
        """ gets the next move from the player """
        self.num_moves += 1
        while True:
            try:
                col = int(input('Enter a column: '))
                if board.can_add_to(col):
                    return col
                print('Invalid column, try again!')
            except ValueError:
                print('Please enter a valid number!')
