board = ['-' , '-' , '-' ,
         '-' , '-' , '-' ,
         '-' , '-' , '-']

gameIsGoing = True
currentPlayer = 'X'

# The Winner
winner = None

# Function to display the board
def displayBoard() :
    print ( board[0] + ' | ' + board[1] + ' | ' + board[2] )
    print ( board[3] + ' | ' + board[4] + ' | ' + board[5] )
    print ( board[6] + ' | ' + board[7] + ' | ' + board[8] )


# Function for the main game
def playGame() :
    # This displays the board
    displayBoard ( )

    while gameIsGoing:
        # Handles the turn of the current player
        seeTurnsAndPositions(currentPlayer)

        # Checks if game is over
        checkGameOver()

        # Gives turns to the next player
        nextPlayer()

    # If game ended
    if winner == "X" or winner == "O":
        print(f"{winner} has won")
    elif winner == None:
        print("It's a tie")



def seeTurnsAndPositions(player) :

    print(player + "'s turn")

    # Checks turns and position
    position = input ( "What is the position from 1 to 9: " )
    valid = False
    while not valid:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("What is the position from 1 to 9: ")

        position = int ( position ) - 1

        if board[position] == '-':
            valid = True
        else:
            print("You can't put it there. Put again")

    board[position] = player

    displayBoard ( )

def checkGameOver():
    checkWin()
    checkTie()

def checkWin():
    global winner
    # Check straight lines and sleeping lines and slanting lines
    straight_winner = checkStraightLines()
    sleeping_winner = checkSleepingLines()
    slanting_winner = checkSlantingLines()
    if straight_winner:
        winner = straight_winner

    elif sleeping_winner:
        winner = sleeping_winner

    elif slanting_winner:
        winner = slanting_winner

    else:
        winner = None

def checkStraightLines():
    global gameIsGoing
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'

    if column1 or column2 or column3 :
        gameIsGoing = False

    if column1 :
        return board[0]
    elif column2 :
        return board[1]
    elif column3 :
        return board[2]

def checkSleepingLines():
    global gameIsGoing
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    if row1 or row2 or row3 :
        gameIsGoing = False

    if row1 :
        return board[0]
    elif row2 :
        return board[3]
    elif row3 :
        return board[6]

def checkSlantingLines():
    global gameIsGoing
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'

    if diagonal1 or diagonal2:
        gameIsGoing = False

    if diagonal1 :
        return board[0]
    elif diagonal2 :
        return board[2]

def checkTie():
    # Check if no one wins
    global gameIsGoing
    if '-' not in board:
        gameIsGoing = False
    pass
def nextPlayer():
    global currentPlayer
    # Gives turn to another player
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"

playGame( )