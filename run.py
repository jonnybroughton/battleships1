import random
def create_bpard(size):
    return [["~"] * size for i in range(size)]

def print_board(board):
    for row in board:
        print(" ".join(row))

def place_ships(board, size):
    ship_row = random.randint(0, size - 1)
    ship_col = random.randint(0, size - 1)
    return ship_row, ship_col