import random

class Mapinfo:
    def __init__(self):
        self.tilemap = [
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0]
        ]

        self.skeleton_list = []

    def add_more_skeleton(self):
        for _ in range(random.randint(3,7)):
            skeleton = Skeleton()
            self.skeleton_list.append(skeleton)
        return self.skeleton_list


class Character:
    def __init__(self):
        self.health_point = 0
        self.defense_point = 0
        self.strike_point = 0
        self.d6roll = random.randint(1, 6)

class Hero(Character):
    def __init__(self):
        super().__init__()
        self.position = {"x" : 0, "y" : 0}

class Skeleton(Character):
    def __init__(self): ###########??
        self.map_info = Mapinfo()
        self.position = {"x": 0, "y" : 0}
        self.skeletons_stop_at_walls()
        self.monster_direction = ((0,1), (0,-1), (1,0), (-1,0))

    def skeletons_stop_at_walls(self):
        positionx = random.randint(0,9)
        positiony = random.randint(0,9)
        if  self.map_info.tilemap[positiony][positionx] != 1:
            self.position["x"] = positionx
            self.position["y"] = positiony
        else:
            self.skeletons_stop_at_walls()
