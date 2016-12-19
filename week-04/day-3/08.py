#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

size = 300
canvas = Canvas(root, width=size, height=size)
canvas.pack()

#line1 = canvas.create_line(0, 0, 150, 150, fill='red')

def draw_rect(x, y):
    return canvas.create_rectangle(x, y, x+50, y+50)

draw_rect(120, 20)
draw_rect(80, 40)
draw_rect(40, 80)


root.mainloop()
