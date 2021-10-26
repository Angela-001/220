"""
Name: Angela Nganga
weighted_average.py

Problem: This program uses numerical data from a text file.
Certification of Authenticity:
I certify that this assignment is entirely my own work, however I discussed it with tutors at the CSL.
"""


def weighted_average(grades, avg):
    read_file = open(grades, "r")
    write_file = open(avg, "w")
    lines = read_file.readlines()
    for each_line in lines:
        split_colon = each_line.split(":")
        w_g = split_colon[1]
        w_g = w_g.split()
        total = 0
        w = 0
        for i in range(len(w_g)//2):
            w = w + int(w_g[2*i])
            total = total + int(w_g[2*i]) * int(w_g[2*i+1])
        average = total /100
        if w > 100:
            print(split_colon[0] + "'s average: Error: The weights are more than 100.", file=write_file)
        elif w < 100:
            print(split_colon[0] + "'s average: Error: The weights are less than 100.",file=write_file)
        else:
            print("{0}'s average: {1}".format(split_colon[0], round(average, 1)), file=write_file)


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == '__main__':
    main()


