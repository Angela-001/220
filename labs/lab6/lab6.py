"""
Name: Angela Nganga
elementary_strings.py
Problem: This function analyzes strings as a sequence.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
   name = input("Enter a person's name in first-last order: ")
   split1 = name.split()
   first = split1[0]
   last = split1[1]
   print(last + ", " + first)

def company_name():
    name = input("Enter a three-part internet domain name here: ")
    split2 = name.split(".")
    print(split2[1])


def initials():
    number = input("Enter how many names will be input: ")
    for i in range(len(number)):
        first = input("Enter the first name of student " + str(i + 1))
        last = input("Enter" + first + "'s last name")
        first_letter = first[0]
        last_letter = last[0]
        capital = first_letter.capitalize()
        capital2 = last_letter.capitalize()
        print(capital + capital2, end="")


def names():
    list_of_names = input("Enter a list of names , first and last only, seperated by commas: ")
    individual = list_of_names.split(",")
    for i in range(len(individual)):
        first1 = individual[i]
        each_name = first1.split()
        first_name = each_name[0]
        last_name = each_name[1]
        first_letter = first_name[0]
        second_letter = last_name[0]
        print(first_letter + " " + second_letter,end="")


def thirds():

    no_sentences = eval(input("Enter the number of sentences to be inputed: "))
    for i in range(len(no_sentences)):
        sentence = input("Enter sentence " + str(i+1) +" here")
        for j in range(2,len(sentence),3):
            print(sentence[j])


def word_average():
    sentence = eval(input("Type in a sentence here: "))
    total = 0
    words = sentence.split()
    for i in range(len(words)):
        each_word = words[i]
        total = total + len(each_word)
        average = total / len(words)
    print(average)


def pig_latin():
    sentence1 = input("Type in a sentence here: ")
    split_sent = sentence1.split()
    for i in range(len(split_sent)):
        word = split_sent[i]
        first_letter = word[0]
        rest_letters = word[1:]

        print((rest_letters + first_letter +"ay").lower(), end=" ")




def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()



main()
