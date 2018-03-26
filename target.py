# target.py
from graphics import *
from math import sqrt


class Target:
    def __init__(self, win, shot, x, height, width):
        self.win = win
        self.shot = shot
        self.x = x
        self.height = height
        self.width = width

        p1 = Point(self.x,self.height)
        p2 = Point(self.x+self.width,0)
        
        self.rect = Rectangle(p1,p2)
        self.rect.draw(win)

    def collide(self):
        return self.shot.getY() <= self.height and\
                            self.shot.getX() >= self.x
