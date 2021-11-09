"""
Name: Angela Nganga
hello.py

Problem: This function prints "hello, world!".

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def main ():
    print("hello, world!")

main ()
total = 0
    n = eval(input("enter the number of values to be entered: "))
    for i in range(n):
        x = (eval(input("enter value: ")))**2
        total = (total + x)
    average2 = total/n
    math.sqrt(average2)



    total = 0
    n = eval(input("enter the number of values to be entered: "))
    for i in range (n):
        x = eval(input("enter value: "))
        total = total + (1/x)
    average3 = n/total


    total = 1
    n = eval(input("enter the number of values to be entered: "))
    for i in range(n):
       x = eval(input("enter value: "))
       total = (total * x)
    average4 = (total)**1/n
    print(average1,average2, average3, average4)


if __name__=='__main__':
    main()


# if hit_vertical(Circle, win):
    #     dy = dy*-1
    #     return dy
    # elif did_collide(ball, ball2):
    #     dx = dx*-1
    #     return dx
    # elif did_collide(ball, ball2):
    #     dy = dy*-1
    #     return dy
    # elif hit_horizontal(Circle, win):
    #     dx = dx*-1
    #     return dx
# for _ in range(100):
#     ball2.move(dx,dy)
#     time.sleep(0.3)
# for _ in range(100):
#     ball.move(dx,dy)
#     time.sleep(0.3)