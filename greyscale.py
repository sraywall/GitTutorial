# grayscale.py

from graphics import *

def main():  
    infileName = input("File name: ")  
    outfileName = input("Save to: ")
    #temp = Image(Point(100,100), infileName)
    #image = Image(Point(temp.getWidth()/2,temp.getHeight()/2), infileName)
    image = Image(Point(100,100), infileName)
    width = image.getWidth()
    height = image.getHeight()
    win = GraphWin("rgb",height=200,width=200)
    image.draw(win)

    win.getMouse()

    for row in range(width):
        for column in range(height):
            r, g, b = image.getPixel(column, row)
            brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            image.setPixel(column, row, color_rgb(brightness, brightness, brightness))
            #p = Point(column,row).draw(win)
            #p.setFill(color_rgb(brightness, brightness, brightness))
            win.update()

    win.getMouse()
    win.close()
main()
