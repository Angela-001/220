"""
Name: Angela Nganga
traffic.py

Problem: This function analyzes traffic patterns.

Certification of Authenticity:
I certify that this assignment is entirely my own work, but I discussed it with tutors at the CSL.
"""

def main():
    total1 = 0
    roads = eval(input("How many roads were surveyed? "))
    for i in range(roads):
        days = eval(input("How many days was road " + str(i+1) + " surveyed? "))
        total = 0
        for k in range(days):
            cars = eval(input("How many cars travelled on day " + str(k+1) + "?"))
            total += cars
        average = total/days
        total1 += total
        print("Road" + str(i+1) + " average vehicles per day: ", round(average,1))
    average1 = total1/roads
    print("Total number of vehicles traveled on all roads: ", total1)
    print("Average number of vehicles per road: ", (round(average1,2)))

if __name__ == '__main__':
    main()
