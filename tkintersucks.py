from tkinter import *

root = Tk()
canvas = Canvas(root, width=200, height=200)
canvas.pack()
canvas.create_line(50,50,100,100)
mainloop()
