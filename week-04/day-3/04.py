#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *

root = Tk()

size = 300
canvas = Canvas(root, width=size, height=size)
canvas.pack()

#line1 = canvas.create_line(0, 0, 150, 150, fill='red')

def line_draw(x, y):
    return canvas.create_line(x, y, size/2, size/2)

line_draw(20, 20)
line_draw(50, 10)
line_draw(0, 120)

root.mainloop()
