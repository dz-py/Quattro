class Board:
    """ a data type for a Connect Four board with arbitrary dimensions """   
    def __init__(self, height, width):
        """ constructor that initializes the board dimensions """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string representation of the board """
        s = ''
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'
        
        s += '-' * (2 * self.width + 1) + '\n'
        s += ' '
        for i in range(self.width):
            s += str(i % 10) + ' '
        s += '\n'
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker to the column """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        row = 0
        while self.slots[row][col] == ' ':
            if row >= (self.height - 1):
                row += 1
                break
            row += 1
        self.slots[row - 1][col] = checker

    def reset(self):
        """ reset the Board object """
        self.slots = [[' '] * self.width for row in range(self.height)]
        
    def can_add_to(self, col):
        """ returns True if the column can accept a checker """
        if col >= 0 and col < self.width:
            return self.slots[0][col] == ' '
        return False
        
    def is_full(self):
        """ returns True if the board is completely full """
        return not any(self.can_add_to(i) for i in range(self.width))

    def remove_checker(self, col):
        """ removes the top checker from column """
        row = 0
        while row < self.height and self.slots[row][col] == ' ':
            row += 1
            if row >= (self.height - 1):
                break
        self.slots[row][col] = ' '

    def _check_win_pattern(self, checker, positions):
        """ helper method to check if a set of positions contains a win """
        return all(self.slots[r][c] == checker for r, c in positions)

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win """
        for row in range(self.height):
            for col in range(self.width - 3):
                positions = [(row, col + i) for i in range(4)]
                if self._check_win_pattern(checker, positions):
                    return True
        return False
    
    def is_vertical_win(self, checker):
        """ Checks for a vertical win """
        for row in range(self.height - 3):
            for col in range(self.width):
                positions = [(row + i, col) for i in range(4)]
                if self._check_win_pattern(checker, positions):
                    return True
        return False
        
    def is_down_diagonal_win(self, checker):
        """ Checks for a diagonal win (down-right) """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                positions = [(row + i, col + i) for i in range(4)]
                if self._check_win_pattern(checker, positions):
                    return True
        return False
    
    def is_up_diagonal_win(self, checker):
        """ Checks for a diagonal win (up-right) """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                positions = [(row - i, col + i) for i in range(4)]
                if self._check_win_pattern(checker, positions):
                    return True
        return False
        
    def is_win_for(self, checker):
        """ returns True if there is a win on the board """
        assert(checker == 'X' or checker == 'O')
        return (self.is_horizontal_win(checker) or
                self.is_vertical_win(checker) or
                self.is_down_diagonal_win(checker) or
                self.is_up_diagonal_win(checker))
