"""
Name: Angela Nganga
bumper.py

Problem: This program uses the graphics package and uses decision statements.
Certification of Authenticity:
I certify that this assignment is entirely my own work, however I discussed it with tutors at the CSL and worked with Maritou Seke.
"""

from graphics import*
from random import randint

def did_collide(ball, ball2):
    r1_x = ball.getCenter().getX()
    r1_y = ball.getCenter().getY()
    r1 = ball.getRadius()
    r2_x = ball2.getCenter().getX()
    r2_y = ball2.getCenter().getY()
    r2 = ball2.getRadius()
    x_values = (r1_x - r2_x) ** 2
    y_values = (r1_y - r2_y) ** 2
    d = (x_values + y_values) ** (1 / 2)
    if d <= (r1+r2):
        return True
    else:
        return False


def hit_vertical(ball, win):
    edge_y = ball.getCenter().getY() + ball.getRadius()
    edge_y2 = ball.getCenter().getY() - ball.getRadius()
    if edge_y >= win.getHeight() or edge_y2 <= 0:
        return True
    else:
        return False

def hit_horizontal(ball, win):
    edge_x = ball.getCenter().getX() + ball.getRadius()
    edge_x2 = ball.getCenter().getX() - ball.getRadius()
    if edge_x >= win.getWidth() or edge_x2 <= 0:
        return True
    else:
        return False



def get_random(move_amount):
    move = randint(-move_amount, +move_amount)
    return move


def get_random_color():
    return color_rgb()

def main():
    width = 400
    height = 400
    win = GraphWin("Bumper", width, height)
    ball = Circle(Point(3, 4), 10.5)
    ball.draw(win)
    dx = get_random(30)
    dy = get_random(30)
    ball2 = Circle(Point(10, 11), 13.5)
    ball2.draw(win)
    randint(-30, 30)
    did_collide(ball, ball2)
    total = 0
    while not (hit_vertical(ball, win) or hit_horizontal(ball, win)):
        get_random_color()
        total = total + ball.move(dx, dy)
        return total

    win.getMouse()
    win.close()

if __name__=='__main__':
    main()
