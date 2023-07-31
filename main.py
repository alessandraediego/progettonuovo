#print("aggiunto")
import pygame, sys
from players import Player
pygame.init()

window_size = (700, 700)
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption('progetto')

clock = pygame.time.Clock()
p1 = Player(screen, (100, 100), (100, 100), 'progettonuovo/immagini/monster.png')
p2 = Player(screen, (600, 600), (100, 100), 'progettonuovo/immagini/monster (1).png')
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
    p1.draw()
    p2.draw()
    pygame.display.flip()

    clock.tick(60)