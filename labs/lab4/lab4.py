"""
Name: Angela Nganga
lab4.py
Problem: These functions use the graphics package and practice accumulating sequences.

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
    shape = Rectangle(Point(50, 70), Point(90, 110))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        print("test")
        p = win.getMouse()

        # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX()
        dy = p.getY()
        new = Rectangle(Point(dx - 20, dy - 20), Point(dx + 20, dy + 20))
        new.setOutline("red")
        new.setFill("red")
        new.draw(win)

    print("Click again to quit: ")
    win.getMouse()
    win.close()




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
    perimeter = 2 * (width + height)
    area = (width) * (height)

    instr_pt = Point(200, height - 20)
    perimeter = Text(instr_pt, "Display the perimeter: " + str(perimeter))
    perimeter.draw(win)
    instr_pt = Point(200, height - 40)
    area = Text(instr_pt, "Display the area: " + str(area))
    area.draw(win)

    print("Click again to quit: ")
    win.getMouse()
    win.close()

    pass




def circle():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    center = win.getMouse()
    circum = win.getMouse()

    radius = ((center.getX() - circum.getX()) ** 2 + (center.getY() - circum.getY()) ** 2) ** (1 / 2)
    # radius = abs(radius)
    circle = Circle(center, radius)
    circle.draw(win)
    instr_pt = Point(width / 2, height - 10)
    radiustext = Text(instr_pt, "Radius is " + str(radius) + ", click again to quit.")
    radiustext.draw(win)
    win.getMouse()
    win.close()




def pi2():
    n = eval(input("Enter the numbers of terms to sum: "))
    sum = 0.0
    print(n)
    for i in range(1, 4 * n, 4):
        sum += (4.0 / i) - (4.0 / (i + 2.0))
        print(sum)
    print(sum)


def main():
    # squares()
    # rectangle()
    # circle()
    # pi2()


main()
