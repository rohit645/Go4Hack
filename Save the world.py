import pygame, time, random, sys
from pygame.locals import *

display_height, display_width = 600, 1000
RESOLUTION = (display_width, display_height)
BLACK = (0, 0, 0)
BGCOLOR = BLACK #Background color
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
        FPSCLOCK.tick(60)



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
    game_loop()
    terminate()
    
    while True:
        DISPLAYSURF.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        pygame.display.update()

def startScreen():
    titleRect = IMAGESDICT['title'].get_rect()
    topCoord = RESOLUTION[1]//2 - titleRect.height
    titleRect.top = topCoord
    titleRect.centerx = RESOLUTION[0]//2
    topCoord+=titleRect.height
   
    DISPLAYSURF.fill(BGCOLOR)
    DISPLAYSURF.blit(IMAGESDICT['title'],titleRect)
    
    displayText = BASICFONT.render("Press any key to continue...",True,WHITE,BLACK)
    displayTextPos = displayText.get_rect()
    displayTextPos.center = (RESOLUTION[0]//2,topCoord)
    DISPLAYSURF.blit(displayText,displayTextPos)
    
    # theme music
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
