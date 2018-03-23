#random_walk.py
"""
Stephen Wall CS1400 Random Walk 3/17/18

Program that takes 1 pixel steps in random directions
beginning at the origin.  The number of steps is user
defined and total distance traveled and distance between
origin and final position are displayed in the console
while the path traveled is rendered in tkinter

Some major steps were spiral design, an accumulator pattern,
a distance formula, error handling

Lessons Learned:
    *getting a small part working and building on that is good practice
    *print function can be put on mulitple lines to prevent long lines
    *functions that are used many times should be tested before repeated use

"""

from random import random
from math import cos,sin,pi,sqrt
from graphics import *
from tkinter import *

def distance(p1,p2):
    dist = sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2)
    return dist

def main():
    steps = None
    while steps is None:
        try:
            steps = int(input("Enter the number of steps: "))
        except ValueError:
            print("Enter a valid integer")

    x,y = 100,100
    win = GraphWin("Random Walk",200,200)
    initial = Point(x,y)
    initial.draw(win)
    point = None
    total= 0

    for i in range(steps):
        prevpoint = Point(x,y)
        angle = random() * 2 * pi
        x += cos(angle)
        y += sin(angle)
        point = Point(x,y)
        Line(prevpoint,point).draw(win)
        total+= distance(prevpoint,point)

    print("Actual distance:",round(total),"Straight-line distance:",
                                    round(distance(initial,point)))
    mainloop()

if __name__ == "__main__":
    main()
