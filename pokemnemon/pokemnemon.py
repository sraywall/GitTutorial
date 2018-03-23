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

choice = int(input("1: Sequential,2: Random"))
upper = int(input("Enter upper limit of range: "))
lower = int(input("Enter lower limit of range:  "))

def checkanswer(ans,hint):
    answer = input("{}:".format(hint))
    if str(ans) == answer:
        print("Correct!")
    else:
        print("Wrong!",ans)
    input()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice ==1:
        for i in range(lower,upper+1):
            if randrange(2):
                checkanswer(arr[i-1],i)
            else:
                checkanswer(i,arr[i-1])
            os.system('cls' if os.name == 'nt' else 'clear')
    else:
        while True:
            num = randrange(lower,upper)
            if randrange(2):
                checkanswer(num+1,arr[num])
            else:
                checkanswer(arr[num],num+1)
            os.system('cls' if os.name == 'nt' else 'clear')
