#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

canvas.create_line(10, 10, 300, 10, fill='red')
canvas.create_line(10, 10, 10, 300, fill='green')
canvas.create_line(10, 300, 300, 300, fill='blue')
canvas.create_line(300, 10, 300, 300, fill='brown')


root.mainloop()
