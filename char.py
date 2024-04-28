import pygame
import math
import os


class Char:
    def __init__(self, levels, screen):
        self.screen = screen
        self.levels = levels
        self.pos = [100, 10]
        self.speed = [1, 0]
        self.collideDown = False
        self.collideUp = False
        self.movement = [0, 0]
        self.image = pygame.image.load(os.path.join('data', 'img', 'lapin1.png'))

        self.customhitbox = [self.image.get_width()-20, self.image.get_height()-30]

        self.sqrtlol = 1 / math.sqrt(2)
        self.lasth = 0
        self.isleft = True
        self.space = False
        self.iscrouching = False
        self.jump = False
        # self.collision_rect = self.image.get_rect(left=self.pos[0], top=self.pos[1])

    def render(self):
        self.screen.blit(self.image, [self.pos[0]-20,self.pos[1]-30])
        #pygame.draw.rect(self.screen, (255,0,0),self.rect,1)

    def trajectorything(self, steps):
        for i in range(steps):
            pass

    def check_event(self):
        keys = pygame.key.get_pressed()
        self.movement[0] = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        self.movement[1] = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        self.space = keys[pygame.K_SPACE]

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         self.player.speed[1] = -5
        #         # self.player.trajectorything(10)

    def check_collision(self):
        pass

    def check_levels(self):
        if self.pos[1] < 0 and self.levels.current_level < self.levels.max_levels:
            print("awesome lil bro")
            self.pos[1] += self.screen.get_height() + self.rect.width
            self.levels.current_level += 1
        if self.pos[1] > self.screen.get_height():
            self.pos[1] -= self.screen.get_height() + self.rect.width
            self.levels.current_level -= 1

    @property
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.customhitbox[0], self.customhitbox[1])
        # return pygame.Rect(self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())

    def update(self):  # update everything

        self.check_event()
        self.collideDown = False
        self.collideUp = False

        if self.movement[0]:
            if self.movement[0] == 1:
                self.speed[0] = 5 #min(5, self.speed[0] + 0.5)
                if self.isleft == True:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.isleft = False

            if self.movement[0] == -1:
                self.speed[0] = -5 #max(-5, self.speed[0] - 0.5)
                if self.isleft == False:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.isleft = True
        else:
            #self.speed[0] = max(0, self.speed[0] - 0.5)
            self.speed[0] = 0

        if self.space and (self.iscrouching == False):
            print('a')
            self.iscrouching = True
            self.image = pygame.image.load(os.path.join('data', 'img', 'lapin2.png'))
            if not self.isleft:
                self.image = pygame.transform.flip(self.image, True, False)


        if (not self.space) and self.iscrouching:
            print('b')
            self.iscrouching = False
            self.image = pygame.image.load(os.path.join('data', 'img', 'lapin.png'))
            if not self.isleft:
                self.image = pygame.transform.flip(self.image, True, False)
            self.speed[1] = -5



        frame_movement = (self.speed[0], self.speed[1])

        # collision X
        if not self.iscrouching:
            self.pos[0] += frame_movement[0]

        ent_rect = self.rect
        for platform in self.levels.levels[self.levels.current_level].platform:
            if platform.rect.colliderect(self.rect):
                if frame_movement[0] > 0:
                    ent_rect.right = platform.rect.left
                if frame_movement[0] < 0:
                    ent_rect.left = platform.rect.right
                self.pos[0] = ent_rect.x


        # collision Y
        self.pos[1] += frame_movement[1]
        ent_rect = self.rect
        for platform in self.levels.levels[self.levels.current_level].platform:
            if platform.rect.colliderect(self.rect):
                if frame_movement[1] > 0:
                    ent_rect.bottom = platform.rect.top
                    self.collideDown = True
                if frame_movement[1] < 0:
                    ent_rect.top = platform.rect.bottom
                    self.collideUp = True
                self.pos[1] = ent_rect.y

        self.speed[1] = min(5, self.speed[1] + 0.1)  # gravity

        if self.collideDown or self.collideUp:
            self.speed[1] = 0

        self.check_levels()
