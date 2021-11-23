"""
Name: Angela Nganga
lab12.py
Problem: This program uses while control structures and lists
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from algorithms import is_in_linear, read_data
from random import randint


def find_and_remove_first(list, value):
    i = 0
    while i < len(list):
        if list[i] == value:
            list.insert(i, "Angela")
            list.remove(value)
        i = i + 1


def good_input():
    user_input = eval(input("Enter a number in the range 1 to 10: "))
    while user_input > 10 or user_input < 1:
        print("The number is out of range")
        user_input = eval(input("Enter a number in the range 1 to 10: "))
    return user_input


def num_digits():
    user_input = eval(input("Enter a positive integer "))
    while user_input > 0:
        i = 0
        num = user_input
        while num > 0:
            num = num // 10
            i = i + 1
        print("There were", i, " digits found")
        user_input = eval(input("Enter a positive integer "))


def hi_lo_game():
    randi = randint(0, 100)
    guess = eval(input("Enter an integer in the range 1 to 100 inclusive: "))
    guess_no = 0
    while guess_no < 6:
        guess_no = guess_no + 1
        if randi == guess:
            print("You win in ", guess_no, "guesses!")
            guess_no = 10
        else:
            if guess < randi:
                print("Your number is too low")
            else:
                print("Your number is too high")
            if guess_no > 6:
                print("Sorry, you lose. The number was", randi)
            else:
                guess = eval(input("Enter an integer in the range 1 to 100 inclusive: "))


def main():
    list = [1, 2, 3, 4, 5]
    value = 2
    find_and_remove_first(list, value)
    print(read_data("read_data_test_data.txt"))
    print(is_in_linear(2, [1, 2, 3, 4, 5]))
    print(good_input())
    num_digits()
    hi_lo_game()
    pass


main()


# def read_data(filename):
#     infile = open(filename, "r")
#     eachline = infile.read()
#     eachline = eachline.split()
#     i = 0
#     while i < len(eachline):
#         eachline[i] = eval(eachline[i])
#         i = i+1
#     infile.close()
#     return eachline
#
# def is_in_linear(search_val, values):
#     i = 0
#     while i <len(values):
#         if search_val == values[i]:
#             return True
#         else:
#             i = i + 1
#     return False

