from rpg_view import GameMap
from rpg_model import Mapinfo, Character, Hero, Skeleton
import random

class MainControl:
    def __init__(self):

        self.viewGameMap = GameMap()
        self.map_info = Mapinfo()
        self.hero_data = Hero()
        self.skeleton_data = Skeleton()
        self.model_data_Game = Character()
        self.skeleton_list = []

        self.viewGameMap.draw_map(self.map_info.tilemap)
        self.viewGameMap.create_hero(self.hero_data.position["x"], self.hero_data.position["y"])
        self.viewGameMap.create_skeleton(self.skeleton_data)
        self.viewGameMap.create_more_skeletons(self.skeleton_list)
        self.viewGameMap.create_boss(7,5)

        self.movement_indexer = 0

        self.character_step()
        self.viewGameMap.canvas.focus_set()
        self.viewGameMap.mainloop_draw()

    def skeleton_creator(self):
        for skeleton in range(3, 6):
            skeleton = Skeleton()
            self.skeleton_list.append(skeleton)

    def character_step(self):
        self.viewGameMap.canvas.bind("<w>", self.growth)
        self.viewGameMap.canvas.bind("<a>", self.growth)
        self.viewGameMap.canvas.bind("<s>", self.growth)
        self.viewGameMap.canvas.bind("<d>", self.growth)

    def growth(self, event):
        self.movement_indexer += 1
        self.move_enemies()
        print(self.hero_data.position["x"],self.hero_data.position["y"])

        if event.keysym == "w":
            self.move_up()
        if event.keysym == "s":
            self.move_down()
        if event.keysym == "d":
            self.move_right()
        if event.keysym == "a":
            self.move_left()

    def move_down(self):
        if self.wall_checker(self.hero_data.position["x"], self.hero_data.position["y"]+1):
            self.hero_data.position["y"]+=1
            self.viewGameMap.move("hero", 0, 1)
        self.viewGameMap.canvas.itemconfigure(self.viewGameMap.characters["hero"], image = self.viewGameMap.hero_images["down"])

    def move_up(self):
        if self.wall_checker(self.hero_data.position["x"], self.hero_data.position["y"]-1):
            self.hero_data.position["y"] -= 1
            self.viewGameMap.move("hero",0,-1)
        self.viewGameMap.canvas.itemconfigure(self.viewGameMap.characters["hero"], image = self.viewGameMap.hero_images["up"])

    def move_right(self):
        if self.wall_checker(self.hero_data.position["x"]+1, self.hero_data.position["y"]):
            self.hero_data.position["x"] += 1
            self.viewGameMap.move("hero",1,0)
        self.viewGameMap.canvas.itemconfigure(self.viewGameMap.characters["hero"], image = self.viewGameMap.hero_images["right"])


    def move_left(self):
        if self.wall_checker(self.hero_data.position["x"]-1, self.hero_data.position["y"]):
            self.hero_data.position["x"] -= 1
            self.viewGameMap.move("hero",-1,0)
        self.viewGameMap.canvas.itemconfigure(self.viewGameMap.characters["hero"], image = self.viewGameMap.hero_images["left"])

    def move_enemies(self):
        if self.movement_indexer % 2 == 0:
            x,y = random.choice(self.skeleton_data.monster_direction)

            if self.wall_checker(self.skeleton_data.position["x"]+x, self.skeleton_data.position["y"]+y):
                self.skeleton_data.position["x"] += x
                self.skeleton_data.position["y"] += y
                self.viewGameMap.move("skeletons", x, y)


    def wall_checker(self, positionx, positiony):
        if len(self.map_info.tilemap)-1 < positiony or  positiony < 0:
            return False
        elif len(self.map_info.tilemap)-2 < positionx or positionx < 0:
            return False
        elif (self.map_info.tilemap[positiony][positionx] == 1 ):
            return False
        else:
            return True


game = MainControl()
