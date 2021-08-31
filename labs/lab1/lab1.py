"""
Name: <Angela Nganga>
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_area() :
    length = 20
    width = 5
    area = length * width
    print("Area =", area)
    """
    Name: <Angela Nganga>
    lab1.py
    
    Problem: This function calculates the area of a rectangle
    """


def calc_rec_area() :
    length = eval (input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

"""
Name: <Angela Nganga>
lab1.py

Problem: This function calculates the volume of a rectangle
"""


def calc_rec_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

"""
Name: <Angela Nganga>
lab1.py

Problem: This function calculates the shooting percentage
"""


def calc_rec_percentage():
    total_shots = eval(input("Enter the total_shots: "))
    shots_made = eval(input("Enter the shots_made: "))
    shooting_percentage =(shots_made / total_shots) * 100
    print("Shooting_percentage =", shooting_percentage)
""" 
Name: <Angela Nganga>
lab1.py

Problem: This function calculates the cost of shipping a coffee order
"""



def coffee():
    coffee_cost = 10.50
    shipping_cost = 0.86
    fixed_cost= 1.50
    pounds_of_coffee = eval(input("Enter the pounds of coffee: "))
    shipping_cost = (coffee_cost + shipping_cost ) * pounds_of_coffee + fixed_cost
    print("shipping cost=", shipping_cost)

"""
Name: <Angela Nganga>
lab1.py

Problem: This function calculates the number of kilometers to miles
"""


def kilometers_to_miles() :
    mile = 1.61
    kilometers = eval(input("Enter the number of kilometers: "))
    miles = (kilometers / mile)
    print(" kilometers to miles=", miles )