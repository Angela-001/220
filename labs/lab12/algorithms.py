"""
Name: Angela Nganga
algorithms.py
Problem: This program uses while control structures and lists
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def read_data(filename):
    infile = open(filename, "r")
    eachline = infile.read()
    eachline = eachline.split()
    i = 0
    while i < len(eachline):
        eachline[i] = eval(eachline[i])
        i = i+1
    infile.close()
    return eachline

def is_in_linear(search_val, values):
    i = 0
    while i <len(values):
        if search_val == values[i]:
            return True
        else:
            i = i + 1
    return False









