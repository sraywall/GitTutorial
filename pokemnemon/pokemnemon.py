#! /usr/bin/env python3
import time
from sys import argv
import os
import time
from random import *
#fname = argv[1]
ifile = open("pokemon.txt",'r')
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
def tests():
    global missed
    missed = {}
    global numcorrect
    numcorrect = 0
    begin = time.time()
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice ==1:
        for i in range(lower,upper+1):
            q,a = arr[i],i
            if qtype == 3:
                a = bin(i)[2:].zfill(8)
            elif qtype == 4:
                a = hex(i)[2:].zfill(8)
            checkanswer(q,a)
            os.system('cls' if os.name == 'nt' else 'clear')
    else:
        for i in range(numquestions):
            print("Question",i)
            num = randrange(lower,upper)
            q,a = arr[num],num
            if qtype == 3:
                a = bin(num)[2:].zfill(8)
            elif qtype == 4:
                a = hex(num)[2:].zfill(8)
            checkanswer(q,a)
            os.system('cls' if os.name == 'nt' else 'clear')

    print("Correct : ","{}/{}".format(numcorrect,numquestions))
    seconds = time.time()-begin
    minutes = int(seconds) // 60
    seconds %= 60
    print("Time:{} minutes {} seconds".format(minutes,seconds))
    print(missed)
    input()
tests()
again = True
while again:
    again = bool(input("Again? "))
    if again:
        tests()
