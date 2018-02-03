# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 11:29:38 2018

@author: rohit
"""

import pygame,time,random,sys
from pygame.locals import *

pygame.init()
display_width,display_height = 800,600
RESOLUTION = (display_width,display_height)
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Save The World!")

# define colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#add menu screen


#main game loop
# anything after the game has started is written inside this loop
ball_image= pygame.image.load('images/fireball.png')
fireball_position_x = random.randint(0,display_width - 240)
fireball_position_y = -252

def firewall():
    wall_image = pygame.image.load('images/flames_for_games_by_naruhanaluvr_without_background.png')
    DISPLAYSURF.blit(wall_image,(0,0))
while True:
    DISPLAYSURF.fill(BLACK)
    firewall()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    DISPLAYSURF.blit(ball_image,(fireball_position_x,fireball_position_y))
    fireball_position_y += 5
    if fireball_position_y > display_height:
        fireball_position_x = random.randint(0,display_width - 240)
        fireball_position_y = -252
    pygame.display.update()
