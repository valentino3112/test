import pygame
import math
import os
import sys
import time

class Char:
    def __init__(self, levels, screen):
        self.screen = screen
        self.levels = levels
        self.pos = [500, 500]
        self.speed = [0, 0]
        self.collideDown = False
        self.collideUp = False
        self.collideLeft = False
        self.collideRight = False
        self.movement = [0, 0]
        self.image = pygame.image.load(os.path.join('data', 'img', 'lapin1.png'))

        self.customhitbox = [self.image.get_width()-20, self.image.get_height()-30]

        self.sqrtlol = 1 / math.sqrt(2)
        self.lasth = 0
        self.isleft = True
        self.space = False
        self.iscrouching = False
        self.jump = False
        self.mouse_x, self.mouse_y = 0,0
        self.click = False
        # self.collision_rect = self.image.get_rect(left=self.pos[0], top=self.pos[1])

    def render(self):
        self.screen.blit(self.image, [self.pos[0]-20,self.pos[1]-30])
        #pygame.draw.rect(self.screen, (255,0,0),self.rect,1)

    def move(self):
            #temps_diff = time.time() - self.temps_debut
            temps_diff = 2
            # print("Click Up ", self.last_event[0].pos, temps_diff)
            self.temps_debut = None

            nombre_secondes_max = 2
            if temps_diff > nombre_secondes_max:
                temps_diff = nombre_secondes_max


            angle = math.atan2((self.mouse_y - self.pos[1]), (self.mouse_x - self.pos[0]))
            force_frottement = 10
            masse_personnage = 50
            g = 9.81
            v0 = 200 + 200 * temps_diff
            vx = v0 * math.cos(angle)
            vy = v0 * math.sin(angle)
            dt = 0.05
            # #self.rect.x += dt * vx
            # self.pos[0] += dt * vx
            # #self.rect.y += dt * vy
            # self.pos[1] += dt * vy
            # vx += dt * vx * (-force_frottement / masse_personnage)
            # vy += dt * vy * (-force_frottement / masse_personnage) + dt * g * masse_personnage
            self.speed[0] = dt * vx
            self.speed[1] = dt * vy


    def check_event(self):
        keys = pygame.key.get_pressed()
        self.movement[0] = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        self.movement[1] = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        self.space = keys[pygame.K_SPACE]

        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.click = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.click = False
            if event.type == pygame.QUIT:
                print("quit")
                pygame.quit()
                sys.exit()


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


        if self.click and (self.iscrouching == False):
            print('a')
            self.iscrouching = True
            self.image = pygame.image.load(os.path.join('data', 'img', 'lapin2.png'))
            if not self.isleft:
                self.image = pygame.transform.flip(self.image, True, False)


        if (not self.click) and self.iscrouching:
            print('b')
            self.iscrouching = False
            self.image = pygame.image.load(os.path.join('data', 'img', 'lapin.png'))
            if not self.isleft:
                self.image = pygame.transform.flip(self.image, True, False)
            print("FUCK")
            self.move()



        frame_movement = (self.speed[0], self.speed[1])

        # collision X
        if not self.iscrouching:
            self.pos[0] += frame_movement[0]

        ent_rect = self.rect
        for platform in self.levels.levels[self.levels.current_level].platform:
            if platform.rect.colliderect(self.rect):
                if frame_movement[0] > 0:
                    ent_rect.right = platform.rect.left
                    self.speed[0] = -self.speed[0]*0.6
                if frame_movement[0] < 0:
                    ent_rect.left = platform.rect.right
                    self.speed[0] = -self.speed[0]*0.6
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

        self.speed[1] = min(100, self.speed[1] + 3)  # gravity

        if self.collideDown or self.collideUp:
            self.speed[1] = 0
            self.speed[0] = 0

        self.check_levels()
