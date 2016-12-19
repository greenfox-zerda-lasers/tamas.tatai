#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *

root = Tk()

size = 300
canvas = Canvas(root, width=size, height=size)
canvas.pack()

canvas.create_rectangle(0, 0, size/3, size/3, fill='red')
canvas.create_rectangle(100, 10, size/2, size/2, fill='black')
canvas.create_rectangle(150, 150, size, size, fill='yellow')
canvas.create_rectangle(200, 200, size/4, size/4, fill='purple')

root.mainloop()
