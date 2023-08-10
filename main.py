#print("aggiunto")
import pygame, sys, random
from players import Player
from ball import Ball
from altre import decreasepoints
pygame.init()

window_size = (800, 800)
screen = pygame.display.set_mode(window_size)
space1 = pygame.Surface((350, 600))
space2 = pygame.Surface((350, 600))
pygame.display.set_caption('progetto')
creataball1, creataball2  = False, False

clock = pygame.time.Clock()
p1 = Player(1, screen, space1, (100, 100), (100, 100), 'progettonuovo/immagini/monster.png')
p2 = Player(2, screen, space2, (600, 600), (100, 100), 'progettonuovo/immagini/monster (1).png')
scorep1 = 20
scorep2 = 20
time = 2000
timelastevent = pygame.time.get_ticks()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    currenttime = pygame.time.get_ticks()
    if currenttime - timelastevent > time:
        events = ["1", "2", "3"]
        event = random.choice(events)
        if event == "1": 
            b1 = Ball(1, screen, space1, (100, 100), 'progettonuovo/immagini/green-slime.png')
            b2 = Ball(2, screen, space2, (100, 100), 'progettonuovo/immagini/green-slime.png')
            creataball1, creataball2  = True, True
            b1.startmov()
            b2.startmov()
            
        if event != "1":
            creataball, creataball2  = False, False
            
        # print(event)
        timelastevent = currenttime
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
    if creataball1 == True:
        b1.move()
        if pygame.sprite.collide_mask(b1, p1):
            decreasepoints = True
            print(scorep1)
    if creataball2 == True:
        b2.move()
        if pygame.sprite.collide_mask(b1, p1):
            scorep1 -= 1
            # print(scorep2)
        
    
   
    


    screen.fill((153,17,153))
    space1.fill((255, 255, 255))
    space2.fill((255, 255, 255))
    
    screen.blit(space1, (25, 100))
    screen.blit(space2, (425, 100))
    p1.draw()
    p2.draw()
    if creataball1 == True:
        b1.draw()
    if creataball2 == True:
        b2.draw()
    
    pygame.display.flip()

    clock.tick(60)