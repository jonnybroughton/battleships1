import random


def create_board(size):
    """
    Create the game board
    """
    return [["~"] * size for _ in range(size)]


def print_board(board, title=""):
    """
    Print the current game board
    """
    size = len(board)
    print(title)
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

def computer_guess(size, previous_guesses):
    """
    Generate a computer's guess
    """
    while True:
        guess_row = random.randint(0, size - 1)
        guess_col = random.randint(0, size - 1)
        if (guess_row, guess_col) not in previous_guesses:
            previous_guesses.append((guess_row, guess_col))
            break
    return guess_row, guess_col

def check_guess(guess_row, guess_col, ships, player=""):
    """
    Check guess to see if it hits a battleship
    """
    if (guess_row, guess_col) in ships:
        if player:
            print(f'{player} hit a battleship!\n')
        ships.remove((guess_row, guess_col))
        return True
    else:
        if player:
            print(f"{player} didn't hit a battleship.\n")
        return False


def update_board(board, guess_row, guess_col, hit):
    """
    Update the board according to the guesses
    """
    if hit:
        board[guess_row][guess_col] = 'X'
    else:
        board[guess_row][guess_col] = '*'


def is_game_over(ships):
    """
    Check if all battleships have been sunk meaning game is over
    """
    return len(ships) == 0


def get_board_size():
    """
    Ask the user to input the size of the board for the game,
    with a minimum of 2 and maximum of 10
    """
    while True:
        try:
            size = int(input("Enter the board size (minimum 2, maximum 10): "))
            if 2 <= size <= 10:
                return size
            else:
                print("Board size must be an integer between 2 and 10.")
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
    Initialize and manage the game of Battleships
    """
    print("Let's play Battleships!\n"
          "Guess a row and column number\n"
          "to find and sink the battleships!\n")
    size = get_board_size()
    num_ships = get_num_ships(size)
    max_guesses = size * 3
    user_board = create_board(size)
    computer_board = create_board(size)
    user_ships = place_ships(user_board, size, num_ships)
    computer_ships = place_ships(computer_board, size, num_ships)
    guesses_remaining = max_guesses
    user_game_over = False

    while not user_game_over and guesses_remaining > 0:

        print_board(user_board, title="User Grid:")
        print_board(computer_board, title="Computer Grid:")

        guess_row, guess_col = get_user_guess(size)
        user_hit = check_guess(guess_row, guess_col, computer_ships, "User")
        update_board(computer_board, guess_row, guess_col, user_hit)
        guesses_remaining -= 1

        guess_row, guess_col = computer_guess(size, [])
        computer_hit = check_guess(guess_row, guess_col, user_ships, "Computer")
        update_board(user_board, guess_row, guess_col, computer_hit)

        print_board(user_board, title="User Grid:")
        print_board(computer_board, title="Computer Grid:")

        print(f"User guessed Row {guess_row}, Column {guess_col} - {'Hit' if user_hit else 'Miss'}")
        print(f"Computer guessed Row {guess_row}, Column {guess_col} - {'Hit' if computer_hit else 'Miss'}")
        print(f"Guesses remaining: {guesses_remaining}")
        print(f"User's ships remaining: {len(user_ships)}")
        print(f"Computer's ships remaining: {len(computer_ships)}")
        print()

        user_game_over = is_game_over(computer_ships)

    print("User's final board:")
    print_board(user_board, title="User Grid:")
    print("Computer's final board:")
    print_board(computer_board, title="Computer Grid:")

    if user_game_over:
        print('User wins! All computer battleships have been sunk!')
    else:
        print('Computer wins! User ran out of guesses!')

    play_again = input("Would you like to play again? "
                       "(yes/no): ").strip().lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == '__main__':
    play_game()
