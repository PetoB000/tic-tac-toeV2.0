import os
# import random


def init_board():
    board = [["." for _ in range(3)] for _ in range(3)]
    return board


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_move():
    pass


def mark():
    pass


def has_won():
    pass


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

def print_result():
    pass


def quiting():
    pass


def tictactoe_game():
    pass


def demo():
    board = init_board()
    print_board(board)

if __name__ == '__main__':
    demo()