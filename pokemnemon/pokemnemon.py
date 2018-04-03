#! /usr/bin/env python3
from sys import argv
import os
import time
from random import *
fname = argv[1]
ifile = open(fname,'r')
arr =[]
for line in ifile.readlines():
    arr.append(line.strip())

choice = int(input("1: Sequential,2: Random: "))
lower = int(input("Enter lower limit of range:  "))
upper = int(input("Enter upper limit of range: "))
shuffle = True
if choice == 2:
    numquestions = int(input("Enter how many questions: "))
missed = {}
numcorrect = 0

def checkanswer(ans,hint):
    if shuffle:
        if randrange(2):
            ans,hint = hint,ans
    answer = input("{}:".format(hint))
    if str(ans) == answer:
        print("Correct!")
        global numcorrect
        numcorrect += 1
    else:
        print("Wrong!",ans)
        missed[hint] = str(ans)
    input()

os.system('cls' if os.name == 'nt' else 'clear')
if choice ==1:
    while True:
        for i in range(lower,upper+1):
            checkanswer(arr[i-1],i)
            os.system('cls' if os.name == 'nt' else 'clear')
else:
    for q in range(numquestions):
        print("Question",q)
        num = randrange(lower,upper)
        checkanswer(num+1,arr[num])
        os.system('cls' if os.name == 'nt' else 'clear')

print("Correct : ","{}/{}".format(numcorrect,numquestions))
print(missed)
