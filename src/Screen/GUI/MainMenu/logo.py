import pygame

from pygame.locals import *
from Screen.GUI.pygame_helper import load_image

class Logo:
    """ Represents the Logo on the screen """
    
    def __init__(self):
        """ Builds the logo """
        self.image = load_image("PkmnLogo.png")
        
    def draw(self, background):
        """ Draws the logo """
        imgPos = self.image.get_rect(centerx = background.get_width()/2, centery = background.get_height()/4)
        background.blit(self.image, imgPos)