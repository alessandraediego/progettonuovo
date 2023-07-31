import pygame

class Player:
    def __init__(self, screen, pos, size, pic) -> None:
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load(pic)
        self.image = pygame.transform.scale(self.image, size)
        self.vel = 5
    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    def moveup(self):
        self.rect.top -= self.vel
        if self.rect.top <= 0:
            self.rect.top = 0
    def movedown(self):
        
        self.rect.bottom += self.vel
        if self.rect.bottom >= self.screen.get_height():
            self.rect.bottom = self.screen.get_height()
    def moveright(self):
        self.rect.right += self.vel
        if self.rect.right >= self.screen.get_width():
            self.rect.right = self.screen.get_width()
    def moveleft(self):
        self.rect.left -= self.vel
        if self.rect.left <= 0:
            self.rect.left = 0
        