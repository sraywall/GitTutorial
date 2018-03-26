#volleyball.py
# simulates a volleyball game with Monte Carlo
from random import random
prob1 = float(input("Enter win probability for player1: "))
prob2 = float(input("Enter win probability for player2: "))
numgames = int(input("Enter number of games to simulate: "))
p1serves = True
pointsp1 = 0
pointsp2 = 0
winsp1 = 0
winsp2 = 0
for i in range(numgames):
    pointsp1 = 0
    pointsp2 = 0
    p1serves = True
    while True:
        if p1serves:
            if random() < prob1:
                pointsp1 += 1
            else:
                p1serves = False
                pointsp2 += 1
        else:
            if random() < prob2:
                pointsp2 += 1
            else:
                p1serves = True
                pointsp1 += 1
        if(pointsp1 == 25):
            #print("Player 1 wins")
            winsp1 += 1
            break
        if(pointsp2 == 25):
            #print("Player 2 wins")
            winsp2 += 1
            break

print("Player 1 won:",winsp1,"Player 2 won:",winsp2)
