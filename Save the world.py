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
    global HEALTH
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

        pygame.display.update()

        time.sleep(2)
        pygame.display.update()
        # game starts again after health is 0
        if HEALTH <= 0:
            main()
        game_loop()

    def crash(self) :
        global HEALTH
        HEALTH -= 1

        if HEALTH <= 0:
            self.message_display("GAME OVER")

        self.message_display("YOU CRASHED!")


    def planeRender (self,x,y):
        DISPLAYSURF.blit(self.image,(x,y))

class fireball:
    def __init__(self):
        self.image = load_image("images/meteor.png")
        self.width, self.height = 35, 45
        self.position_y = -self.height
        self.position_x = random.randint(50, display_width - self.width - 50)
        self.velocity = 10
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

def create_fireballs(count):
    """
    Returns a list of 4 fireballs
    """
    fireballs = []
    for i in range(count):
        fireballs.append(fireball())
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
    fireballs = create_fireballs(FIREBALLSCOUNT)
    jet = plane()
    x = display_width/2 - jet.width/2
    y = display_height - jet.height -50
    xchange = 0
    game_level = 1
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
                if event.key == pygame.K_LEFT :
                    xchange = -10

                if event.key == pygame.K_RIGHT:
                    xchange = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange = 0
        x = x + xchange
        for i in range(FIREBALLSCOUNT):
            fireballs[i].move()

            if fireballs[i].position_y >= display_height:
                fireballs[i].update_position()
                #fireball_near = (fireball_near + 1) % 4
                #score(count)
                count +=1
                if count % 20 == 0:
                    game_level += 1
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
        if x < 50 or x > display_width - jet.width - 50:
            jet.crash()

        for i in range(4):
            if fireballs[i].position_y + fireballs[i].height > y and fireballs[i].position_y < y + jet.height :
                    if not (x >= fireballs[i].position_x + fireballs[i].width  or x + jet.width <= fireballs[i].position_x ) :
                        jet.crash()
                    #if (x + jet.width >= fireballs[i].position_x + 25 and x + jet.width <= fireballs[i].position_x + fireballs[i].width -  25):
        pygame.display.update()
        FPSCLOCK.tick(FPS)


# main game loop
# anything after the game has started is written inside this loop
def main():
    global DISPLAYSURF, FPSCLOCK, IMAGESDICT, BASICFONT, FPS,HEALTH,count

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

    pygame.mixer.music.load('sounds/theme.mp3')
    pygame.mixer.music.play(-1,0.0)

    fireballs = create_fireballs(FIREBALLSCOUNT)
    while True: #Main loop for the start screen

        DISPLAYSURF.fill(BGCOLOR)

    # theme music
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

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
