import pygame
def collisiontest(oggetto1, oggetto2):
    collision1 = oggetto1.rect.colliderect(oggetto2)
    if collision1 == True:
        oggetto1.vel = -oggetto1.vel
 