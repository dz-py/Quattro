from board import Board

def process_move(player, board):
    """ processes a single move """
    print(f"{player}'s turn")

    if player.name == 'AI':
        print('AI is thinking...')
    
    col = player.next_move(board)
    board.add_checker(player.checker, col)
    print()
    print(board)
    
    if board.is_win_for(player.checker):
        print(f'{player} wins in {player.num_moves} moves.')
        print('Congratulations!')
        return True
    elif board.is_full():
        print("It's a tie!")
        return True
    return False

def connect_four(p1, p2):
    """ Plays a game of Connect Four between two players """
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('Need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(p1, board):
            return board
        if process_move(p2, board):
            return board