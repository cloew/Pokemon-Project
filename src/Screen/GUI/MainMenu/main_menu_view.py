import random

import pygame
from pygame.locals import *

from scrolling_map import ScrollingMap
from logo import Logo
from menu_view import MenuView

class MainMenuScreen:
    """ Main Menu screen """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.font = pygame.font.SysFont("Times New Roman", 36)
        self.map = ScrollingMap()
        self.logo = Logo()
        self.menuView = MenuView(menu)
        
    def update(self):
        """ Update the screen """
        self.map.update()
        
    def draw(self, window):
        """ Draw the window """
        self.map.draw(window)
        self.logo.draw(window)
        self.menuView.draw(window)