import os
import random


def init_board():
    board = [["." for _ in range(3)] for _ in range(3)]
    return board


def restart():
    option = input("Do you want to play again?\n(Y/N)").upper()
    if option == "Y":
        main_menu()
    elif option == "N":
        print("Thank you for playing!")
        quit()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_row(board):
    for row in range(len(board)):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != ".":
            return True


def check_col(board):
    for col in range(len(board)):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != ".":
            return True


def check_first_diagonal(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ".":
        return True


def check_second_diagonal(board):
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ".":
        return True


def has_won(board):
    row = check_row(board)
    col = check_col(board)
    diag1 = check_first_diagonal(board)
    diag2 = check_second_diagonal(board)
    if row or col or diag1 or diag2 == True:
        return True


def reset(board):
    clear()
    print_board(board)
    get_move(board)



def get_move(board):
    row, col = 0, 0
    letters = ['A', 'B', 'C']
    numbers = [0, 1, 2]
    while True:
        row_col = input("Give a letter for the row and a number for the collumn:").upper()
        if row_col == "QUIT":
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


def get_AI_move(board):
    aviable_moves = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == ".":
                aviable_moves.append((row, col))
    return random.choice(aviable_moves)


def mark(turn, row, col, board):
    if turn % 2 == 0:
        player = 'X'
    else:
        player = 'O'
    if board[row][col] == ".":
        board[row][col] = player
    else:
        print("Field taken")
        return False
    return board


def is_full(board):
    counter = 0
    for row in board:
        for col in row:
            if col == ".":
                counter += 1
        if counter > 0:
            return False
    if counter == 0:
        return True


def print_board(board):
    letters = ['A', 'B', 'C']
    print("  1", "  2", "  3")
    for i in range(len(board)):
        print(letters[i] + " " + board[i][0] + " | " + board[i][1] + " | " + board[i][2])
        if i == 0 or i == 1:
            print(" ---|---|---")


def main(mode):
    board = init_board()
    turn = 0
    if mode == "HUMAN-HUMAN":
        while True:
            if turn % 2 == 0:
                player = 'O'
            else:
                player = 'X'
            clear()
            if has_won(board) == True:
                print(player + " has won!")
                print_board(board)
                restart()
            if is_full(board) == True:
                print("The board is full")
                print_board(board)
            print_board(board)
            move = get_move(board)
            mark(turn, move[0], move[1], board)
            turn += 1
    if mode == "HUMAN-AI":
        while True:
            clear()
            if has_won(board) == True:
                print(player + " has won!")
                print_board(board)
                restart()
            if is_full(board) == True:
                print("The board is full")
                print_board(board)
                quit()
            if turn % 2 == 0:
                player = 'X'
                print_board(board)
                move = get_move(board)
                mark(turn, move[0], move[1], board)
            else:
                player = 'O'
                print_board(board)
                move = get_AI_move(board)
                mark(turn, move[0], move[1], board)
            turn += 1


def main_menu():
    while True:
        clear()
        print("Please select a game mode\n")
        mode = input("1. HUMAN VS HUMAN\n2. HUMAN VS AI\n").upper()
        if mode == "1":
            main("HUMAN-HUMAN")
        elif mode == "2":
            main("HUMAN-AI")
        elif mode == "QUIT":
            os.system("clear")
            quit()
        else:
            print("Invalid input, please use the numbers!")


if __name__ == '__main__':
    main_menu()