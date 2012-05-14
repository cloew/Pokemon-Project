import random

import pygame
from pygame.locals import *
from pygame.transform import scale

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
    image, rect = load_image("pokeball.png")
    return image

def DrawBackground(mapLoc):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((100, 100, 100))
    image, rect = load_image("pokearth.png")
    rect = Rect(int(mapLoc[0]), int(mapLoc[1]), 640, 480)
    
    imgPiece = image.subsurface(rect)
    background.blit(imgPiece, (0, 0))
    
    DrawLogo(background)
    return background
    
def DrawLogo(background):
    image, rect = load_image("PkmnLogo.png")
    imgPos = image.get_rect(centerx = background.get_width()/2, centery = background.get_height()/4)
    background.blit(image, imgPos)

def DrawFont(font, background): 
    text = font.render("Start Game", 1, (10, 10, 10))
    textpos = text.get_rect(centerx = background.get_width()/2, centery= background.get_height()/2)
    background.blit(text, textpos)
    
def DrawScreen(screen, background): 
    screen.blit(background, (0,0))
    Update()
    
def Update():
    pygame.display.flip()

pygame.init()
pygame.display.set_icon(GetIcon())
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pokemon')
pygame.mouse.set_visible(0)

background = DrawBackground((0,0))
clock = pygame.time.Clock()
#font = pygame.font.SysFont("Microsoft Sans Serif", 36)
font = pygame.font.SysFont("Times New Roman", 36)
DrawFont(font, background)
DrawScreen(screen, background)

print pygame.font.get_fonts()


image, rect = load_image("pokearth.png")

xRange = range(1100-640)
yRange = range(850-480)
d = 1

coord = [0,0]
mapLoc = [0,0]
diff = [0, 0]

view_rect = Rect(0, 0, 640, 480)
screen.set_clip((0, 0, 640, 480))

running = True
while running:
    clock.tick(60)
    
    if coord == mapLoc:
        coord[0] = random.choice(xRange)
        coord[1] = random.choice(yRange)
    else:
        diff[0] = coord[0] - mapLoc[0]
        diff[1] = coord[1] - mapLoc[1]
        
        if diff[0] > diff[1]:
            if diff[0] == 0:
                denom = 1
            else:
                denom = float(abs(diff[0]))
            mapLoc[0] += diff[0]/denom
            mapLoc[1] += diff[1]/denom
        else:
            if diff[1] == 0:
                denom = 1
            else:
                denom = float(abs(diff[1]))
            mapLoc[0] += diff[0]/denom
            mapLoc[1] += diff[1]/denom
    
    # mapLoc[0] += d
    # mapLoc[1] += d
    
    # if mapLoc[0] > 1100-640:
        # mapLoc[0] = 1100-640
        # d = -1
    # elif mapLoc[0] < 0:
        # mapLoc[0] = 0
        # d = 1
        
    # if mapLoc[1] > 850-480:
        # mapLoc[1] = 850-480
        # d = -1
    # elif mapLoc[1] < 0:
        # mapLoc[1] = 0
        # d = 1
        
    background = DrawBackground(mapLoc)
        
    # Event
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_UP: 
                font.set_bold(True)                
            elif event.key == K_DOWN:
                font.set_bold(False)
                
    DrawFont(font, background)
    DrawScreen(screen, background)