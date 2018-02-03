# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 11:29:38 2018

@author: rohit
"""

import pygame,time,random,sys
from pygame.locals import *

pygame.init()
display_width,display_height = 1280,720
RESOLUTION = (display_width,display_height)
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Save The World!")
clock = pygame.time.Clock()
# define colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#add menu screen


#main game loop
# anything after the game has started is written inside this loop
ball_image= pygame.image.load('images/fireball.png')


def load_image(name):
     return pygame.image.load(name)
class flames:
    def __init__(self):
        self.image = load_image("images/flames_for_games_by_naruhanaluvr_without_background.png")
        self.width, self.height = 1280,200
        self.position = (0, 0)

class plane:
    def __init__(self):
        self.image = pygame.image.load("images/plane1.png")
        self.width = 114
        self.height = 123
    def text_objects(self,text,font):
        textSurface = font.render(text, True, WHITE)
        return textSurface, textSurface.get_rect()

    def message_display(self,text):
        largeText = pygame.font.Font("freesansbold.ttf",115)
        textSurf,textRect = self.text_objects(text,largeText)
        textRect.center = ((display_width/2),(display_height/2))
        DISPLAYSURF.blit(textSurf,textRect)

        pygame.display.update()

        time.sleep(2)
        gameloop()

    def crash(self) :
        self.message_display("you crashed")


    def planeRender (self,x,y):
        DISPLAYSURF.blit(self.image,(x,y))
class fireball:
    global velocity
    velocity = 5

    def __init__(self):
        self.image = load_image("images/fireball.png")
        self.width, self.height = 104, 100
        self.position_y = -self.height
        self.position_x = random.randint(0, display_width - self.width)

    def update_position(self):
        """
        Updates the position of fireballs from downside of screen to top of screen
        """
        self.position_y = -self.height
        self.position_x = random.randint(0, display_width - self.width)

    def move(self):
        """
        Moves the fireballs downwards
        """
        self.position_y += velocity

def create_fireballs():
    """
    Returns a list of 4 fireballs
    """
    fireballs = []
    for i in range(4):
        fireballs.append(fireball())
        fireballs[i].position_y -= i * (display_height / 4)
    return fireballs

'''def firewall():
    wall_image = pygame.image.load('images/flames.png')
    DISPLAYSURF.blit(wall_image,(display_width-100,0))'''
def gameloop():
    fireballs = create_fireballs()
    jet = plane()
    x = display_width/2 - jet.width/2
    y = display_height - jet.height
    xchange = 0
    thingstarty = -600
    thingspeed  = 7
    thingwidth  = 150
    thingheight = 150
    while True:
        DISPLAYSURF.fill(BLACK)
        firewall = flames()
        DISPLAYSURF.blit(firewall.image,firewall.position)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT :
                    xchange = -10

                if event.key == pygame.K_RIGHT:
                    xchange = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange = 0
        x = x + xchange
        for i in range(4):
            fireballs[i].move()

            if fireballs[i].position_y >= display_width:
                fireballs[i].update_position()

            DISPLAYSURF.blit(fireballs[i].image, (fireballs[i].position_x, fireballs[i].position_y))

        DISPLAYSURF.blit(firewall.image, firewall.position)
        jet.planeRender(x,y)
        if x < 0 or x > display_width - jet.width:
            jet.crash()
        if thingstarty + thingheight > y :
                if (x >= thingstartx and x <= thingstartx+thingwidth) or (x + plane_width >= thingstartx and x + plane_width <= thingstartx + thingwidth) :
                    jet.crash()
        pygame.display.update()
        clock.tick(60)
gameloop()
