

import pygame 
import time 

pygame.init()

RESOLUTION = (800,600)

DISPLAYSURF = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Save The World!")
clock = pygame.time.Clock()

plane = pygame.image.load("images/plane1.png")

# define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
xchange = 0
#add menu screen
def planeRender (x,y):
    DISPLAYSURF.blit(plane,(x,y))
    

#main game loop
# anything after the game has started is written inside this loop 
x = (RESOLUTION[0] * 0.45)
y = (RESOLUTION[1] * 0.7)
while True:
    
    
    
    DISPLAYSURF.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                xchange = -10 
            
            if event.key == pygame.K_RIGHT:
                xchange = 10
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xchange = 0
    
    DISPLAYSURF.fill(BLACK)        
    x = x + xchange
    planeRender(x,y)
#    print(x,y)
            
    pygame.display.update()
    clock.tick(30)
    
