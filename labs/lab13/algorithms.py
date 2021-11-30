"""
Name: Angela Nganga
algorithms.py
Problem: This program uses while control structures and lists
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def read_data(filename):
    infile = open(filename, "r")
    eachline = infile.read()
    eachline = eachline.split()
    i = 0
    while i < len(eachline):
        eachline[i] = eval(eachline[i])
        i = i+1
    infile.close()
    return eachline

def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val == values[i]:
            return True
        else:
            i = i + 1
    return False


def is_in_binary(search_val, values):
    high = len(values)-1
    low = 0
    while low <= high:
        half = (low+high)//2
        if values[half] > search_val:
            high = half-1
        elif values[half] == search_val:
            return True
        else:
            low = half+1
    return False

def selection_sort(values):
    for num in range(len(values)):
        mini = num
        for i in range(num, len(values)):
            if values[i] < values[mini]:
                mini = i
        temp = values[num]
        values[num] = values[mini]
        values[mini] = temp
        print(values)


def calc_area(rect):
    point1 = rect.getP1()
    point2 = rect.getP2()
    p1x1 = point1.getX()
    p1x2 = point2.getX()
    p2y1 = point1.getY()
    p2y2 = point2.getY()

    rect_len = abs(p1x1 - p1x2)
    rect_width = abs(p2y1 - p2y2)
    r_area = rect_len * rect_width
    return r_area

def rect_sort(rectangles):
    for num in range(len(rectangles)):
        min_area = num
        for i in range(num, len(rectangles)):
            if calc_area(rectangles[i]) < calc_area(rectangles[min_area]):
                min_area = i
        temp = rectangles[num]
        rectangles[num] = rectangles[min_area]
        rectangles[min_area] = temp












