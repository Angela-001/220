"""
Name: Angela Nganga
arithmetic,loops.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def average():
    grades = int(input("Enter the number of grades: "))
    start = 1
    sum = 0
    for i in range(start,grades+1):
        text = input("enter your grade on "+str(i))
        sum = sum + text
        average = sum/grades
    print("This is the value of the average", average)


def tip_jar():
    fact = 0
    for i in [5, 4, 3, 2, 1]:
        x= float(input("Enter the amount of donation: "))
        fact = fact + x
    print("This is the total amount", fact)


def newton():
    x= eval(input("Enter the number x"))
    improve= eval(input("Enter the number of times to improve the approximation: "))
    approx = x / 2
    for i in range(improve):
        approx = (approx+(x/approx))/2

    print("This is the approximation for the square root", x)
    print("This is the number of approximations",improve)
    print(approx)


def sequence():
    x=int(input("Enter the number of terms"))
    start=1
    for i in range(x):
        start=2*(i%2)+start
        #print(start,end=" ")


def pi():
    n=eval(input("Enter the number of terms in the series: "))
    total = 1
    start1=2
    den=1
    for i in range(n):
        den=2*(i%2)+den
        num=1+(i+1%2)+i
        print("num:", start1, num)

        total=(start1/den)*total*num/den

    print("The approximation for pi/2 is: ",total)
