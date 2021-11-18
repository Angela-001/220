"""
Name: Angela Nganga
bumper.py

Problem: This program uses the graphics package and uses decision statements.
Certification of Authenticity:
I certify that this assignment is entirely my own work, however I discussed it with tutors at the CSL.
"""

from graphics import *
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
    if d <= (r1 + r2):
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
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return color_rgb(r, g, b)


def main():
    width = 400
    height = 400
    win = GraphWin("Bumper", width, height)
    ball = Circle(Point(100, 100), 10.5)
    ball.draw(win)
    dx1 = get_random(10)
    dy1 = get_random(10)
    dx2 = get_random(10)
    dy2 = get_random(10)
    ball2 = Circle(Point(300, 300), 13.5)
    ball2.draw(win)
    ball.setFill(get_random_color())
    ball2.setFill(get_random_color())
    randint(-30, 30)
    did_collide(ball, ball2)

    playing = True
    while playing:
        if win.checkMouse():
            playing = False
        time.sleep(.1)
        if hit_vertical(ball, win):
            dy1 = -dy1
        if hit_horizontal(ball, win):
            dx1 = -dx1
        if hit_vertical(ball2, win):
            dy2 = -dy2
        if hit_horizontal(ball2, win):
            dx2 = -dx2
        if did_collide(ball, ball2):
            ball.setFill(get_random_color())
            ball2.setFill(get_random_color())
            dx1 = -dx1
            dx2 = -dx2
            dy1 = -dy1
            dy2 = -dy2
        ball.move(dx1, dy1)
        ball2.move(dx2, dy2)

    win.close()


if __name__ == '__main__':
    main()
