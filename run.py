import random
def create_board(size):
    """
    Create the game board
    """
    return [["~"] * size for i in range(size)]

def print_board(board):
    """
    Print the current game board
    """
    for row in board:
        print(" ".join(row))

def place_ships(board, size):
    """
    Place ships randomly on the game board
    """
    ship_row = random.randint(0, size - 1)
    ship_col = random.randint(0, size - 1)
    return ship_row, ship_col

def get_user_guess(size):
    """
    Get the user to input their guess
    """
    while True:
        try:
            guess_row = int(input(f"Guess Row (0-{size-1}): "))
            guess_col = int(input(f"Guess Column (0-{size-1}): )"))
            if 0 <= guess_row < size and 0 <= guess_col < size:
                return guess_row, guess_col
            else: print(f"You must enter values between 0 and {size-1}")
        except ValueError:
            print("Invalid input, you must enter an integer")

