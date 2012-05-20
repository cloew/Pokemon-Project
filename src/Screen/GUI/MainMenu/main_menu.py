import random

import pygame
from pygame.locals import *

from scrolling_map import ScrollingMap
from logo import Logo
from menu import Menu

class MainMenu:
    """ Main Menu screen """
    
    def __init__(self):
        """  """
        self.font = pygame.font.SysFont("Times New Roman", 36)
        self.map = ScrollingMap()
        self.logo = Logo()
        self.menu = Menu()
        
    def update(self):
        """ Update the screen """
        self.map.update()
        
    def draw(self, window):
        """ Draw the window """
        self.map.draw(window)
        self.logo.draw(window)
        self.menu.draw(window)
        
    def processEvent(self, event):
        """ Process Commands """
        if event.type == KEYDOWN:
            if event.key == K_UP: 
                self.menu.setBold(True)
            elif event.key == K_DOWN:
                self.menu.setBold(False)