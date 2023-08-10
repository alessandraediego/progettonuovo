import pygame

class Player:
    def __init__(self, p, screen, space, pos, size, pic) -> None:
        self.screen = screen
        self.space = space
        self.p = p
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load(pic)
        self.image = pygame.transform.scale(self.image, size)
        self.vel = 5
    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    def moveup(self):
        self.rect.top -= self.vel
        if self.rect.top <= 100:
            self.rect.top = 100
    def movedown(self):
        self.rect.bottom += self.vel
        if self.rect.bottom >= 100 + self.space.get_height():
            self.rect.bottom = 100 + self.space.get_height()
    def moveright(self):
        self.rect.right += self.vel
        if self.p == 1:
           if self.rect.right >= 25 + self.space.get_width():
            self.rect.right = 25 + self.space.get_width()
        if self.p == 2: 
            if self.rect.right >= self.screen.get_width()/2 + 25 + self.space.get_width():
                self.rect.right = self.screen.get_width()/2 + 25 + self.space.get_width()
    def moveleft(self):
        self.rect.left -= self.vel
        if self.p == 1:
            if self.rect.left <= 25:
                self.rect.left = 25
        if self.p == 2:
            if self.rect.left <= self.screen.get_width()/2 + 25:
                self.rect.left = self.screen.get_width()/2 + 25
        