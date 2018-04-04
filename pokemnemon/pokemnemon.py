#! /usr/bin/env python3
import time
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
qtype = int(input("1:Name, 2:Alphabet, 3:Binary, 4:Hex: "))
shuffle = True
if choice == 2:
    numquestions = int(input("Enter how many questions: "))
else:
    numquestions = upper - lower + 1
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
begin = time.time()
os.system('cls' if os.name == 'nt' else 'clear')
if choice ==1:
    for i in range(lower,upper+1):
        q,a = arr[i-1],i
        if qtype == 3:
            q = bin(i)[2:].zfill(8)
        elif qtype == 4:
            q = hex(i)[2:].zfill(8)
        checkanswer(q,a)
        os.system('cls' if os.name == 'nt' else 'clear')
else:
    for i in range(numquestions):
        print("Question",i)
        num = randrange(lower,upper)
        q,a = num+1,arr[num]
        if qtype == 3:
            a = bin(q)[2:].zfill(8)
        elif qtype == 4:
            a = hex(q)[2:].zfill(8)
        checkanswer(q,a)
        os.system('cls' if os.name == 'nt' else 'clear')

print("Correct : ","{}/{}".format(numcorrect,numquestions))
print("Time: {} seconds".format(time.time()-begin))
print(missed)
