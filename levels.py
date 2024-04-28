import pygame
import os
from platforms import Platforms


class Level:
    def __init__(self, screen, level_id):
        self.screen = screen
        self.level_id = level_id
        self.platform = Platforms().load(self.level_id)
        self.items = None
        self.image = pygame.image.load(os.path.join('data', 'img', "lol" + str(level_id) + '.png'))

        print("good job lilbro")

        self.x, self.y = 0, 0
        self.width, self.height = self.image.get_size()

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def render(self):
        self.screen.blit(self.image, self.rect)


class Levels:
    def __init__(self, screen):
        self.screen = screen
        self.max_levels = 2
        self.current_level = 1
        self.levels = {}
        self.load_levels()

    def load_levels(self):
        for i in range(1, self.max_levels + 1):
            self.levels[i] = Level(self.screen, i)

    def render(self):
        current_level = self.levels[self.current_level]
        self.screen.blit(current_level.image, current_level.rect)

        # for platform in current_level.platform:
        #     pygame.draw.rect(self.screen, (0,0,0), platform.rect)
