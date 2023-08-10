import pygame
import random
class Ball(pygame.sprite.Sprite):
    def __init__(self, p,  screen, space, size, pic):
        super().__init__()
        self.screen = screen
        self.space = space
        self.p = p
        if p == 1:
            pos = ((25 + 50*(random.randint(0, 5)), 0))  
        if p == 2:
            pos = ((425 + 50*(random.randint(0, 5)), 0)) 
        self.pos = pos
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load(pic)
        self.image = pygame.transform.scale(self.image, size)
        self.vel = 0.5
        self.gravity = 0.2
        self.startmoving = False
    def draw(self):
        self.screen.blit(self.image, self.rect)
    def startmov(self):
        self.startmoving = True
    def move(self):
        if self.startmoving == True:
            self.vel += self.gravity
            self.rect.bottom += self.vel