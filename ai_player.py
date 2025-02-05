import random
from player import Player

class RandomPlayer(Player):
    """ Computer player that chooses moves randomly """
    def __init__(self, checker):
        super().__init__(checker, name="Random AI")
        
    def next_move(self, board):
        self.num_moves += 1
        available_cols = [col for col in range(board.width) 
                         if board.can_add_to(col)]
        return random.choice(available_cols)

class AIPlayer(Player):
    """ Intelligent computer player that looks ahead """
    def __init__(self, checker, tiebreak, lookahead):
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak in ['LEFT', 'RIGHT', 'RANDOM'])
        assert(lookahead >= 0)
        super().__init__(checker, name="AI")
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    def __repr__(self):
        return f'Player: {self.name} ({self.checker})'
        
    def max_score_column(self, scores):
        """ returns the index of the column with the maximum score """
        max_score = max(scores)
        indices = [i for i, score in enumerate(scores) if score == max_score]
        
        if self.tiebreak == 'LEFT':
            return indices[0]
        if self.tiebreak == 'RIGHT':
            return indices[-1]
        return random.choice(indices)
        
    def scores_for(self, board):
        """ determines scores for each possible move """
        scores = [50] * board.width
        
        for col in range(board.width):
            if not board.can_add_to(col):
                scores[col] = -1
            elif board.is_win_for(self.checker):
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), 
                                  self.tiebreak, 
                                  self.lookahead - 1)
                opp_scores = opponent.scores_for(board)
                
                if max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 0:
                    scores[col] = 100
                else:
                    scores[col] = 50
                    
                board.remove_checker(col)
        return scores
    
    def next_move(self, board):
        """ returns the best move based on score analysis """
        self.num_moves += 1
        scores = self.scores_for(board)
        return self.max_score_column(scores)

