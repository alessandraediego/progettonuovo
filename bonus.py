import pygame
import random
class Bonus(pygame.sprite.Sprite):
    def __init__(self, p,  screen, space, size, x):
        super().__init__()
        self.screen = screen
        self.space = space
        self.p = p
        self.x = x
        if x == "1point":
            pic = 'progettonuovo/immagini/star2.png'
        elif x == "2points":
            pic = 'progettonuovo/immagini/star (1).png'
        if p == 1:
            pos = (random.randint(25, 25+self.space.get_width()-size[0]), random.randint(100, 100+self.space.get_width() - size[1]))  
        if p == 2:
            pos = (random.randint(425, 425+self.space.get_width()-size[0]), random.randint(100, 100+self.space.get_width() - size[1]))
        self.pos = pos
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load(pic)
        self.image = pygame.transform.scale(self.image, size)
        
    def draw(self):
        self.screen.blit(self.image, self.rect)