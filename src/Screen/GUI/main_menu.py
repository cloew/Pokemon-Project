import pygame
from pygame.locals import *

def load_image(name, colorkey=None):
    fullname = name
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
    
def GetIcon():
    image, rect = load_image("pokeball.gif")
    icon = pygame.Surface((225, 225))
    icon.blit(image, rect)
    return image

def DrawBackground():
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 175, 175))
    return background

def DrawFont(font, background): 
    text = font.render("Start Game", 1, (10, 10, 10))
    textpos = text.get_rect(centerx = background.get_width()/2, centery= background.get_height()/2 - 100)
    background.blit(text, textpos)
    
def DrawScreen(screen, background): 
    screen.blit(background, (0,0))
    Update()
    
def Update():
    pygame.display.flip()

pygame.init()
pygame.display.set_icon(GetIcon())
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption('Pokemon')
pygame.mouse.set_visible(0)

background = DrawBackground()

font = pygame.font.Font(None, 36)
text = font.render("Start Game", 1, (10, 10, 10))
textpos = text.get_rect(centerx = background.get_width()/2, centery= background.get_height()/2 - 100)
background.blit(text, textpos)

#screen.blit(background, (0,0))
#pygame.display.flip()

DrawScreen(screen, background)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_UP:
                """  """
                background = DrawBackground()
                font.set_bold(True)
                DrawFont(font, background)
                DrawScreen(screen, background)
            elif event.key == K_DOWN:
                """  """
                background = DrawBackground()
                font.set_bold(False)
                DrawFont(font, background)
                DrawScreen(screen, background)