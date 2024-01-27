import pygame
from sys import exit


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption("pygame2")

q0 = pygame.mixer.Sound("q0.mp3")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #piano starts here

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            if event.key == pygame.K_SPACE:
                if event.key == pygame.K_KP0:
                    pass
                if event.key == pygame.K_KP1:
                    print("1")
                if event.key == pygame.K_KP2:
                    print("2")
                if event.key == pygame.K_KP3:
                    print("3")
                if event.key == pygame.K_KP4:
                    print("4")
                if event.key == pygame.K_KP5:
                    print("5")
                if event.key == pygame.K_KP6:
                    print("6")
                if event.key == pygame.K_KP7:
                    print("7")
                print("qspace")
            print("q0q")
    #Displaying things
    pygame.display.update()