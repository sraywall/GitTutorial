import os
import time
from random import *
ifile = open("pokemon.txt",'r')
arr =[]
for line in ifile.readlines():
    arr.append(line.strip())

choice = int(input("1: Sequential,2: Random"))
upper = int(input("Enter upper limit of range: "))
lower = int(input("Enter lower limit of range:  "))

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice ==1:
        for i in range(lower,upper+1):
            if randrange(2):
                guess = input("{}:".format(i+1))
                if guess == arr[i]:
                    print("Correct!")
                    input()
                else:
                    print("Wrong!",arr[i])
                    input()
            else:
                guess = int(input("{}:".format(arr[i])))
                if guess == i+1:
                    print("Correct!")
                    input()
                else:
                    print("Wrong!",i+1)
                    input()
            os.system('cls' if os.name == 'nt' else 'clear')
    else:
        while True:
            if randrange(2):
                answer  = randint(lower,upper)
                guess = int(input("{}:".format(arr[answer-1])))
                if guess == answer :
                    print("Correct!")
                    input()
                else:
                    print("Wrong!",answer)
                    input()
            else:
                num  = randint(lower,upper)
                answer = arr[num-1]
                guess = input("{}:".format(num))
                if guess == answer:
                    print("Correct!")
                    input()
                else:
                    print("Wrong!",answer)
                    input()
            os.system('cls' if os.name == 'nt' else 'clear')
