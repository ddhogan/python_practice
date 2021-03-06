from random import randint

# Set up the board
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# Place the ship somewhere
ship_row = random_row(board)
ship_col = random_col(board)

# these next two lines can help with debugging, but should be commented out or the game will be too easy!
#print ship_row
#print ship_col

# This for loop plays up to 4 iterations
for turn in range(4):
    # tell the player what turn they're on:
    print ("Turn", turn + 1)
    # make a guess, test the guess

    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.")
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            if turn == 3:
                board[ship_row][ship_col]="@"                
                print ("Game Over")

        print_board(board)