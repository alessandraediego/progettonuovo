import pygame, sys, random
from players import Player
from ball import Ball
from rectangle import Rectangle
from bonus import Bonus
from button import Button
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
createdbutton = False
move = True
gameover = False
font2 = pygame.font.Font("progettonuovo/fonts/Rocket Italic.otf", 100)
buttondown = False

clock = pygame.time.Clock()
p1 = Player(1, screen, space1, (25 + space1.get_width()//2 - 100/2 , screen.get_height()//2 - 100/2), (100, 100), 'progettonuovo/immagini/monster.png')
p2 = Player(2, screen, space2, (screen.get_width()//2 + 25 + space2.get_width()//2 - 100/2, screen.get_height()//2 - 100/2), (100, 100), 'progettonuovo/immagini/monster (1).png')
scorep1 = 10
scorep2 = 10
time = 1500
timelastevent = pygame.time.get_ticks()
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if createdbutton == True:
                buttondown = True
                pos = pygame.mouse.get_pos()
    if scorep1 <=0 or scorep2 <= 0:
        gameover = True
        createdbutton = True
        button = Button((400, 100), screen)
        if buttondown == True:
            if button.rect.collidepoint(pos):
                
                gameover = False
                scorep1, scorep2 = 10, 10
                p1 = Player(1, screen, space1, (25 + space1.get_width()//2 - 100/2 , screen.get_height()//2 - 100/2), (100, 100), 'progettonuovo/immagini/monster.png')
                p2 = Player(2, screen, space2, (screen.get_width()//2 + 25 + space2.get_width()//2 - 100/2, screen.get_height()//2 - 100/2), (100, 100), 'progettonuovo/immagini/monster (1).png')
                buttondown = False
    currenttime = pygame.time.get_ticks()
    
    if gameover == False:
        if currenttime - timelastevent > time:
            events = ["ball", "ball", "spikes", "spikes", "bonus"]
            event = random.choice(events)
            if event == "ball":
                time = 2000
                b1 = Ball(1, screen, space1, (100, 100), 'progettonuovo/immagini/green-slime.png')
                b2 = Ball(2, screen, space2, (100, 100), 'progettonuovo/immagini/green-slime.png')
                createdball1, createdball2  = True, True
                b1.startmov()
                b2.startmov()
            
            if event != "ball":
                createdball1, createdball2  = False, False
                time = 1500
            if event == "spikes":
                    
                    rect1 = Rectangle(1, screen, space1, (space1.get_width(), space1.get_height()))
                    createdrect1 = True
                    rect2 = Rectangle(2, screen, space2, (space2.get_width(), space2.get_height()))
                    createdrect2 = True
                    rect1.startmov()
                    rect2.startmov()
            if event != "spikes":
                    createdrect1 = False
                    createdrect2 = False
            if event == "bonus":    
                
                x = random.choice(["1point", "2points"])
                bonus1 = Bonus(1, screen, space1, (50, 50), x )
                bonus2 = Bonus(2, screen, space2, (50, 50), x )
                createdbonus1 = True
                createdbonus2 = True
            if event != "bonus":
                
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
                
                scorep1 -= 1
                
        if createdball2 == True:
            b2.move()
            if pygame.sprite.collide_mask(b2, p2):
                createdball2 = False
                
                scorep2 -= 1
                
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
    
        if createdbonus1 == True:
            if pygame.sprite.collide_mask(bonus1, p1):
                if bonus1.x == "1point":
                    scorep1 += 1
                elif bonus1.x == "2points":
                    scorep1 += 2
                createdbonus1 = False
        if createdbonus2 == True:
            if pygame.sprite.collide_mask(bonus2, p2):
                if bonus2.x == "1point":
                    scorep2 += 1
                elif bonus2.x == "2points":
                    scorep2 += 2
                createdbonus2 = False
    


    


    screen.fill((66,49,127))
    space1.fill((255, 255, 255))
    space2.fill((255, 255, 255))
    
    screen.blit(space1, (25, 100))
    screen.blit(space2, (425, 100))
    p1.draw()
    p2.draw()
    if gameover == False:
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
    pygame.draw.rect(screen, ((66,49,127)), pygame.Rect(0, 0, screen.get_width(), 100))
    pygame.draw.rect(screen, ((66,49,127)), pygame.Rect(0, 700, screen.get_width(), 100))
    fontsize = 80
    font = pygame.font.Font(None, fontsize)
    text1 = font.render(str(scorep1), 1, (255, 255, 255))
    text2 = font.render(str(scorep2), 1, (255, 255, 255))
    screen.blit(text1, (screen.get_width()/4 - (fontsize/2), 40))
    screen.blit(text2, ((screen.get_width()/4)*3 - (fontsize/2), 40 ))
    if gameover == True:
        
        if scorep1 <=0:
            textgameover = font2.render("PLAYER 2 WON!", 1, (180,140,208))
        if scorep2 <= 0:
            textgameover = font2.render("PLAYER 1 WON!", 1, (180,140,208))
        
        
        screen.blit(textgameover, (screen.get_width()// 2 - textgameover.get_width() //2, screen.get_height()- 50 - textgameover.get_height() //2))
        if createdbutton == True:
            button.draw()
    pygame.display.flip()

    clock.tick(60)