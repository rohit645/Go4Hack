import pygame,time,random,sys
from pygame.locals import *

RESOLUTION = (800,600)

# define colors
BLACK = (0,0,0)
WHITE = (255,255,255)


BGCOLOR = BLACK #Background color


# main game loop
# anything after the game has started is written inside this loop
def main():
    global DISPLAYSURF, FPSCLOCK, IMAGESDICT, BASICFONT
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    
    DISPLAYSURF = pygame.display.set_mode(RESOLUTION)
    
    pygame.display.set_caption("Save The World!")
    BASICFONT = pygame.font.Font("freesansbold.ttf",22)
    
    IMAGESDICT = {'title':pygame.image.load('images/title_image.png')}
    
    startScreen()
    
    
    while True:
        DISPLAYSURF.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        pygame.display.update()

def startScreen():
    titleRect = IMAGESDICT['title'].get_rect()
    topCoord = 150
    titleRect.top = topCoord
    titleRect.centerx = RESOLUTION[0]//2
    topCoord+=titleRect.height
   
    DISPLAYSURF.fill(BGCOLOR)
    DISPLAYSURF.blit(IMAGESDICT['title'],titleRect)
    
    displayText = BASICFONT.render("Press any key to continue...",True,WHITE,BLACK)
    displayTextPos = displayText.get_rect()
    displayTextPos.center = (RESOLUTION[0]//2,RESOLUTION[1]//2)
    DISPLAYSURF.blit(displayText,displayTextPos)
    pygame.mixer.music.load('sounds/theme.mp3')
    pygame.mixer.music.play(-1,0.0)
    while True: #Main loop for the start screen
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                pygame.mixer.music.stop()
                return
        pygame.display.update()
        FPSCLOCK.tick()
        
def terminate():
    pygame.quit()
    sys.exit()
    
if __name__ == '__main__':
    main()