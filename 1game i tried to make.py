import pygame
from sys import exit
import math

pygame.init()
screen = pygame.display.set_mode((450,600))
screen.fill("red")
clock = pygame.time.Clock()
pygame.display.set_caption("Something")

#VARIBLES

game_phase = 1
camera_x_pos = 0
camera_y_pos = 0
gravity = 3
anti_gravity = -3

#PLAYERS

player_surf = pygame.image.load("/home/jai/Desktop/python work/player.png").convert_alpha()
player2_surf = pygame.image.load("/home/jai/Desktop/python work/player2.png").convert_alpha()
player_rect = player_surf.get_rect(topleft = (camera_x_pos,camera_y_pos))
player2_rect = player2_surf.get_rect(topleft = (0,550))

ball_surf = pygame.image.load("/home/jai/Desktop/python work/ball.png")
ball_rect = ball_surf.get_rect(topleft = (0,300))

playbutton_surf = pygame.image.load("/home/jai/Desktop/python work/playbutton.png").convert_alpha()
playbutton_rect = playbutton_surf.get_rect(topleft = (125,380))
#BACKGROUND

background_img = pygame.image.load("/home/jai/Desktop/python work/background.png")

#MOVEMENTS

player_movement_pos_x = +4
player_movement_neg_x = -4
timespan = 1000#its in miliseconds so 1sec = 1000

#GAME MENU =========>>>>>>>>
while game_phase ==0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    mouse_pos = pygame.mouse.get_pos()
    if playbutton_rect.collidepoint(mouse_pos):
         print(pygame.mouse.get_pressed())
         if pygame.mouse.get_pressed() == True:
            game_phase += 1


    
#DISPLAYING STUFF AND UPDATING THEM ========>>>>>>

    pygame.display.update()
    screen.blit(background_img,(camera_x_pos,camera_y_pos))
    screen.blit(playbutton_surf,(playbutton_rect))


while game_phase == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

#CAMERA OFF SET THINGS



#PLAYER MOVEMENTS HERE---------->>>>>>>>>>

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player_rect.x += player_movement_pos_x
        player2_rect.x += player_movement_pos_x
        

    if keys[pygame.K_a]:
        player_rect.x += player_movement_neg_x
        player2_rect.x += player_movement_neg_x
        
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_movement_pos_x
        player2_rect.x += player_movement_pos_x
        

    if keys[pygame.K_LEFT]:
        player_rect.x += player_movement_neg_x
        player2_rect.x += player_movement_neg_x
    
    if player_rect.x < 0:
        player_rect.x = 0
        player2_rect.x = 0

    if player_rect.x >= 400:
        player_rect.x = 400
        player2_rect.x = 400
    
#BALL MECHANICS ==============>>>>>>>>>>

    if keys[pygame.K_SPACE]:
        ball_rect.y = ball_rect.y
    else: 
        if ball_rect.y <= 510:
            while ball_rect.y <= 50:
                ball_rect.y += anti_gravity
        if ball_rect.y <= 50:
            while ball_rect.y >= 510:
                ball_rect.y += gravity

    ball_rect.x = player_rect.x 

#ENEMY STUFF HERE =============>>>>>>>>>>>


#UPDATING AND SHIT =============>>>>>>>>
    
    pygame.display.update()
    screen.blit(background_img,(camera_x_pos,camera_y_pos))

    screen.blit(player_surf,(player_rect))
    screen.blit(player2_surf,(player2_rect))
    screen.blit(ball_surf,(ball_rect))
    clock.tick(60)