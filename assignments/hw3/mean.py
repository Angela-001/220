"""
Name: Angela Nganga
mean.py

Problem: This function outputs the RMS average,the Harmonic mean, and the geometric mean.

Certification of Authenticity:
I certify that this assignment is entirely my own work, but I discussed it with tutors at the CSL.
"""

import math
def main():
    total2 = 0
    total3 = 0
    total4 = 1
    n = eval(input("enter the number of values to be entered: "))
    for i in range(n):
        x = eval(input("enter value: "))
        total2 = total2 + x**2
        total3 = total3 + (1 / x)
        total4 = (total4 * x)
    average2 = total2 / n
    print(round(math.sqrt(average2), 3))
    average3 = n / total3
    print(round(average3, 3))
    average4 = (total4) ** (1 / n)
    print(round(average4, 3))

if __name__ == '__main__':
    main()
