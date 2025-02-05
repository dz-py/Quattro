from board import Board
from player import Player
from ai_player import RandomPlayer, AIPlayer
from game import connect_four

def get_difficulty():
    while True:
        print("\nSelect AI difficulty:")
        print("1. Easy (1 move lookahead)")
        print("2. Medium (3 moves lookahead)")
        print("3. Hard (5 moves lookahead)")
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                return 1
            elif choice == 2:
                return 3
            elif choice == 3:
                return 5
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Welcome to Connect Four!")
    print("------------------------")    
    while True:
        try:
            difficulty = get_difficulty()
            p1 = Player('X')
            p2 = AIPlayer('O', 'RANDOM', difficulty)
            break
        except ValueError:
            print("Please enter a valid number.")

    connect_four(p1, p2)

if __name__ == "__main__":
    main()