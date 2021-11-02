"""
Name: Angela Nganga
conditionals.py

Problem: This program uses accumulations and conditional control structures.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *

def addTen(nums):
    for i in range(len(nums)):
        nums[i]+=10

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2

def sumList(nums):
    start = 0
    for i in range(len(nums)):
        start = nums[i] +start
    return start

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])

def writeSumOfSquares():
    user_file = input("Enter file name with at least 2 numbers on each line without .txt: ")
    read_file = open(user_file, "r")
    write_file = open("sum_out.txt", "w")
    total = read_file.readlines()
    for line in total:
        line = line.split(" ")
        toNumbers(line)
        squareEach(line)
        output = sumList(line)
        print("The sum of squares is =", output ,end="\n",  file = write_file)

    read_file.close()
    write_file.close()

def starter():
    weight = float(input("Enter the weight: "))
    numWins = int(input("Enter the number of wins: "))
    if 150<= weight <=160 and numWins>=5:
        print("The individual should start")
    elif weight>199 or numWins>20:
        print("The individual should start")
    else:
        print("The individual should not start")


def leapYear(year):
    if year%400 ==0:
        print(year, "is a leap year")
        return True
    elif year%4==0 and year%100!=0:
        print(year, "is a leap year")
        return True
    elif year%100 ==0:
         print(year, "is not a leap year")
         return False
    else:
        print(year, "is not a leap year")
        return False

def circleOverlap():
    width = 400
    height = 400
    win = GraphWin("Lab 9", width, height)
    message = Text(Point(200, 29), "Click on any 2 points")
    message.draw(win)

    center = win.getMouse()
    circumf = win.getMouse()

    x_values1 = (center.getX()-circumf.getX())**2
    y_values1 = (center.getY()-circumf.getY())**2
    radius = (x_values1 + y_values1)**(1/2)
    Circ = Circle(center, radius)

    Circ.draw(win)
    Circ_x = Circ.getCenter().getX()
    Circ_Y = Circ.getCenter().getY()
    circ2 = Circle(Point(200, 200), 10.5)
    circ2.draw(win)
    circ2_x = circ2.getCenter().getX()
    circ2_Y = circ2.getCenter().getY()
    x_values = (Circ_x - circ2_x)**2
    y_values = (Circ_Y - circ2_Y)**2
    d = (x_values + y_values)**(1/2)
    if d > 0:
        message = Text(Point(200, 380), " The circles do not overlap")
        message.draw(win)
    else:
        message = Text(Point(200, 380), " The circles overlap")
        message.draw(win)

    win.getMouse()
    win.close()

def main():
    addTen([1, 3, 5])
    squareEach([1, 3, 5])
    sumList([1, 3, 5])
    toNumbers(["1", "3", "5"])
    starter()
    leapYear(2100)
    circleOverlap()
    writeSumOfSquares()

    pass


main()
