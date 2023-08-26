import pygame
class Button():
    def __init__(self, size, screen):
        
        self.size = size
        self.screen = screen
        pos = (self.screen.get_width()/2 - (self.size[0]/2), screen.get_height()/2 - (self.size[1]/2))
        
        self.pos = pos
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.Surface(size)
        self.image.fill((180,140,208))
        
    def draw(self):
        pygame.draw.rect(self.image, (180,140,208), (self.pos[0], self.pos[1], self.size[0], self.size[1]))
        font2 = pygame.font.Font("progettonuovo/fonts/Rocket Italic.otf", 50)
        textplayagain = font2.render("PLAY AGAIN", 1, (255,255,255))
        pos = (self.size[0] // 2 - textplayagain.get_width() // 2,self.size[1] // 2 - textplayagain.get_height() // 2)
        self.image.blit(textplayagain, pos)
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()

            