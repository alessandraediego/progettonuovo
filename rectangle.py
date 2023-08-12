import random, pygame
class Rectangle(pygame.sprite.Sprite):
    def __init__(self, p,  screen, space, size, pic):
        super().__init__()
        self.screen = screen
        self.space = space
        self.p = p
        if p == 1:
            pos = ((25, (random.choice([100 - self.space.get_height(), (self.screen.get_height() - 100)]))))
            print(pos)
        if p == 2:
            pos = ((425, (random.choice([100 - self.space.get_height(), (self.screen.get_height() - 100)]))))
        self.pos = pos
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load(pic)
        self.image = pygame.transform.scale(self.image, size)
        self.vel = 3
        self.startmoving = False
    def draw(self):
        self.screen.blit(self.image, self.rect)
    def startmov(self):
        self.startmoving = True
    def move(self):
        if self.startmoving == True:
            if self.pos[1] == 100 - self.space.get_height():
                    self.rect.bottom += self.vel
            if self.pos[1] == self.screen.get_height() - 100:
                    self.rect.top -= self.vel