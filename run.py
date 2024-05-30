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
    size = len(board)
    print("  " + " ".join(str(i) for i in range(size)))
    for idx, row in enumerate(board):
        print(f"{idx} " + " ".join(row))


def place_ships(board, size, num_ships):
    """
    Place ships randomly on the game board
    """
    ships = []
    while len(ships) < num_ships:
        ship_row = random.randint(0, size - 1)
        ship_col = random.randint(0, size - 1)
        if (ship_row, ship_col) not in ships:
            ships.append((ship_row, ship_col))
    return ships


def get_user_guess(size):
    """
    Get the user to input their guess
    """
    while True:
        try:
            guess_row = int(input(f"Guess Row (0-{size-1}): "))
            if 0 <= guess_row < size:
                break
            else:
                print(f"Row must be between 0 and {size-1}")
        except ValueError:
            print("Invalid input, you must enter an integer")

    while True:
        try:
            guess_col = int(input(f"Guess Column (0-{size-1}): "))
            if 0 <= guess_col < size:
                break
            else:
                print(f"Column must be between 0 and {size-1}")
        except ValueError:
            print("Invalid input, you must enter an integer")

    return guess_row, guess_col


def check_guess(guess_row, guess_col, ships):
    """
    Check user's guess to see if they hit a battleship
    """
    if (guess_row, guess_col) in ships:
        print('You hit a battleship!\n')
        ships.remove((guess_row, guess_col))
        return True
    else:
        print("You didn't hit a battleship.\n")
        return False


def update_board(board, guess_row, guess_col, hit):
    """
    Update the board according to the user's guesses
    """
    if hit:
        board[guess_row][guess_col] = 'X'
    else:
        board[guess_row][guess_col] = ' '


def is_game_over(ships):
    """
    Check if all battleships have been sunk meaning game is over
    """
    return len(ships) == 0


def get_board_size():
    """
    Ask the user to input the size of the board for the game, with constraints.
    """
    while True:
        try:
            size = int(input("Enter the board size (e.g., 8 for 8x8, "
                             "maximum 10): "))
            if 1 <= size <= 10:
                return size
            else:
                print("Board size must be an integer between 1 and 10.")
        except ValueError:
            print("Invalid input, you must enter a positive integer.")


def get_num_ships(size):
    """
    Ask the user how many ships they want to try to sink
    """
    while True:
        try:
            num_ships = int(input("Enter the number of ships you wish to find "
                                  "(e.g., 6): "))
            if 0 < num_ships < size * size:
                return num_ships
            else:
                print(f"Number of ships must be a positive integer less than "
                      f"{size * size}.")
        except ValueError:
            print("Invalid input, you must enter a positive integer.")


def play_game():
    """
    This function initializes and manages the game of Battleships.
    """
    print("Let's play Battleships!\n"
          "Guess a row and column number\n"
          "to find and sink the battleships!\n")
    size = get_board_size()
    num_ships = get_num_ships(size)
    max_guesses = size * 3
    board = create_board(size)
    ships = place_ships(board, size, num_ships)
    guesses = 0
    game_over = False

    while not game_over and guesses < max_guesses:
        print_board(board)
        print(f"Ships remaining: {len(ships)}")
        guess_row, guess_col = get_user_guess(size)
        hit = check_guess(guess_row, guess_col, ships)
        update_board(board, guess_row, guess_col, hit)
        guesses += 1
        game_over = is_game_over(ships)
        print(f"Guesses remaining: {max_guesses - guesses}")
    print_board(board)
    if game_over:
        print('Game over! All battleships have been sunk!')
    else:
        print('Game over! You ran out of guesses!')

    play_again = input("Would you like to play again? "
                       "(yes/no): ").strip().lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing!")


if __name__ == '__main__':
    play_game()
