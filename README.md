# Battleships
![Screenshot](assets/images/command-line.png)
The Battleships game is designed to provide an engaging and interactive experience for the user. Each function contributes to a specific aspect of the game, ensuring it is intuitive, challenging, and enjoyable. From creating and displaying the board to handling user input and updating the game state, every part of the program works together to deliver a cohesive and entertaining gameplay experience.
## Features and Functions

### create_board(board)
- Creates the game board as a 2D grid filled with the character '~' to represent water
- Initializes the visual representation of the game board where players will make their guesses
- Ensures a clean slate for each new game

### print_board(board)
- Prints the current state of the game board to the console
- Provides a visual display of the game board, helping players see their guesses and the status of their hits and misses
- Includes row and column numbers to guide user input

### place_ships(board, ships, num_ships)
- Randomly places a specified number of ships on the game board, ensuring no two ships occupy the same space
- Adds randomness to each game, making it challenging and replayable
- Ensures that ships are distributed unpredictably, which enhances the strategic element of the game

### get_user_guess(size)
- Prompts the user to input their guess for a row and a column, validates the input, and handles incorrect input
- Ensures user input is within the valid range and prevents invalid guesses
- Provides clear feedback and re-prompts for incorrect input, enhancing the user’s interaction with the game

### check_guess(guess_row, guess_col, ships)
- Checks if the user's guess hits a ship and updates the ships list accordingly
- Provides immediate feedback on whether a guess was successful or not, keeping the user engaged
- Updates the game state based on the user's actions, creating a dynamic game environment

### update_board(board, guess_row, guess_col, hit)
- Updates the game board to mark a guessed position as hit ('X') or missed (' ')
