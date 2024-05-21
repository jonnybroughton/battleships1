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
            guess_col = int(input(f"Guess Column (0-{size-1}): "))
            if 0 <= guess_row < size and 0 <= guess_col < size:
                return guess_row, guess_col
            else: 
                print(f"You must enter values between 0 and {size-1}")
        except ValueError:
            print("Invalid input, you must enter an integer")

def check_guess(guess_row,guess_col,ship_row,ship_col):
    """
    Check user's guess to see if they hit a battleship
    """
    if guess_row == ship_row and guess_col == ship_col:
        print('You sunk the battleship!')
        return True
    else:
        print("You didn't hit a battleship")
        return False

def update_board(board, guess_row, guess_col, hit):
    """
    Update the board according to the user's guesses
    """
    if hit:
        board[guess_row][guess_col] = 'X'
    else:
        board[guess_row][guess_col] = '0'

def is_game_over(board):
    """
    Check if all battleships have been sunk meaning game is over
    """
    for row in board:
        if '~' in row:
            return False
    return True

def play_game():
    print("Let's play Battleships!\nGuess a row and column number\nto find a battleship to sink!")
    size = 8
    board = create_board(size)
    ship_row, ship_col = place_ships(board, size)
    game_over = False
    while not game_over:
        print_board(board)
        guess_row, guess_col = get_user_guess(size)
        hit = check_guess(guess_row,guess_col,ship_row,ship_col)
        update_board(board,guess_row,guess_col,hit)
        game_over = is_game_over(board)
    print('Game over!')
if __name__ == '__main__':
    play_game()