#print("aggiunto")
import pygame, sys
from players import Player
from altre import collisiontest
pygame.init()

window_size = (800, 800)
screen = pygame.display.set_mode(window_size)
space1 = pygame.Surface((350, 600))
space2 = pygame.Surface((350, 600))
pygame.display.set_caption('progetto')

clock = pygame.time.Clock()
p1 = Player(1, screen, space1, (100, 100), (100, 100), 'progettonuovo/immagini/monster.png')
p2 = Player(2, screen, space2, (600, 600), (100, 100), 'progettonuovo/immagini/monster (1).png')
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1.moveup()
    if keys[pygame.K_a]:
        p1.moveleft()
    if keys[pygame.K_s]:
        p1.movedown()
    if keys[pygame.K_d]:
        p1.moveright()
    if keys[pygame.K_UP]:
        p2.moveup()
    if keys[pygame.K_LEFT]:
        p2.moveleft()
    if keys[pygame.K_DOWN]:
        p2.movedown()
    if keys[pygame.K_RIGHT]:
        p2.moveright()
    
    screen.fill((153,17,153))
    space1.fill((255, 255, 255))
    space2.fill((255, 255, 255))
    
    screen.blit(space1, (25, 100))
    screen.blit(space2, (425, 100))
    p1.draw()
    p2.draw()
    pygame.display.flip()

    clock.tick(60)