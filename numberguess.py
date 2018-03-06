#numberguess.py
#asks for a user input
#as a guess for a number on a range

from random import *
from collections import *

limit = 100
numiterations = 100000
dic = defaultdict(int)
for i in range(numiterations):
    correctanswer = randrange(1,limit+1)
    #correctanswer = 100
    while True:
        guess = limit // 2
        minguess = 0
        maxguess = 0
        guess = randrange(1,limit+1)
        guesses = [guess]
        #print("correct answer",correctanswer)
        half = limit - guess
        count = 0
        while True:
            #num = int(input("Guess a number: "))
            #print("Guess is:",guess)
            count += 1
            half -= half // 2
            if(guess > correctanswer):
                #print("Too high")
                #guess -= half
                maxguess = guess
            elif(guess < correctanswer):
                #print("Too low")
                #guess += half
                minguess = guess
            else:
                #print("Correct answer")
                break
            guess = randrange(minguess+1, maxguess or (limit + 1))
            guesses.append(guess)
            if len(guesses)>= 20:
                print(guesses)

        dic[count]+=1
        #print("Number of guesses:",count)
        break
for  i in range(1,limit + 1):
    print("Number of times guessed in ",i,"guesses:",dic[i])
