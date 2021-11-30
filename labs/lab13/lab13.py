"""
Name: Angela Nganga
lab13.py
Problem: This program uses list methods and compares search/sort algorithms
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from algorithms import *
from graphics import *

def trade_alert(tradefile):
    infile = open(tradefile, "r")
    nums = infile.read()
    listnums = nums.split(" ")
    count = 0
    for num in listnums:
        count = count+1
        if int(num) > 830:
            print("Watch out, The trade volume at " + str(count) + " has exceeded 830")
        elif int(num) == 500:
            print("Pay attention, the volume at " + str(count) + " is 500")

    infile.close()







def main():
    trade_alert("trades.txt")
    print(is_in_binary(7, [1, 2, 3, 4, 5]))
    selection_sort([1, 7, 10, 4, 8])
    area1 = Rectangle(Point(1, 2), Point(3, 4))
    area2 = Rectangle(Point(10, 12), Point(13, 16))
    area3 = Rectangle(Point(20, 22), Point(23, 24))
    lista = [area1, area2, area3]
    rect_sort(lista)
    for i in lista:
        print(calc_area(i), end=" ")
    pass


main()
