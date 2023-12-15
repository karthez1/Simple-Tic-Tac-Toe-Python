# Define function to check for winner
def winner():
    # X axis
    if grid[0] == turn and grid[1] == turn and grid[2] == turn:
        return turn
    elif grid[3] == turn and grid[4] == turn and grid[5] == turn:
        return turn
    elif grid[6] == turn and grid[7] == turn and grid[8] == turn:
        return turn
    # Y axis
    if grid[0] == turn and grid[3] == turn and grid[6] == turn:
        return turn
    elif grid[1] == turn and grid[4] == turn and grid[7] == turn:
        return turn
    elif grid[2] == turn and grid[5] == turn and grid[8] == turn:
        return turn
    # Diagonal axis
    if grid[0] == turn and grid[4] == turn and grid[8] == turn:
        return turn
    elif grid[2] == turn and grid[4] == turn and grid[6] == turn:
        return turn


# Prompt user to make a move, and update grid
def select_square():
    global grid  # To modify the global variable
    global x, y, index
    while True:
        try:
            x, y = map(int, input().split())
            if not (1 <= x <= 3 and 1 <= y <= 3):
                print("Coordinates should be from 1 to 3!")
                continue

            index = (x - 1) * 3 + (y - 1)
            if grid[index] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                return index
        except ValueError:
            print("You should enter numbers!")


# Updates the current selected grid
def update_square():
    global grid

    # Check whose turn it is and update the grid accordingly
    if turn == "X":
        grid[index] = "X"
    else:
        grid[index] = "O"

# Prints out the game board
def print_board():
    print("---------")
    print("|", grid[0], grid[1], grid[2], "|")
    print("|", grid[3], grid[4], grid[5], "|")
    print("|", grid[6], grid[7], grid[8], "|")
    print("---------")

# Runs through the game of tic-tac-toe, updating the grid
def game():
    global game_round
    print_board()
    while game_round < 9:
        select_square()
        update_square()
        print_board()
        if winner():
            print_board()
            print(turn, "wins!")
            return

        game_round = game_round + 1
        change_turn()
    print("Draw")

# Changes between X or 0 based on turn
def change_turn():
    global turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

# Variables
game_round = 0
turn = "X"
grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
game()