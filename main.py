#print("aggiunto")
import pygame, sys, random
from players import Player
from ball import Ball
from rectangle import Rectangle
from bonus import Bonus
pygame.init()

window_size = (800, 800)
screen = pygame.display.set_mode(window_size)
space1 = pygame.Surface((350, 600))
space2 = pygame.Surface((350, 600))
pygame.display.set_caption('progetto')
createdball1, createdball2  = False, False
createdrect1 = False
createdrect2 = False
createdbonus1, createdbonus2 = False, False
move = True

clock = pygame.time.Clock()
p1 = Player(1, screen, space1, (100, 100), (100, 100), 'progettonuovo/immagini/monster.png')
p2 = Player(2, screen, space2, (600, 600), (100, 100), 'progettonuovo/immagini/monster (1).png')
scorep1 = 10
scorep2 = 10
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
            createdball1, createdball2  = True, True
            b1.startmov()
            b2.startmov()
         
        if event != "1":
            createdball1, createdball2  = False, False
        if event == "2":
                rect1 = Rectangle(1, screen, space1, (space1.get_width(), space1.get_height()))
                createdrect1 = True
                rect2 = Rectangle(2, screen, space2, (space2.get_width(), space2.get_height()))
                createdrect2 = True
                rect1.startmov()
                rect2.startmov()
        if event != "2":
                createdrect1 = False
                createdrect2 = False
        if event == "3":    
            time = 1500
            x = random.choice(["good", "bad"])
            bonus1 = Bonus(1, screen, space1, (50, 50), x )
            bonus2 = Bonus(2, screen, space2, (50, 50), x )
            createdbonus1 = True
            createdbonus2 = True
        if event != "3":
            time = 2000
            createdbonus1 = False
            createdbonus2 = False
        print(event)
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
    if createdball1 == True:
        b1.move()
        if pygame.sprite.collide_mask(b1, p1):
            createdball1 = False
            # decreatedsepoints = True
            scorep1 -= 1
            # print(scorep1)
    if createdball2 == True:
        b2.move()
        if pygame.sprite.collide_mask(b2, p2):
            createdball2 = False
            # decreatedsepoints = True
            scorep2 -= 1
            # print(scorep2)
    if createdrect1 == True:
        rect1.move()
            
        if pygame.sprite.collide_mask(rect1, p1):
            createdrect1 = False
            scorep1 -= 1
        
    if createdrect2 == True:
        rect2.move()
        if pygame.sprite.collide_mask(rect2, p2):
            createdrect2 = False
            scorep2 -= 1
    # print(createdball1)  
    if createdbonus1 == True:
        if pygame.sprite.collide_mask(bonus1, p1):
            if bonus1.x == "good":
                scorep1 += 1
            elif bonus1.x == "bad":
                scorep1 -= 1
            createdbonus1 = False
    if createdbonus2 == True:
        if pygame.sprite.collide_mask(bonus2, p2):
            if bonus2.x == "good":
                scorep2 += 1
            elif bonus2.x == "bad":
                scorep2 -= 1
            createdbonus2 = False
    


    


    screen.fill((153,17,153))
    space1.fill((255, 255, 255))
    space2.fill((255, 255, 255))
    
    screen.blit(space1, (25, 100))
    screen.blit(space2, (425, 100))
    p1.draw()
    p2.draw()
    if createdball1 == True:
        b1.draw()
    if createdball2 == True:
        b2.draw()
    if createdrect1 == True:
        rect1.draw()
    if createdrect2 == True:
        rect2.draw()
    if createdbonus1 == True:
        bonus1.draw()
    if createdbonus2 == True:
        bonus2.draw()
    pygame.draw.rect(screen, (153, 17, 153), pygame.Rect(0, 0, screen.get_width(), 100))
    pygame.draw.rect(screen, (153, 17, 153), pygame.Rect(0, 700, screen.get_width(), 100))
    # print(scorep1, scorep2)
    fontsize = 80
    font = pygame.font.Font(None, fontsize)
    text1 = font.render(str(scorep1), 1, (255, 255, 255))
    text2 = font.render(str(scorep2), 1, (255, 255, 255))
    screen.blit(text1, (screen.get_width()/4 - (fontsize/2), 40))
    screen.blit(text2, ((screen.get_width()/4)*3 - (fontsize/2), 40 ))
    pygame.display.flip()

    clock.tick(60)