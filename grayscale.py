# grayscale.py
# takes a ppm image and converts it to grayscale
from tkinter import *
from graphics import *
def main():
    infile = open(input("Enter a file name: "))
    header = infile.readline()
    line = infile.readline()
    while line:
        columns = line.split()
        for r,g,b in columns:
            brightness = int(round(.299*r + .587*g + .114*b))
            
        line = infile.readline()
        

if __name__ == "__main__":
    pass
        #main()
        
win = GraphWin()
img =Image(Point(0,0),"marbles.ppm")
img.draw(win)
mainloop()
