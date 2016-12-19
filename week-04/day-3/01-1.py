#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# create a 300x300 black canvas.
# draw a red horizontal line to its middle.
# draw a green vertical line to its middle.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

canvas.create_rectangle(0, 0, 300, 300, fill='black')
canvas.create_line(0, 150, 300, 150, fill='red')
canvas.create_line(150, 0, 150, 300, fill='green')
#olive_oval = canvas.create_oval(120, 10, 180, 90, fill='olive drab')

root.mainloop()
