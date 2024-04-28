import pygame
import sys
import char
from levels import Levels


class Game:
    """ Overall class to manage game aspects """

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fps = int(60)
        self.bg_color = (0, 0, 0)
        self.screen = pygame.display.set_mode((1152, 672))
        pygame.display.set_caption('batur hamzagulari')

        #level
        self.levels = Levels(self.screen)

        #player
        self.player = char.Char(self.levels, self.screen)








        #self.collisiontest = pygame.Rect(180, 280, 300, 50)

    def running(self):
        """
        main loop of game
        """

        while True:
            #self.screen.fill((14, 219, 248))
            # self.screen.blit(pygame.image.load('data/img/jump.png'), (100, 200))

            #pygame.draw.rect(self.screen, (0, 0, 0), self.collisiontest, 1)

            self.checkevents()
            self.levels.render()

            self.player.update()
            self.player.render()


            pygame.display.update()
            self.clock.tick(60)

    def checkevents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quit")
                pygame.quit()
                sys.exit()



if __name__ == "__main__":
    Game = Game()
    Game.running()