#!/usr/bin/python3
def print_board(board):
    """
    Prints the tic-tac-toe board.

    Parameters:
    - board: A 2D list representing the tic-tac-toe board.

    Returns:
    - None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner on the tic-tac-toe board.

    Parameters:
    - board: A 2D list representing the tic-tac-toe board.

    Returns:
    - True if there is a winner, False otherwise.
    """
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Plays a game of tic-tac-toe.

    Returns:
    - None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    while moves < 9:  # Maximum possible moves
        print_board(board)
        row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
        col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
            board[row][col] = player
            moves += 1

            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                return

            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("Invalid input or spot already taken! Try again.")

    print_board(board)
    print("It's a tie!")

tic_tac_toe()

