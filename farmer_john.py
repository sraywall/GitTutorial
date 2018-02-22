from tkinter import *
from math import pi
def drawThing():
    """
    Merely draws the image required in a tkinter canvas
    and then waits for user to close window
    """
    root = Tk()
    w = Canvas(root, width=200, height=200)
    w.pack()
    w.configure(background="white")
    w.create_rectangle(50, 50, 150, 150, fill="gray")
    w.create_oval(0,0,100,100, fill="white")
    w.create_oval(100,0,200,100, fill="white")
    w.create_oval(0,100,100,200, fill="white")
    w.create_oval(100,100,200,200, fill="white")
    w.create_rectangle(50, 50, 150, 150)
    w.create_text(45,45,text="A", font = ('Comic Sans MS',10))
    w.create_text(155,45,text="B", font = ('Comic Sans MS',10))
    w.create_text(155,155,text="C", font = ('Comic Sans MS',10))
    w.create_text(45,155,text="D", font = ('Comic Sans MS',10))
    w.create_line(50,50,100,100)

    mainloop()

def calcArea(side):
    """
    calculates the area between 4 circles
    side- the side of square made by circles radii
    diamondarea- the area between 4 circles
    """
    squarea = side ** 2
    r = side / 2
    circlearea = pi * r ** 2
    diamondarea = squarea - circlearea
    return diamondarea
def main():
    drawThing()
    side = float(input("Enter the length of the side of the square: "))
    print("The area of the gray diamond is: {0:0.2f}".format(calcArea(side)))

main()
