"""
Name: Angela Nganga
Partner: Marietou Seck
Functions and spy craft.py
This function uses python text files and writes functions.
I certify that this assignment is entirely my own.
"""

import math

def cash_conversion():
    user_input = int(input("Enter an integer value here: "))
    print("${0:2.2f}".format(user_input))


def encode():
    user_input = input("Type in a word here: ")
    key = eval(input("Type in a key here: "))
    output = ""
    for ch in user_input:
        encode1 = chr(ord(ch) + key)
        output = output + str(encode1)
    print(output)


def sphere_area(radius):
    area = 4*math.pi*(radius**2)
    return(area)

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius**3)
    return(volume)


def sum_n(n):
    start = 0
    for i in range(n):
        start = start + i+1
    return start



def sum_n_cubes(n):
    start = 0
    for i in range(n):
        cubes = (i+1)**3
        start = cubes + start
    return start

def encode_better():
    name = input("Enter your message here: ")
    key = input("Enter the key here: ")
    string = " "
    for i in range(len(name)):
        shift = ord(key[i]) + ord(name[i])-97
        string += chr(shift)
    print("Your encrypted message is:" , string)




def main():
    cash_conversion()
    print(sphere_area(5))
    print(sphere_volume(5))
    print(sum_n(5))
    print(sum_n_cubes(3))
    encode()
    encode_better()


    pass


main()
