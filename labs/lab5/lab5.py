"""
Name: Angela Nganga
graphics.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()
"""
Problem: This function prints the perimeter and area.
"""

def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    text1 = Text(Point(150, 10),"Click on any 3 points")
    text1.draw(win)
    P1 = win.getMouse()
    P2 = win.getMouse()
    P3 = win.getMouse()
    polygon1 = Polygon(P1,P2,P3)
    polygon1.draw(win)
    dx = P2.getX() - P1.getX()
    a_x = P1.getX()
    a_y = P1.getY()
    b_x = P2.getX()
    b_y = P2.getY()
    c_x = P3.getX()
    c_y = P3.getY()
    length1 = math.sqrt(((a_x - b_x)**2) + ((a_y-b_y)**2))
    length2 = math.sqrt(((b_x - c_x)**2) + ((b_y-c_y)**2))
    length3 = math.sqrt(((c_x - a_x)**2) + ((c_y-a_y)**2))
    perimeter = length1 + length2 + length3
    s= (length1+length2+length3)/2
    area = math.sqrt(s*(s-length1)*(s-length2)*(s-length3))
    text1.setText("The perimeter is:" + str(perimeter) + "\nThe area is:" + str(area))
    text1.move(0, 460)


    # and display its area in the graphics window.

    # Wait for another click to exit
    win.getMouse()
    win.close()

"""
Problem: This function prints the different colors for the circle. 
"""

def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    entry = Entry(Point(win_width / 2 - 20, win_height / 2 + 40), 3)
    entry.setText(255)
    entry.draw(win)
    entry2 = Entry(Point(win_width / 2 - 20, win_height / 2 + 70), 3)
    entry2.setText(255)
    entry2.draw(win)
    entry3 = Entry(Point(win_width / 2 - 20, win_height / 2 + 100), 3)
    entry3.setText(255)
    entry3.draw(win)


    for i in range (5):
        win.getMouse()
        red = entry.getText()
        green = entry2.getText()
        blue = entry3.getText()
        color = color_rgb(eval(red), eval(green), eval(blue))
        shape.setFill(color)

    # Wait for another click to exit
    win.getMouse()
    win.close()

"""
Problem: This function computes different values on the string based on position. 
"""


def process_string():
    string1 = (input("Enter text here: "))
    string_ans = string1[0]
    print(string_ans)
    string_ans2 = string1[-1]
    print(string_ans2)
    string_ans3 = string1[1:5]
    print(string_ans3)
    string_ans3 = string1[0] + string1[-1]
    print(string_ans3)
    string_ans4 = (string1[0:2])*10
    print(string_ans4)
    for i in range(len(string1)):
        n = (string1[i])
        print(n)
    string_ans5 = string1[:]
    print(len(string_ans5))

def process_list():
    pt = Point(5,10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    value[1]
    value[3]
    x = "hi" + "there"
    print(x)




def main():
    # target()
    triangle()
    color_shape()
    process_string()
    process_list()
    pass


main()
