#simulates a roll of 5 dice and
#counts how many times yahtzee
from random import randrange
numyahtzees = 0
for j in range(5000):
    initial = randrange(1,7)
    equal = True
    for i in range(4):
        equal = (initial == randrange(1,7)) and equal

    if equal:
        print("yahtzee!","of",initial)
        numyahtzees += 1

print("number of yahtzees:",numyahtzees)
