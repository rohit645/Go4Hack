# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 11:29:38 2018

@author: rohit
"""

import pygame,time,random,sys
from pygame.locals import *

pygame.init()

RESOLUTION = (800,600)
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Save The World!")

# define colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#add menu screen


#main game loop
# anything after the game has started is written inside this loop 
while True:
    DISPLAYSURF.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
