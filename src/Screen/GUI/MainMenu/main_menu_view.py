import random

import pygame
from pygame.locals import *

from scrolling_map import map
from logo import Logo
from menu_view import MenuView

class MainMenuScreen:
    """ Main Menu screen """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.logo = Logo()
        self.menuView = MenuView(menu)
        
    def update(self):
        """ Update the screen """
        map.update()
        
    def draw(self, window):
        """ Draw the window """
        map.draw(window)
        self.logo.draw(window)
        self.menuView.draw(window)