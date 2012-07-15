import pygame

from pygame.locals import *
from Screen.GUI.view import View
from Screen.GUI.pygame_helper import load_image

class Logo(View):
    """ Represents the Logo on the screen """
    
    def __init__(self):
        """ Builds the logo """
        self.image = load_image("PkmnLogo.png")
        
    def draw(self):
        """ Draws the logo """
        return self.image