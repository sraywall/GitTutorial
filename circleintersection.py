# a program that computes the intersection of a circle with a horizontal
# line and displays the information textually and graphically.
from graphics import *
from tkinter import *
from math import *

def main():
    radius = float(input("Enter the radius: "))
    y = float(input("Enter the y-intercept: "))
    win = GraphWin()
    win.setCoords(-10,-10, 10.0, 10.0)
    circle = Circle(Point(0,0),radius)
    circle.draw(win)
    line = Line(Point(-10,y),Point(10,y))
    line.draw(win)
    try:
        x1 = sqrt(radius ** 2 - y ** 2)
        x2 = -sqrt(radius ** 2 - y ** 2)
        p1 = Point(x1,y)
        p2 = Point(x2,y)
        p1.draw(win)
        p2.draw(win)
        p1.setFill("red")
        p2.setFill("red")
    except ValueError:
        print("Line does not intersect the circle!")
    mainloop()
if __name__ == "__main__":
    main()
