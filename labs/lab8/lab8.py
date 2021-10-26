"""
Name: Angela Nganga
functions.py
Problem: This program writes functions.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from encryption import encode

def number_words(Walrus, out1):
    read_file = open(Walrus, "r")
    write_file = open(out1, "w")
    lines = read_file.readlines()
    total = 0
    for each_line in lines:
        split_space = each_line.split()
        for i in range(len(split_space)):
            total = total + 1
            print(total, split_space[i], end="\n", file=write_file)
    read_file.close()
    write_file.close()

def hourly_wages(hourly_wages, out2):
    read_file = open(hourly_wages, "r")
    write_file = open(out2, "w")
    lines = read_file.readlines()
    for each_line in lines:
        split_space = each_line.split()
        split_space[2] = float(split_space[2]) + 1.65
        print(split_space[0], split_space[1], split_space[2], file=write_file )

    read_file.close()
    write_file.close()

def calc_check_sum(isbn):
    string = "10,9,8,7,6,5,4,3,2,1"
    pos = string.split(",")
    acc= 0
    for i in range(10):
        each = int(isbn[i])*int(pos[i])
        acc = acc + each

    print(acc)


def send_message(message, bob):
    read_file = open(message, "r")
    file_name = bob + ".txt"
    write_file = open(file_name, "w")
    file_content = read_file.read()
    print(file_content, file=write_file)

    write_file.close()
    read_file.close()


def send_safe_message(message, bob, key):
    read_file = open(message, "r")
    file_name = bob + ".txt"
    file_contents = read_file.read()
    write_file = open(file_name, "w")
    new_encoded = encode(file_contents, key)
    print(new_encoded, file=write_file)


    write_file.close()
    read_file.close()


def main():
    number_words("Walrus.txt", "out1")
    hourly_wages("hourly_wages.txt", "out2")
    calc_check_sum("0072946520")
    send_message("message.txt", "Alice")
    send_safe_message("safest_message.txt", "bob", 3)
    pass


main()
