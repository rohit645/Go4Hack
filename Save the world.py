# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 11:29:38 2018

@author: rohit
"""

import pygame, time, random, sys
from pygame.locals import *

pygame.init()

display_height, display_width = 600, 1000
RESOLUTION = (display_width, display_height)
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Save the world!")
CLOCK = pygame.time.Clock()
BLACK = (0, 0, 0)

class flames:
    def __init__(self):
        self.image = load_image("images/flames.png")
        self.width, self.height = 100, 600
        self.position = (display_width - self.width, 0)

class fireball:
    global velocity
    velocity = 5

    def __init__(self):
        self.image = load_image("images/fireball.png")
        self.width, self.height = 104, 100
        self.position_x = display_width
        self.position_y = random.randint(0, display_height)

    def update(self):
        self.position_x -= velocity

def load_image(name):
     return pygame.image.load(name)

def create_fireballs():
    fireballs = []
    for i in range(4):
        fireballs.append(fireball())
        fireballs[i].position_x += i * (display_width / 4)
    return fireballs

def game_loop():
    game_exit = False
    firewall = flames()
    fireballs = create_fireballs()

    while not game_exit:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_exit = True
                break

        DISPLAYSURF.fill(BLACK)

        for i in range(4):
            fireballs[i].update()

            if fireballs[i].position_x <= -fireballs[i].width:
                fireballs[i].position_x += display_width
                fireballs[i].position_y = random.randint(0, display_height)

            DISPLAYSURF.blit(fireballs[i].image, (fireballs[i].position_x, fireballs[i].position_y))

        DISPLAYSURF.blit(firewall.image, firewall.position)
        pygame.display.update()
        CLOCK.tick(60)

game_loop()
pygame.quit()
quit()
