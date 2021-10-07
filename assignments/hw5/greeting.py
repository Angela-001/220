"""
Name: Angela Nganga
greeting.py

Problem: This program displays a heart.

Certification of Authenticity:
I certify that this assignment is entirely my own work, however I discussed it with tutors at the CSL.
"""

import time
from graphics import GraphWin, Circle, Polygon, Line, Point, Text



def main():
    width = 400
    height = 400
    win = GraphWin("Draw a heart", width, height)

    circle = Circle(Point(200, 200), 29)
    circle.draw(win)
    circle.setOutline("pink")
    circle.setFill("pink")
    circle_2 = circle.clone()
    circle_2.move(60,0)
    circle_2.draw(win)

    triangle = Polygon(Point(230, 350), Point(170, 200), Point(290, 200))
    triangle.draw(win)
    triangle.setOutline("pink")
    triangle.setFill("pink")

    line1 = Line(Point(0,400), Point(20,380))
    line1.setArrow("last")
    line1.draw(win)

    message = Text(Point(200,20), "Happy Valentine's Day!")
    message.draw(win)

    for _ in range(30):
        line1.move(15,-15)
        time.sleep(0.1)

    close = Text(Point(200,380), "Click anywhere to close")
    close.draw(win)




    win.getMouse()
    win.close()


main()
