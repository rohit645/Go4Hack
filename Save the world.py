

import pygame 
import time 

pygame.init()

display_width,display_height = 800 , 600
RESOLUTION = (display_width,display_height)

DISPLAYSURF = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Save The World!")
clock = pygame.time.Clock()

plane = pygame.image.load("images/plane1.png")
plane_width = 114
plane_height = 123
# define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
xchange = 0

def text_objects(text,font):
        textSurface = font.render(text, True, WHITE)
        return textSurface, textSurface.get_rect() 
    
    
def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",115)
    textSurf,textRect = text_objects(text,largeText)
    textRect.center = ((display_width/2),(display_height/2))
    DISPLAYSURF.blit(textSurf,textRect) 
    
    pygame.display.update()
    
    time.sleep(2)
    gameloop()
    
def crash() :
    message_display("you crashed")
    


def planeRender (x,y):
    DISPLAYSURF.blit(plane,(x,y))
    

    
#main game loop
# anything after the game has started is written inside this loop 

def gameloop():
            
        x = display_width/2 - plane_width/2
        y = display_height - plane_height
        xchange = 0
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
            if x < 0 or x > display_width - plane_width:
                crash()
            pygame.display.update()
            clock.tick(60)


gameloop()

            
