import random

import pygame
from pygame.locals import *

from Screen.Pygame.screen import Screen
from scrolling_map import map
from logo import Logo
from menu_view import MenuView

class MainMenuScreen(Screen):
    """ Represents the Main Menu screen """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.logo = Logo()
        self.menuView = MenuView(menu)
        
    def update(self):
        """ Update the screen """
        map.update()
        
    def draw(self, window):
        """ Draws the screen to the provided window """
        surface = pygame.Surface((window.width, window.height))
        self.drawMap(surface)
        self.drawLogo(surface)
        self.drawMenu(surface)
        return surface
        
    def drawMap(self, surface):
        """ Draws the map to the window """
        mapSurface = map.draw()
        surface.blit(mapSurface, (0, 0))
        # window.draw(mapSurface, (0,0))
        
    def drawLogo(self, surface):
        """ Draws the Logo to the window """
        logoSurface = self.logo.draw()
        logoPosition = self.getCenteredRect(surface, logoSurface, .5, .25) 
        surface.blit(logoSurface, logoPosition)
        # window.draw(logoSurface, logoPosition)
        
    def drawMenu(self, surface):
        """ Draws the Menu to the window """
        menuSurface = self.menuView.draw()
        menuPosition = self.getCenteredRect(surface, menuSurface, .5, 11.0/16)
        surface.blit(menuSurface, menuPosition)
        # window.draw(menuSurface, menuPosition)
        