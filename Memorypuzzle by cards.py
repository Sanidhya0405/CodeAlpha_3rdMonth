import random
import time

def create_board(size):
    """Create a shuffled board with pairs of cards."""
    num_pairs = size * size // 2
    cards = list(range(1, num_pairs + 1)) * 2
    random.shuffle(cards)
    return [cards[i:i + size] for i in range(0, len(cards), size)]

def display_board(board, revealed):
    """Display the current state of the board."""
    for i, row in enumerate(board):
        for j, card in enumerate(row):
            if revealed[i][j]:
                print(card, end=' ')
            else:
                print('X', end=' ')
        print()

def get_coordinates(size):
    """Get valid coordinates from the player."""
    while True:
        try:
            x, y = map(int, input("Enter coordinates (row col): ").split())
            if 0 <= x < size and 0 <= y < size:
                return x, y
            else:
                print("Coordinates out of bounds. Try again.")
        except ValueError:
            print("Invalid input. Enter two integers separated by a space.")

def check_match(board, revealed, coord1, coord2):
    """Check if the two coordinates are a match."""
    x1, y1 = coord1
    x2, y2 = coord2
    if board[x1][y1] == board[x2][y2]:
        revealed[x1][y1] = True
        revealed[x2][y2] = True
        return True
    return False

def all_revealed(revealed):
    """Check if all cards have been revealed."""
    return all(all(row) for row in revealed)

def memory_puzzle(size, time_limit):
    """Main function to play the memory puzzle game."""
    board = create_board(size)
    revealed = [[False] * size for _ in range(size)]
    start_time = time.time()

    while True:
        display_board(board, revealed)
        if all_revealed(revealed):
            print("Congratulations! You've matched all pairs!")
            break
        if time.time() - start_time > time_limit:
            print("Time's up! Game over.")
            break
        print("Choose two cards to flip.")
        coord1 = get_coordinates(size)
        coord2 = get_coordinates(size)
        if coord1 == coord2:
            print("You chose the same card. Try again.")
            continue
        if check_match(board, revealed, coord1, coord2):
            print("It's a match!")
        else:
            print("Not a match. Try again.")

# Play the game with a 4x4 board and a 60-second time limit
memory_puzzle(4, 60)
