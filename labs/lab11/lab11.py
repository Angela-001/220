"""
Name: Angela Nganga
Hangman.py
Problem: This program reads from a file, uses functions and uses decision and repetition to solve a problem.
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

from random import randrange

def readfile(wordlist):
    fromfile = open(wordlist, "r")
    file1 = fromfile.readlines() #lower in for loop
    for i in range(len(file1)):
        file1[i] = file1[i].lower()
    fromfile.close()
    return file1


def secretword(wordlist):
    lengthlist = len(wordlist)

    randword = wordlist[randrange(-1, lengthlist)]#reterns a string
    return randword

def guessed_word(userguess, randword, pastguess, newword):

    for i in range(len(randword)):
        if userguess == randword[i]:
            newword[i] = userguess

    return "".join(newword)#concatenetes a list into a string





def spellword(randword, newword):
    if randword == newword:
        return True
    else:
        return False



def main():
    getword = secretword(readfile("wordlist.txt"))
    acc = 0
    pastempty = ""
    total = ""
    newword = []
    for i in range(len(getword)):
        newword.append("_")
    #if i not in getword:
    while acc < 7:
        ask_user = input("Guess a letter: ")
        if ask_user not in getword:
            acc = acc+1
            pastempty = ask_user + pastempty

        if ask_user in getword:
            get_new = guessed_word(ask_user, getword, pastempty, newword)
            print(get_new)

        if spellword(getword, get_new):
            acc = 7
        print(7-acc, "Guesses left")

    pass

# list
# World
# Lists
# And
# Lost




main()
