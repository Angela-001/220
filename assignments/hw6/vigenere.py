"""
Name: Angela Nganga
vigenere.py

Problem: This program implements the Vigenere cipher.

Certification of Authenticity:
I certify that this assignment is entirely my own work, however I discussed it with tutors at the CSL and with Brianna Joyner.
"""

from graphics import *

def button_clicked(win, button):
    clicked = win.getMouse()
    clicked_x = clicked.getX()
    clicked_y = clicked.getY()



def user_input(enter, enter_2):
    encrypt_msg = " "
    user_code = enter.getText()
    user_key = enter_2.getText()
    for i in range(len(user_code)):
        encrypt_char = chr((ord(user_code[0]) + ord(user_key[0])) % 26)
        encrypt_msg += encrypt_char
    return encrypt_msg



def main():
    width = 400
    height = 400
    win = GraphWin("Vigenere cipher", width, height)

    message = Text(Point(80, 100), "Message to encode ")
    message.draw(win)
    keyword = Text(Point(80, 160), "Enter Keyword ")
    keyword.draw(win)

    enter = Entry(Point(220, 100), 20)
    enter.draw(win)
    enter_2 = enter.clone()
    enter_2.move(0, 60)
    enter_2.draw(win)



    encode = Text(Point(200, 200), "Encode ")
    center = encode.getAnchor()
    encode.draw(win)
    c_x = center.getX()
    c_y = center.getY()
    rectangle1 = Rectangle(Point(c_x-30, c_y+20), Point(c_x+30, c_y-20))
    rectangle1.draw(win)


    button_clicked(win,rectangle1)

    output = user_input(enter, enter_2)
    output.replace(" ", "")
    output.upper()


    rectangle1.undraw()
    encode.setText(" Resulting Message\n" + output)

    close = Text(Point(200, 380), "Click anywhere to close")
    close.draw(win)

    win.getMouse()
    win.close()

main()
