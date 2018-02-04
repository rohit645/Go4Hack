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
        self.image1 = load_image("images/flame1.png")
        self.image2 = load_image("images/flame2.png")
        self.width, self.height = 120, 720
        self.position1 = (0, 50)
        self.position2 = (display_width - self.width, 50)

    def display(self):
        DISPLAYSURF.blit(self.image1, self.position1)
        DISPLAYSURF.blit(self.image2, self.position2)

class plane:
    global HEALTH ,count
    def __init__(self):
        self.image = pygame.image.load("images/ship.png")
        self.width = 70
        self.height = 80
    def text_objects(self,text,font):
        textSurface = font.render(text, True, WHITE)
        return textSurface, textSurface.get_rect()

    def message_display(self,text):
        largeText = pygame.font.Font("freesansbold.ttf",100)
        textSurf,textRect = self.text_objects(text,largeText)
        textRect.center = ((display_width/2),(display_height/2))
        DISPLAYSURF.blit(textSurf,textRect)
        #if text=="GAME OVER":

        pygame.display.update()



        # game starts again after health is 0
        if HEALTH <= 0:
            textSurf,textRect = self.text_objects("Score: "+ str(count),largeText)
            textRect.center = ((display_width/2),(display_height/2 + textRect.height))
            DISPLAYSURF.blit(textSurf,textRect)
            pygame.display.update()

            time.sleep(2)
            main()
        time.sleep(2)    
        game_loop()

    def crash(self) :
        global HEALTH
        HEALTH -= 1
        crashSound = pygame.mixer.Sound('sounds/explodedeath.wav')
        crashSound.play()
        if HEALTH <= 0:
            self.message_display("GAME OVER")


        self.message_display("YOU CRASHED!")


    def planeRender (self,x,y):
        DISPLAYSURF.blit(self.image,(x,y))

class fireball:
    def __init__(self,velocity):
        self.image = load_image("images/meteor.png")
        self.width, self.height = 35, 45
        self.position_y = -self.height
        self.position_x = random.randint(50, display_width - self.width - 50)
        self.velocity = velocity
        self.add = 3

    def update_position(self):
        """
        Updates the position of fireballs from downside of screen to top of screen
        """
        self.position_y = -self.height
        self.position_x = random.randint(50, display_width - self.width - 50)

    def move(self):
        """
        Moves the fireballs downwards
        """
        self.position_y += self.velocity

    def display(self):
        DISPLAYSURF.blit(self.image, (self.position_x, self.position_y))

    def change_speed(self):
        self.velocity += self.add

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
    DISPLAYSURF.blit(text,(0,0))
def LEVEL(game_level):
    font = pygame.font.Font("freesansbold.ttf",25)
    text = font.render("Level: " + str(game_level),True ,WHITE)
    DISPLAYSURF.blit(text,(400,0))
'''def firewall():
    wall_image = pygame.image.load('images/flames.png')
    DISPLAYSURF.blit(wall_image,(display_width-100,0))'''
def game_loop():
    global HEALTH,count
    Healthimg = pygame.image.load("images/healthimg.png")
    FIREBALLSCOUNT = 4
    FIREBALLVELOCITY = 5
    fireballs = create_fireballs(FIREBALLSCOUNT,FIREBALLVELOCITY)
    jet = plane()
    x = display_width/2 - jet.width/2
    y = display_height - jet.height -50
    xchange = 0
    game_level = 1
<<<<<<< HEAD
    #count = 0
=======
>>>>>>> 46f4236cb43000179d9b9946ef7ae3b87347532a
    pygame.mixer.music.load('sounds/game.mp3')
    pygame.mixer.music.play(-1,0.0)
    while True:
        DISPLAYSURF.fill(BLACK)
        firewall = flames()
        #DISPLAYSURF.blit(firewall.image,firewall.position)
        firewall.display()
        score(count)
        for i in range(HEALTH):
            DISPLAYSURF.blit(Healthimg,(200 + (i*45),(0)))
        #LEVEL(game_level)
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
                #vanishSound = pygame.mixer.Sound('sounds/missile.wav')
                #vanishSound.play()
                fireballs[i].update_position()
                #fireball_near = (fireball_near + 1) % 4
                #score(count)
                count +=1
                if count % 20 == 0:
                    game_level += 1
                    levelSound = pygame.mixer.Sound('sounds/healthup.wav')
                    levelSound.play()
                    for i in range(4):
                        fireballs[i].change_speed()
                #score(count)
                #count +=1
            # Only display below score and health bar
            if fireballs[i].position_y > 40:
                DISPLAYSURF.blit(fireballs[i].image, (fireballs[i].position_x, fireballs[i].position_y))
        LEVEL(game_level)
        firewall.display()
        jet.planeRender(x,y)
        if x < 50 or x > display_width - jet.width -50:
            pygame.mixer.music.stop()
            jet.crash()

        for i in range(4):
            if fireballs[i].position_y + fireballs[i].height > y and fireballs[i].position_y < y + jet.height :
                    if not (x >= fireballs[i].position_x + fireballs[i].width  or x + jet.width <= fireballs[i].position_x ) :
                        pygame.mixer.music.stop()
                        jet.crash()
                    #if (x + jet.width >= fireballs[i].position_x + 25 and x + jet.width <= fireballs[i].position_x + fireballs[i].width -  25):
        pygame.display.update()
        FPSCLOCK.tick(FPS)


# main game loop
# anything after the game has started is written inside this loop
def main():
    global DISPLAYSURF, FPSCLOCK, IMAGESDICT, BASICFONT, FPS, HEALTH,count

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    FPS = 60
    HEALTH = 3
    count = 0
    DISPLAYSURF = pygame.display.set_mode(RESOLUTION)

    pygame.display.set_caption("Save The World!")
    BASICFONT = pygame.font.Font("freesansbold.ttf",22)

    IMAGESDICT = {'title':pygame.image.load('images/title_image.png')}

    startScreen()
    game_loop()
    terminate()

def startScreen():
    FIREBALLSCOUNT = 7 # number of fireballs displayed on start screen
    INSTRUCTIONS  = ["Press ESC to quit at any time","Press SPACE to pause","Press any other key to continue...","Tip : Dodge the meteors to increase score"]
    fontObj = pygame.font.Font("freesansbold.ttf",60)
    titleText = fontObj.render("Save the World",True,(51,105,232))
    titleRect = titleText.get_rect()
#    titleRect = IMAGESDICT['title'].get_rect()
    topCoord = RESOLUTION[1]//2 - titleRect.height
    titleRect.top = topCoord
    titleRect.centerx = RESOLUTION[0]//2
    topCoord+=titleRect.height + 20
    displayText = []
    displayTextPos = []
    for i in range(len(INSTRUCTIONS)):

        displayText.append(BASICFONT.render(INSTRUCTIONS[i],True,WHITE))
        displayTextPos.append(displayText[i].get_rect())
        displayTextPos[i].center = (RESOLUTION[0]//2,topCoord)
        topCoord+=displayTextPos[i].height
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
        
        for i in range(len(displayText)):
            DISPLAYSURF.blit(displayText[i],displayTextPos[i])
            
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                pygame.mixer.music.stop()
                return
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def pauseGame():
    LARGEFONT = pygame.font.Font("freesansbold.ttf",100)
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
