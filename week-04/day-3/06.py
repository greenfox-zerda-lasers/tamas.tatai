#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# create a 300x300 canvas.
# draw a green 10x10 square to its center.

from tkinter import *

root = Tk()

size = 300
canvas = Canvas(root, width=size, height=size)
canvas.pack()

canvas.create_rectangle(145, 145, 155, 155, fill = 'green')

root.mainloop()
