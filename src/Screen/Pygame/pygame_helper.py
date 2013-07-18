import pygame
from pygame.locals import *

def load_image(name, colorkey=None):
    fullname = "resources/images/" + name
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image
    
def GetTransparentSurface(width, height):
    """ Constructs a transparent pygame surface """
    surface = pygame.Surface((width, height), flags=pygame.SRCALPHA)
    surface.fill((0,0,0,0))
    return surface