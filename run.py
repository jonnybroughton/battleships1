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

