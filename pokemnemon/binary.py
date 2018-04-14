#!/usr/bin/python3
import os
from random import randint
from random import randrange
ifile = open("pokemon.txt")

arr = [line.strip() for line in ifile.readlines()]
shuffle = True
#for line in arr:
    #print(line,end="")

def checkAnswer(q,a):
    os.system('clear')
    global shuffle
    if shuffle:
        if randrange(2):
            q,a=a,q
    guess = input("{}: ".format(q))
    if guess == a:
        print("Correct!")
    else:
        print("Wrong!",a)
    input()

lower = int(input("Enter the lower range of questions: "))
upper = int(input("Enter the upper range of questions: "))
numq = int(input("Enter the number of questions: "))

for i in range(numq):
    r = randint(lower,upper)
    q = bin(r)[2:].zfill(8)
    checkAnswer(q,arr[r].strip()) 
