# greyscale.py

from graphics import *

def main():  
    infileName = input("File name: ")  
    temp = Image(Point(100,100), infileName)
    width = temp.getWidth()
    height = temp.getHeight()
    image = Image(Point(round(width/2),round(height/2)), infileName)
    win = GraphWin(height=200,width=200)
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
    entry = Entry(Point(50,50),10)
    entry.draw(win)
    label = Text(Point(50,25),"Save As:")
    label.draw(win)
    while True:
        key = win.getKey()
        if key == "Return" :break
    label.undraw()
    entry.undraw()
    txt = entry.getText()
    image.save(txt)
    win.getMouse()
    win.close()
if __name__ == "__main__":
    main()
