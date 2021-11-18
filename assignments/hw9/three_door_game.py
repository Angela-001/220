"""
Name: Angela Nganga
three_door_game.py
Problem: This program draws 3 doors and randomly selects one as the secret door.
Certification of Authenticity:
I certify that this assignment is entirely my own work, however I discussed it with tutors at the CSL.
"""


from random import randint
from graphics import*
from button import Button


def main():
    arectangle1 = Rectangle(Point(80, 270), Point(120, 290))
    arectangle2 = Rectangle(Point(130, 270), Point(170, 290))
    arectangle3 = Rectangle(Point(180, 270), Point(220, 290))
    win = GraphWin("Three Button Game", 400, 400)
    button1 = Button(arectangle1, "Door1")
    button2 = Button(arectangle2, "Door2")
    button3 = Button(arectangle3, "Door3")
    button1.draw(win)
    button2.draw(win)
    button3.draw(win)
    message3 = Text(Point(200, 10), "I have a secret door")
    message3.draw(win)
    message4 = Text(Point(200, 300), "Click to choose my door")
    message4.draw(win)

    button_list = [button1, button2, button3]
    ans = button_list[randint(0, 2)]

    user_click = win.getMouse()
    for button in button_list:
        if button.is_clicked(user_click):
            if ans == button:
                message3.setText("You win!")
                button.color_button("green")
                message4.setText("Click to close")
            else:
                message3.setText("You lost!")
                button.color_button("red")
                message4.setText(ans.get_label() + " is my secret door" )

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

