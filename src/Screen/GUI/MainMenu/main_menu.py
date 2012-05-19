import sys
sys.path.append("C:\\cygwin\\home\\Programming\\Pokemon-Python\\src")

import random

import pygame
from pygame.locals import *
from pygame.transform import scale

from scrolling_map import ScrollingMap
from logo import Logo

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

clock = pygame.time.Clock()
#font = pygame.font.SysFont("Microsoft Sans Serif", 36)
font = pygame.font.SysFont("Times New Roman", 36)



background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((100, 100, 100))
map = ScrollingMap()
logo = Logo()

running = True
while running:
    clock.tick(60)
    
    map.update()
    background = map.drawScrollingMap(background)
    logo.draw(background)
        
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