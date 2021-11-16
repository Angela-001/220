"""
Name: Angela Nganga
Tic-tac-toe.py
Problem: This program constructs a game of tic-tac-toe.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import*
class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(label, shape.getCenter())


    def get_label(self):
        return self.text.getTest()#self.shape is the name of the rectangle, we can replace self.shape with rectangle1 since it's like a variable,same to self.text

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        if self.shape.getP1().getX()<= point.getX()<= self.shape.getP2().getX() and self.shape.getP1().getY()<= point.getY()<= self.shape.getP2().getY():
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)#get text object, call on set text method to reassign the string that it displays


    def main():
        arectangle = Rectangle(Point(30, 50), Point(100, 150))
        win = Graphwin("Button", 400, 400)
        button1 = Button(arectangle, "Door1")