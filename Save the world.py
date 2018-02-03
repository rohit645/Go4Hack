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
def main():
    
    drawMenu()
    
    while True:
#        DISPLAYSURF.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def drawMenu():
    fontObj = pygame.font.Font('freesansbold.ttf',32)
    displayText = fontObj.render("Press any key to continue",True,WHITE,BLACK)
    displayTextPos = displayText.get_rect()
    displayTextPos.center = (RESOLUTION[0]//2,RESOLUTION[1]//2)
    DISPLAYSURF.blit(displayText,displayTextPos)

        
if __name__ == '__main__':
    main()