import tkinter as tk
from tkinter import messagebox

# Function to check if a player has won
def check_winner():
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]

    # Check for a tie
    if all(board[i][j] != '' for i in range(3) for j in range(3)):
        return 'Tie'

    return None

# Function to handle the button click
def button_click(row, col):
    global turn

    if board[row][col] == '':
        board[row][col] = turn
        buttons[row][col].config(text=turn, state='disabled')

        winner = check_winner()
        if winner:
            if winner == 'Tie':
                messagebox.showinfo("Game Over", "It's a Tie!")
            else:
                messagebox.showinfo("Game Over", f"{winner} wins!")
            reset_game()
        else:
            turn = 'O' if turn == 'X' else 'X'

# Function to reset the game
def reset_game():
    global turn, board
    turn = 'X'
    board = [['' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='', state='normal')

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

turn = 'X'  # 'X' starts
board = [['' for _ in range(3)] for _ in range(3)]  # Game board

# Create the buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='', font=('normal', 40), width=5, height=2,
                                  command=lambda i=i, j=j: button_click(i, j))
        buttons[i][j].grid(row=i, column=j)

# Add a reset button
reset_button = tk.Button(root, text="Reset Game", font=('normal', 20), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Run the application
root.mainloop()
