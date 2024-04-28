import pygame


class Hitboxes():
    def __init__(self):
        self.levels = {}
        # self.levels[1] = [(166,130,218,57),
        #                   (0,291,70,309),
        #                   (69,409,377,191),
        #                   (447,276,153,324)]

        # self.levels[1] = [(352, 185, 128, 175),
        #                   (185, 40, 110, 50),
        #                   (128, 330, 224, 30),
        #                   (8, 184, 120, 107),
        #                   (8, 291, 65, 69),
        #                   (73, 330, 55, 30),
        #                   (0, 0, 8, 360),
        #                   (472, 0, 8, 360)]

        self.levels[1] = [(0,0,0,0)]
        self.levels[2] = [(0,0,0,0)]

        # self.levels[2] = [(296, 296, 95, 38),
        #                   (409, 197, 71, 35),
        #                   (255, 199, 74, 33),
        #                   (119, 103, 74, 65),
        #                   (0, 80, 81, 86),
        #                   (0, 0, 8, 360),
        #                   (472, 0, 8, 360)]


class Platform():
    def __init__(self,x,y,width,height):
        self.x,self.y,self.width,self.height = x,y,width,height

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y,self.width,self.height)


class Platforms():
    def __init__(self):
        self.hitboxes = Hitboxes()

    def load(self, level):
        return [Platform(*hitboxe) for hitboxe in self.hitboxes.levels[level]]
