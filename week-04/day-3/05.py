#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

from tkinter import *

root = Tk()

size = 300
canvas = Canvas(root, width=size, height=size)
canvas.pack()

#line1 = canvas.create_line(0, 0, 150, 150, fill='red')

def line_draw(x, y):
    return canvas.create_line(x, y, x+50, y)

line_draw(20, 10)
line_draw(50, 80)
line_draw(30, 90)

root.mainloop()
