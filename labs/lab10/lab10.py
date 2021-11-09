"""
Name: Angela Nganga
Tic-tac-toe.py
Problem: This program constructs a game of tic-tac-toe.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def build_board():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return numbers

def display_board(numbers):#drew board
    for i in range(1, len(numbers)-5):
        print(numbers[i-1], "|", end = " ")
    print("\n--------------", "\n")
    for i in range(4, len(numbers)-2):
        print (numbers[i-1], "|", end = " ")
    print("\n--------------", "\n")
    for i in range(7, len(numbers)+1):
        print(numbers[i-1], "|", end = " ")
    print("\n---------------", "\n")

def fill_spot(board, position, character):#checks if it's an x or an o
    if character == "x" or character =="o":#board represents the whole list
        board[position-1] = character #replace the number with the x or o


def legal_spot(board, position, character):#checks it's a legit spot on the board
    if str(board[position-1]).isnumeric():
        return True
    else:
        return False

def game_won(board):
    if board[0:3] == ["x", "x", "x"] or board[0:3] == ["o", "o", "o"]:
        return True
    elif board[3:6] == ["x", "x", "x"] or board[3:6] == ["o", "o", "o"]:
        return True
    elif board[6:9] == ["x", "x", "x"] or board[6:9] == ["o", "o", "o"]:
        return True
    elif board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[0] == board[4]== board[8]:
        return True
    elif board[2] == board[4] == board[6]:
        return True
    return False


def game_over(board):
    if game_won(board):
        return True
    for i in range(len(board)):
        if str(i).isnumeric():
            return False
        else:
            return True


def main():
    print("This is a game of tic-tac-toe. Enter either x or o")
    board = build_board()
    while not game_over(board):
        display_board(board)
        user_position = eval(input("Which position?"))
        user_char = input("Are you x or o?")
        fill_spot(board, user_position, user_char)
    if game_won(board):
        print("Player", user_char, "wins")
    else:
        print("It's a tie")

    # legal_spot(board, user_position, user_char) == True
    pass


main()
