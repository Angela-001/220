"""
Name: Angela Nganga
lab4.py
Problem: This function draws circles in locations given by the user.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def squares():


    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 70), Point(90,110))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()

        # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX()
        dy = p.getY()
        # shape.move(dx, dy)
        shape = Rectangle(Point((dx - 20, dy- 20), Point((dx + 20, dy + 20))))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    print("Click again to quit: ")
    win.getMouse()
    win.close()

"""
Problem: This function displays information about a rectangle drawn by the user.
"""

def rectangle():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    corner1 = win.getMouse()
    corner2 = win.getMouse()
    shape = Rectangle(corner1, corner2)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    width = corner1.getX() - corner2.getX()
    width = abs(width)
    height = corner1.getY() - corner2.getY()
    height = abs(height)
    perimeter = 2*(width + height)
    area = (width) * (height)

    instr_pt = Point(200, height - 20)
    perimeter = Text(instr_pt, "Display the perimeter: " + str(perimeter))
    perimeter.draw(win)
    instr_pt = Point(200, height - 40)
    area = Text(instr_pt, "Display the area: " +str(area))
    area.draw(win)

    print("Click again to quit: ")
    win.getMouse()
    win.close()

    pass

"""
Problem: This function displays information about a rectangle drawn by the user.
"""


def circle():


    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4")

    center = win.getMouse()
    circum= win.getMouse()

    radius = ((center.getX() - circum.getX())**2 + (center.getY() - circum.getY())**2)**(1/2)
    # radius = abs(radius)
    circle = Circle(center, radius)
    circle.draw(win)
    # d = ((radius)**)+()
    instr_pt = Point(width / 2, height - 10)
    radius = Text(instr_pt, "Display the radius" + str(radius))
    radius.draw(win)

    print("Click again to quit: ")
    win.getMouse()
    win.close()

"""
Problem: This function approximate the value for pi.
"""
def pi2():
    eval(input("Enter a value for n: "))
    eval(input("Enter the numbers of terms to sum: "))
    pi = pi+(V*switch)
    switch = switch*(-1)
