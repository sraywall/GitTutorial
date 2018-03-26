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
if choice == 2:
    numquestions = int(input("Enter how many questions: "))
numcorrect = 0
missed = {}

def checkanswer(ans,hint):
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
            if randrange(2):
                checkanswer(arr[i-1],i)
            else:
                checkanswer(i,arr[i-1])
            os.system('cls' if os.name == 'nt' else 'clear')
else:
    for q in range(numquestions):
        print("Question",q)
        num = randrange(lower,upper)
        if randrange(2):
            checkanswer(num+1,arr[num])
        else:
            checkanswer(arr[num],num+1)
        os.system('cls' if os.name == 'nt' else 'clear')

print("Correct : ","{}/{}".format(numcorrect,numquestions))
global numcorrect
print(missed)
