import math

"""
Name: Angela Nganga
lab2.py

Problem: This function calculates the sum of threes
"""

def sum_of_threes() :
    upper_bound = eval(input("Enter upper bound: "))
    x = upper_bound
    for var in range (0, x+1, 3):
        total = total + var





#end for loop

sum_of_threes()


"""
Problem: This problem prints out a multiplication table
"""


def multiplication_table():
    for num in range (1,11):
        print(num ,end=" ")
        print()
        for num in range (1,11):
            print(num ,end=" ")




#end for loop

multiplication_table()


"""
Problem: This function calculates the area of a triangle.
"""
def triangle_area():
    l1 = eval(input("Enter the length 1: "))
    l2= eval(input("Enter the length 2: "))
    l3 = eval(input("Enter the length 3: "))
    s = (l1 + l2 +l3) / 2
    x = s*(s - l1)*(s - l2)*(s - l3)
    math.sqrt(x)
    print("The area for the triangle is:",x)


"""
Problem: This function calculates the sum of squares in a given range.
"""


def sumSquares():
    starting_number = eval(input("Enter starting point:"))
    ending_number = eval(input("Enter ending point:"))
    total = 0
    for var in range (starting_number,ending_number + 1):
        total = (var**2 + total)
    print("The sum of squares is:", total)

#end of loop

sumSquares()

"""
Problem: This function calculates the sum of squares in a given range.
"""
def power():
    base = eval(input("Enter the base"))
    exponent = eval(input("Enter the exponent"))
    total = 1
    for var in range(exponent):
        total = total*base
    print("The power of the number is:", total)

#end of loop
power()
