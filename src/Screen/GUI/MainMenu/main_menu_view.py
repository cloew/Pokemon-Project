import random

import pygame
from pygame.locals import *

from scrolling_map import ScrollingMap
from logo import Logo
from menu import Menu

class MainMenuScreen:
    """ Main Menu screen """
    
    def __init__(self, menu):
        """  """
        self.model = menu
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
        if event.type == QUIT:
            self.model.running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            self.model.running = False
        else:
            self.menu.processEvent(event)
            
    def up(self):
        """  """
        self.menu.up()
        
    def down(self):
        """  """
        self.menu.down()