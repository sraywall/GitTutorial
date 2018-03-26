from tkinter import *
from graphics import *
from projectile import Projectile
from button import Button
def main():


    # create animation window
    win = GraphWin("Projectile Animation",640,480, autoflush=False)
    win.setCoords(-10,-10,210,155)

    qb = Button(win, Point(100,100), 100,100, "Poop")
    qb.activate()

    # draw baseline
    Line(Point(-10,0), Point(210,0)).draw(win)

    # draw labeled ticks every 50 meters
    for x in range(0,210,50):
        Text(Point(x,-5), str(x)).draw(win)
        Line(Point(x,0), Point(x,2)).draw(win)
    mainloop()

if __name__ == "__main__":
    main()
