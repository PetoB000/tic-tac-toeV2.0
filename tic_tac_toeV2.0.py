import os
# import random


def init_board():
    board = [["." for _ in range(3)] for _ in range(3)]
    return board


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_winer(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != ".":
            return True
        return False
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ".":
            return True
        return False
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ".":
        return True
    return False
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ".":
        return True
    return False



def reset(board):
    clear()
    print_board(board)
    get_move(board)



def get_move(board):
    row, col = 0, 0
    letters = ['A', 'B', 'C']
    numbers = [0, 1, 2]
    while check_winer(board) == False:
        row_col = input("Give a letter for the row and a number for the collumn:")
        if row_col == quit:
            print("Thanks for playing")
            quit()
        if len(row_col) == 2:
            if row_col[0].isalpha() and row_col[1].isdigit():
                row = row_col[0].upper()
                col = int(row_col[1]) - 1
                if row not in letters:
                    print("Invalid input for row")
                    reset(board)
                elif col not in numbers:
                    print("Invalid input for collumn")
                    reset(board)
                elif row == "A":
                    row = 0
                elif row == "B":
                    row = 1
                elif row == "C":
                    row = 2
                elif row not in letters:
                    print("Invalid input for row")
                    reset()
                elif col not in numbers:
                    print("Invalid input for collumn")
                    reset()
            return row, col
        else:
            print("Invalid input")


def mark(turn, row, col, board):
    if turn % 2 == 0:
        player = 'X'
    else:
        player = '0'
    if board[row][col] == ".":
        board[row][col] = player
    else:
        print("Field taken")
    return board


def is_full(turn):
    if turn == 9:
        return True
    return False


def print_board(board):
    letters = ['A', 'B', 'C']
    print("  1", "  2", "  3")
    for i in range(len(board)):
        print(letters[i] + " " + board[i][0] + " | " + board[i][1] + " | " + board[i][2])
        if i == 0 or i == 1:
            print(" ---|---|---")


def main():
    board = init_board()
    print_board(board)
    turn = 0
    won = check_winer(board)
    while won == False and is_full(turn) == False:
        move = get_move(board)
        mark(turn, move[0], move[1], board)
        print_board(board)
        turn += 1

if __name__ == '__main__':
    main()