import tkinter as tk
from tkinter import messagebox

# Initialize the game board and variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# Function to print the game board (for debugging)
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Function to check for win or tie
def checkWin():
    global winner
    if checkHorizontle(board) or checkRow(board) or checkDiag(board):
        return True
    return False

def checkHorizontle(board):
    global winner
    for i in range(0, 7, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != "-":
            winner = board[i]
            return True
    return False

def checkRow(board):
    global winner
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != "-":
            winner = board[i]
            return True
    return False

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkTie(board):
    if "-" not in board and winner is None:
        return True
    return False

# Function to switch the player
def switchPlayer():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"

# Function to handle button click
def button_click(index):
    global gameRunning
    if board[index] == "-" and gameRunning:
        board[index] = currentPlayer
        buttons[index].config(text=currentPlayer)
        if checkWin():
            messagebox.showinfo("Game Over", f"The winner is {winner}!")
            gameRunning = False
        elif checkTie(board):
            messagebox.showinfo("Game Over", "It's a tie!")
            gameRunning = False
        else:
            switchPlayer()

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create buttons for the game board
buttons = []
for i in range(9):
    button = tk.Button(root, text="-", font=('Arial', 24), width=5, height=2,
                       command=lambda index=i: button_click(index))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Start the GUI event loop
root.mainloop()
