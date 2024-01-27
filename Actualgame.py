import pygame
from sys import exit
import math

#VARIABLE------------->

fps=60
screen_width = 1000
screen_height =600
background_location = (0,0)

#SOMETHING------------>

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill((255,255,255))
clock = pygame.time.Clock()
pygame.display.set_caption("ACTUAL_GAME")
background1 = pygame.image.load("background1.png")
BG_image = pygame.transform.scale(background1,(screen_width,screen_height))



#MAIN ----------------->

while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

#DISPLAY--------------->

    pygame.display.update()
    screen.blit(BG_image,background_location)