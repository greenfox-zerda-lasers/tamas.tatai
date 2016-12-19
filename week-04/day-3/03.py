#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# create a 300x300 canvas.
# draw its diagonals in green.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

canvas.create_line(0, 0, 300, 300, fill='red')
canvas.create_line(0, 300, 300, 0, fill='green')



root.mainloop()
