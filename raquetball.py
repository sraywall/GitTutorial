#raquetball.py
# simulates a raquetball game with Monte Carlo
from random import random
prob1 = float(input("Enter win probability for player1: "))
prob2 = float(input("Enter win probability for player2: "))
p1serves = True
pointsp1 = 0
pointsp2 = 0
winsp1 = 0
winsp2 = 0
for i in range(5000):
    pointsp1 = 0
    pointsp2 = 0
    p1serves = True
    while True:
        if p1serves:
            if random() < prob1:
                pointsp1 += 1
            else:
                p1serves = False
        else:
            if random() < prob2:
                pointsp2 += 1
            else:
                p1serves = True
        if(pointsp1 == 15):
            #print("Player 1 wins")
            winsp1 += 1
            break
        if(pointsp2 == 15):
            #print("Player 2 wins")
            winsp2 += 1
            break

print("Player 1 won:",winsp1,"Player 1 won:",winsp2)
