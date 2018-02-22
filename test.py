# Program: triangle2.py
import math
from graphics import *

def square(x):
    return x ** 2

def distance(p1,p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist

# Heron's formula
def triangleArea(a,b,c):
    s = (a + b + c) / 2
    area = math.sqrt(s*(s - a)*(s - b)*(s - c))
    return area

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5,0.5), "Click on three points")
    message.draw(win)

    # Get and draw three verices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    #Use Polygon object to draw the triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Calculate the perimeter of the triangle
    a = distance(p1,p2)
    b = distance(p2,p3)
    c = distance(p3,p1)
    #print("A:",a,"B:",b,"C:",c)
    perim = a + b + c
    area = triangleArea(a,b,c)
    message.setText("Perimeter: {0:0.2f}".format(perim)+"Area: {0:0.2f}".format(area))

    # Wait for another click to exit
    win.getMouse()
    win.close()

main()
