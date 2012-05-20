import random

import pygame
from pygame.locals import *
from pygame.transform import scale

from scrolling_map import ScrollingMap
from logo import Logo

class MainMenu:
    """ Main Menu screen """
    
    def __init__(self):
        """  """
        self.font = pygame.font.SysFont("Times New Roman", 36)
        self.map = ScrollingMap()
        self.logo = Logo()
        
    def update(self):
        """ Update the screen """
        self.map.update()
        
    def draw(self, window):
        """ Draw the window """
        self.map.draw(window)
        self.logo.draw(window)
        self.drawFont(window)
        
    def drawFont(self, window): 
        """ Draw the menu """
        text = self.font.render("Start Game", 1, (10, 10, 10))
        textpos = text.get_rect(centerx = window.get_width()/2, centery= window.get_height()/2)
        window.blit(text, textpos)
        
    def processCommands(self):
        """ Process Commands """
        running = True
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_UP: 
                    self.font.set_bold(True)                
                elif event.key == K_DOWN:
                    self.font.set_bold(False)
                    
        return running