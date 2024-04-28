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

        self.levels[1] = [(0,0,16,672),(1136,0,16,672),(0,656,1152,16),(16,416,125,239),(142,527,127,128),
                          (304,160,432,127), (256,208,48,79),(224,224,32,63),(1008,112,48,97),
                          (1056,96,80,112),(1041,353,95,15),(1057,529,79,15),(817,529,31,127),
                          (833,465,32,78),(849,401,32,93),(865,353,95,15),(879,465,65,15),(865,353,15,48)]
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
