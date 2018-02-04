import pygame, time, random, sys
from pygame.locals import *

display_height, display_width = 600, 1000
RESOLUTION = (display_width, display_height)
BLACK = (0, 0, 0)
WHITE = (255,255,255)

BGCOLOR = BLACK #Background color

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
        game_loop()

    def crash(self) :
        crashSound = pygame.mixer.Sound('sounds/explodedeath.wav')
        crashSound.play()
        self.message_display("You crashed")
        
    def planeRender (self,x,y):
        DISPLAYSURF.blit(self.image,(x,y))
        
class fireball:
    
    def __init__(self,velocity):
        self.image = load_image("images/fireball.png")
        self.width, self.height = 104, 100
        self.position_y = -self.height
        self.velocity = velocity
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
        self.position_y += self.velocity

def create_fireballs(count,velocity):
    """
    Returns a list of 4 fireballs
    """
    fireballs = []
    for i in range(count):
        fireballs.append(fireball(velocity))
        fireballs[i].position_y -= (i+1) * (display_height / count)

    return fireballs
def score(count):
    font = pygame.font.Font("freesansbold.ttf",25)
    text = font.render("Score: " + str(count),True ,WHITE)
    DISPLAYSURF.blit(text,(0,300))
'''def firewall():
    wall_image = pygame.image.load('images/flames.png')
    DISPLAYSURF.blit(wall_image,(display_width-100,0))'''
def game_loop():
    FIREBALLSCOUNT = 4
    FIREBALLVELOCITY = 5
    fireballs = create_fireballs(FIREBALLSCOUNT,FIREBALLVELOCITY)
    jet = plane()
    x = display_width/2 - jet.width/2
    y = display_height - jet.height
    xchange = 0
    count = 0
    pygame.mixer.music.load('sounds/game.mp3')
    pygame.mixer.music.play(-1,0.0)
    while True:
        DISPLAYSURF.fill(BLACK)
        firewall = flames()
        DISPLAYSURF.blit(firewall.image,firewall.position)
        score(count)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    pauseGame()
                if event.key == pygame.K_LEFT :
                    xchange = -10

                if event.key == pygame.K_RIGHT:
                    xchange = 10
                if event.key == K_ESCAPE:
                    terminate()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange = 0
        x = x + xchange
        for i in range(FIREBALLSCOUNT):
            fireballs[i].move()

            if fireballs[i].position_y >= display_height:
                vanishSound = pygame.mixer.Sound('sounds/missile.wav')
                vanishSound.play()
                fireballs[i].update_position()
                #score(count)
                count +=1
            DISPLAYSURF.blit(fireballs[i].image, (fireballs[i].position_x, fireballs[i].position_y))

        DISPLAYSURF.blit(firewall.image, firewall.position)
        jet.planeRender(x,y)
        if x < 0 or x > display_width - jet.width:
            pygame.mixer.music.stop()
            jet.crash()
        for i in range(4):
            if fireballs[i].position_y + fireballs[i].height - 30 > y :
                    if not (x >= fireballs[i].position_x + fireballs[i].width or x + jet.width <= fireballs[i].position_x -25) :
                        pygame.mixer.music.stop()
                        jet.crash()
                    #if (x + jet.width >= fireballs[i].position_x + 25 and x + jet.width <= fireballs[i].position_x + fireballs[i].width -  25):
        pygame.display.update()
        FPSCLOCK.tick(FPS)


# main game loop
# anything after the game has started is written inside this loop
def main():
    global DISPLAYSURF, FPSCLOCK, IMAGESDICT, BASICFONT, FPS
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    FPS = 60
    
    DISPLAYSURF = pygame.display.set_mode(RESOLUTION)
    
    pygame.display.set_caption("Save The World!")
    BASICFONT = pygame.font.Font("freesansbold.ttf",22)
    
    IMAGESDICT = {'title':pygame.image.load('images/title_image.png')}
    
    startScreen()
    game_loop()
    terminate()

def startScreen():
    FIREBALLSCOUNT = 7 # number of fireballs displayed on start screen
    
    fontObj = pygame.font.Font("freesansbold.ttf",60)
    titleText = fontObj.render("Save the World",True,WHITE)
    titleRect = titleText.get_rect()
#    titleRect = IMAGESDICT['title'].get_rect()
    topCoord = RESOLUTION[1]//2 - titleRect.height
    titleRect.top = topCoord
    titleRect.centerx = RESOLUTION[0]//2
    topCoord+=titleRect.height + 20
    
    displayText = BASICFONT.render("Press any key to continue...",True,WHITE)
    displayTextPos = displayText.get_rect()
    displayTextPos.center = (RESOLUTION[0]//2,topCoord)
#    DISPLAYSURF.blit(IMAGESDICT['title'],titleRect)

    # theme music
    pygame.mixer.music.load('sounds/theme.mp3')
    pygame.mixer.music.play(-1,0.0)

    fireballs = create_fireballs(FIREBALLSCOUNT,2)
    while True: #Main loop for the start screen

        DISPLAYSURF.fill(BGCOLOR)
    
        for i in range(FIREBALLSCOUNT):
            fireballs[i].move()
            
            if fireballs[i].position_y >= display_height:
                fireballs[i].update_position()
            
        
            DISPLAYSURF.blit(fireballs[i].image, (fireballs[i].position_x, fireballs[i].position_y))
        DISPLAYSURF.blit(titleText,titleRect)
        DISPLAYSURF.blit(displayText,displayTextPos)
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                pygame.mixer.music.stop()
                return
        pygame.display.update()
        FPSCLOCK.tick(FPS) # for slow effect

def pauseGame():
    LARGEFONT = pygame.font.Font("freesansbold.ttf",120)
    pauseText = LARGEFONT.render("PAUSED",True,WHITE)

    textRect  = pauseText.get_rect()
    textRect.center = (RESOLUTION[0]//2,RESOLUTION[1]//2)

    DISPLAYSURF.blit(pauseText,textRect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_SPACE:
                    return
    
def terminate():
    pygame.quit()
    sys.exit()
    
if __name__ == '__main__':
    main()
