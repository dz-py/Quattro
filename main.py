from board import Board
from player import Player
from ai_player import RandomPlayer, AIPlayer
from game import connect_four

# Create players
p1 = Player('X')
p2 = AIPlayer('O', 'RANDOM', 3)

# Start the game
connect_four(p1, p2)