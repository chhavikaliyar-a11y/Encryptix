board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True


# Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# Take player input
def playerInput(board):
    while True:  # Loop until valid input is received
        inp = int(input("Enter a number 1-9: "))
        if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
            board[inp - 1] = currentPlayer
            break  # Exit the loop if input is valid
        else:
            print("Oops! That spot is already taken or invalid. Try again.")


# Check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False  # Return False if no winner


def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False  # Return False if no winner


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False  # Return False if no winner


def checkTie(board):
    global gameRunning
    if "-" not in board and winner is None:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False


def checkWin():
    if checkDiag(board) or checkHorizontle(board) or checkRow(board):
        print(f"The winner is {winner}")
        return True  # Return True if there is a winner
    return False  # Return False if no winner


# Switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"  # Corrected from "0" to "O"
    else:
        currentPlayer = "X"


# Main game loop
while gameRunning:
    printBoard(board)
    playerInput(board)
    if checkWin():  # Check for win after player input
        gameRunning = False  # End the game if there's a winner
    checkTie(board)
    switchPlayer()
