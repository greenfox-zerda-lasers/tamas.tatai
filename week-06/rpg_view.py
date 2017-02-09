from tkinter import *
from PIL import Image, ImageTk

# root = Tk()

class GameMap:
    def __init__(self):
        self.tile = 72
        self.root = Tk()
        self.canvas = Canvas(self.root, width=10*72, height=10*72)
        self.canvas.pack()
        self.floorimage = ImageTk.PhotoImage (Image.open('floor.png'))
        self.wallimage = ImageTk.PhotoImage (Image.open('wall.png'))
        self.skeletonimage = ImageTk.PhotoImage (Image.open('skeleton.png'))
        self.bossimage = ImageTk.PhotoImage (Image.open('boss.png'))
        self.characters = { "hero" : None, "boss" : None, "skeletons" : []}
        self.hero_images = { "down": ImageTk.PhotoImage(Image.open("hero-down.png")), "up": ImageTk.PhotoImage(Image.open("hero-up.png")), "left": ImageTk.PhotoImage(Image.open("hero-left.png")), "right": ImageTk.PhotoImage(Image.open("hero-right.png"))}

    def draw_map(self, maplist):
        for row in range(len(maplist)):
            for column in range(len(maplist[row])):

                if maplist[row][column] == 0:
                    self.canvas.create_image(column*72, row*72, image = self.floorimage, anchor = NW)
                else:
                    self.canvas.create_image(column*72, row*72, image = self.wallimage, anchor = NW)

    def create_hero(self, positionx, positiony):
        self.characters["hero"] = self.canvas.create_image(positionx*72, positiony*72, image = self.hero_images["down"], anchor= NW)

    def create_boss(self, positionx, positiony):
        self.characters["boss"] = self.canvas.create_image(positionx*72,positiony*72, image = self.bossimage, anchor = NW)

    def create_skeleton(self, skeleton):
        self.characters["skeletons"].append(self.canvas.create_image(skeleton.position["x"]*72, skeleton.position["y"]*72, image = self.skeletonimage, anchor = NW))

    def create_more_skeletons(self, skeleton_list):
        for skeleton in skeleton_list:
            self.create_skeleton(skeleton)

    def move(self, who, positionx, positiony, index=None):
        if type(index) == int:
            self.canvas.move(self.characters[who][index], positionx*72, positiony*72)
        else:
            self.canvas.move(self.characters[who], positionx*72, positiony*72)

    def mainloop_draw(self):
        self.root.mainloop()
