import random
def create_bpard(size):
    return [["~"] * size for i in range(size)]

def print_board(board):
    for row in board:
        print(" ".join(row))